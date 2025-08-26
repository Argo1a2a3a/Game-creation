import random

class Junction:
    def __init__(self):
        # Randomly set the distance (in km) to the next junction when the object is created
        self.distance = random.randint(5, 20)
        # Randomly choose the direction of the junction: "Left" or "Right"
        self.direction = random.choice(["Left", "Right"])

    def approach(self, train):
        # Check if the train has reached or passed the junction
        if self.distance <= 0:
            print(f"\nJunction ahead! The track splits {self.direction}.")
            print("Do you want to stop and choose a route? (yes/no)")
            choice = input("> ").lower()
            if choice == "yes":
                # Stop the train so the player can select a route
                train.speed = 0
                print("You stop at the junction and decide your route.")
                return True  # Indicates that the train has stopped for the junction
        return False  # Train continues without stopping