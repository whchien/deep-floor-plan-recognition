from skimage import measure

from api.models import FloorPlanCompartments


def get_compartment_count(processed_image, compartment_type, compartment_area):
    labels = measure.label(processed_image == compartment_type, connectivity=2)
    properties = measure.regionprops(labels)
    valid_label = set()
    for prop in properties:
        if prop.area > compartment_area:
            valid_label.add(prop.label)
    return len(valid_label)


def get_floor_plan_compartments(processed_image):
    compartments = FloorPlanCompartments
    compartments.closet = get_compartment_count(processed_image, 1, 200)
    compartments.bathroom = get_compartment_count(processed_image, 2, 120)
    compartments.living_room = get_compartment_count(processed_image, 3, 120)
    compartments.bedroom = get_compartment_count(processed_image, 4, 120)
    compartments.hall = get_compartment_count(processed_image, 5, 120)
    compartments.door = get_compartment_count(processed_image, 9, 80)
    return compartments
