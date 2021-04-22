class InMemFloorPlans:
    def __init__(self):
        self.floor_plans = []
        self.floor_plan_names = []

    # TODO: Instead of writing to file, keep them in memory
    # Figure out how to convert InMemoryUploadedFile -> numpy image array
    def overwrite_floor_plans(self, floor_plans):
        self.floor_plans = floor_plans

    def get_floor_plans(self):
        return self.floor_plans
