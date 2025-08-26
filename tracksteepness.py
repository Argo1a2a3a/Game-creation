import random

class TrackSteepness:
    def __init__(self):
        # Randomly set the track steepness when the object is created
        # 0 = flat, 1 = mild, 2 = steep, 3 = very steep
        self.steepness = random.choice([0, 1, 2, 3])