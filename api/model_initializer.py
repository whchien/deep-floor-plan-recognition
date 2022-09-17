import os

from deepfloor.net import *

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def init_model(path_weights):
    # initialize the model
    floor_plan_model = deepfloorplanModel()

    # restore weights from previous training
    floor_plan_model.load_weights(path_weights)

    return floor_plan_model
