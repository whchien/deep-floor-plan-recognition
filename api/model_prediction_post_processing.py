import imageio
from skimage.transform import resize

from deepfloor.utils.util import *
from deepfloor.data import *
from deepfloor.net import *

# invert the color of wall line and background for presentation
room_function_color_codes = {
    0: [255, 255, 255],  # background
    1: [192, 192, 224],  # closet
    2: [192, 255, 255],  # batchroom/washroom
    3: [224, 255, 192],  # livingroom/kitchen/dining room
    4: [255, 224, 128],  # bedroom
    5: [255, 160, 96],  # hall
    6: [255, 224, 224],  # balcony
    7: [224, 224, 224],  # not used
    8: [224, 224, 128],  # not used
    9: [255, 60, 128],  # extra label for opening (door&window)
    10: [0, 0, 0]  # extra label for wall line
}


def process_img(file_name, model):
    im = imageio.imread('tmp/' + file_name)  # imagio read might need to be modified
    im = im.astype(np.float32)
    im = resize(im, (512, 512, 3)) / 255.
    x = np.expand_dims(im, axis=0)

    logits_r, logits_cw = model(x)

    # covert to image
    room_type = convert_one_hot_to_image(logits_r, act='softmax', dtype='int')
    room_boundary = convert_one_hot_to_image(logits_cw, act='softmax', dtype='int')

    # reshape it
    room_type = np.squeeze(room_type)
    room_boundary = np.squeeze(room_boundary)

    # merge results
    floorplan = room_type.copy()
    floorplan[room_boundary == 1] = 9  # door & window, turning pink
    floorplan[room_boundary == 2] = 10  # wall, turning black
    floorplan_rgb = ind2rgb(floorplan, color_map=room_function_color_codes)

    # post-process
    im_ind = rgb2ind(floorplan_rgb, color_map=room_function_color_codes)

    rm_ind = im_ind.copy()
    rm_ind[im_ind == 9] = 0
    rm_ind[im_ind == 10] = 0

    bd_ind = np.zeros(im_ind.shape, dtype=np.uint8)
    bd_ind[im_ind == 9] = 9
    bd_ind[im_ind == 10] = 10

    hard_c = (bd_ind > 0).astype(np.uint8)

    # region from room prediction it self
    rm_mask = np.zeros(rm_ind.shape)
    rm_mask[rm_ind > 0] = 1
    # region from close_wall line
    cw_mask = hard_c
    # refine close wall mask by filling the grap between bright line
    cw_mask = fill_break_line(cw_mask)

    fuse_mask = cw_mask + rm_mask
    fuse_mask[fuse_mask >= 1] = 255

    # refine fuse mask by filling the hole
    fuse_mask = flood_fill(fuse_mask)
    fuse_mask = fuse_mask // 255

    # one room one label
    new_rm_ind = refine_room_region(cw_mask, rm_ind)

    # ignore the background mislabeling
    new_rm_ind = fuse_mask * new_rm_ind

    new_rm_ind[bd_ind == 9] = 9
    new_rm_ind[bd_ind == 10] = 10
    rgb = ind2rgb(new_rm_ind, color_map=room_function_color_codes)

    plt.imshow(im)
    plt.savefig("tmp/original_" + file_name)
    plt.clf()
    plt.imshow(rgb / 255.)
    plt.savefig("tmp/processed_" + file_name)
    return new_rm_ind


def rgb2ind(im, color_map):
    ind = np.zeros((im.shape[0], im.shape[1]))

    for i, rgb in color_map.items():
        ind[(im == rgb).all(2)] = i

    return ind.astype(np.uint8)  # force to uint8


def ind2rgb(ind_im, color_map):
    rgb_im = np.zeros((ind_im.shape[0], ind_im.shape[1], 3))

    for i, rgb in color_map.items():
        rgb_im[(ind_im == i)] = rgb

    return rgb_im
