import random

class Terrain:
    def __init__(self):
        # Randomly select the terrain type when the object is created
        # Possible values: "Rocky", "Fields", "Hilly", "Forest"
        self.type = random.choice(["Rocky", "Fields", "Hilly", "Forest"])

    def describe(self):
        # Print a description of the current terrain
        print(f"The train is now passing through {self.type} terrain.")