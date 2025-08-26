import random

class Weather:
    def __init__(self):
        # Randomly select the weather condition when the object is created
        # Possible values are "Clear", "Snowing", or "Blizzard"
        self.condition = random.choice(["Clear", "Snowing", "Blizzard"])