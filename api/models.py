import os
from dataclasses import dataclass
from django.db import models
import pandas as pd


class RawImageModel(models.Model):
    floor_plan = models.ImageField()


@dataclass
class FloorPlanCompartments:
    closets = 0
    bathrooms = 0
    living_rooms = 0
    bedrooms = 0
    halls = 0
    doors_windows = 0


class FloorPlansCsvData:

    def __init__(self):
        self.file_names = []
        self.total_count = []
        self.closet_count = []
        self.bathroom_count = []
        self.living_room_count = []
        self.bedroom_count = []
        self.hall_count = []
        self.door_window_count = []

    def append_special(self, file_name, compartments):
        self.file_names.append(file_name)
        total = compartments.closets + compartments.bathrooms + compartments.living_rooms + compartments.bedrooms + compartments.halls
        self.total_count.append(total)
        self.closet_count.append(compartments.closets)
        self.bathroom_count.append(compartments.bathrooms)
        self.living_room_count.append(compartments.living_rooms)
        self.bedroom_count.append(compartments.bedrooms)
        self.hall_count.append(compartments.halls)
        self.door_window_count.append(compartments.doors_windows)

    def to_csv_file(self):
        csv_file_name = "tmp/data.csv"
        if os.path.exists(csv_file_name):
            os.remove(csv_file_name)

        data = {
            "file_name": self.file_names,
            "total_num_compartments": self.total_count,
            "num_closets": self.closet_count,
            "num_bathrooms": self.bathroom_count,
            "num_living_rooms": self.living_room_count,
            "num_bedrooms": self.bedroom_count,
            "num_halls": self.hall_count,
            "num_doors_windows": self.door_window_count
        }
        df = pd.DataFrame(data)
        # compression_opts = dict(method='zip', archive_name='data.csv') compression=compression_opts
        return df.to_csv(csv_file_name, index=False)
