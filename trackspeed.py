import random

class TrackSpeed:
    def __init__(self):
        # Initialize the track speed limit randomly from a set of allowed speeds
        self.speed_limit = random.choice([60, 80, 100, 120])

    def update(self, train_speed):
        # Only update the track speed if the train is moving
        if train_speed > 0:
            # There is a 10% chance that the speed limit will change during this update
            if random.random() < 0.1:
                # Assign a new random speed limit from the allowed values
                self.speed_limit = random.choice([60, 80, 100, 120])