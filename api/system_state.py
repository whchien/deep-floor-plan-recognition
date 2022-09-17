from api.in_mem_floor_plans import InMemFloorPlans
from api.model_initializer import init_model

# Model to predict compartments, room functions and boundaries
path_weights = 'floor_plan_model/model/G'
model = init_model(path_weights=path_weights)

# Reference to uploaded images
floor_plan_in_mem_db = InMemFloorPlans()

# Folder to temporarily store processed images
tmp_folder_path = 'tmp/'
