from boiler import Boiler
from trackspeed import TrackSpeed
from tracksteepness import TrackSteepness
from weather import Weather
from terrain import Terrain
from junction import Junction

class Train:
    def __init__(self):
        """
        Initialize a Train object with all its components.
        - Boiler to manage water, coal, and pressure
        - Speed, throttle, brake, and distance attributes
        - Track and environmental features
        """
        self.boiler = Boiler()        # Boiler for fuel, water, and pressure management
        self.speed = 0                # Current speed of the train (km/h)
        self.throttle = 0             # Throttle state (1 if open)
        self.brake = 0                # Brake state (1 if applied)
        self.distance = 0.0           # Distance traveled in km

        # Environmental and track features
        self.current_speed_limit = TrackSpeed()  # Current speed limit on track
        self.track_steepness = TrackSteepness()  # Current steepness of track
        self.weather = Weather()                 # Current weather condition
        self.terrain = Terrain()                 # Current terrain type
        self.junction = Junction()               # Next junction information

    def apply_throttle(self):
        """
        Open the throttle to increase speed if conditions allow:
        - Boiler pressure must be sufficient (>50 psi)
        - Fire must be lit
        If conditions are not met, print an appropriate message.
        """
        if self.boiler.pressure > 50 and self.boiler.fire_lit:
            self.throttle = 1
            self.speed += 10
            self.boiler.pressure -= 10  # Using pressure to accelerate
            print("You open the throttle. The train surges forward!")
        elif not self.boiler.fire_lit:
            print("The fire is out! You need to relight it before moving.")
        else:
            print("Not enough pressure to move!")

    def apply_brake(self):
        """
        Apply the brakes to slow down the train.
        Reduces speed by 10 km/h, cannot go below zero.
        """
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        self.brake = 1
        print("You apply the brake. The train slows down.")

    def update(self):
        """
        Update train state for one iteration of the game loop.
        - Update boiler (pressure, water, coal)
        - Update track speed
        - Adjust train speed based on throttle and fire
        - Track distance traveled
        - Update distance to next junction and handle junction approach
        """
        # Update boiler state (requires current speed)
        self.boiler.update(self.speed)

        # Update track speed limit if the train is moving
        self.current_speed_limit.update(self.speed)

        # Movement logic
        if self.throttle and self.boiler.pressure > 0 and self.boiler.fire_lit:
            self.speed += 1  # Gradual acceleration
        else:
            # Gradual slowdown if no fire or throttle
            if self.speed > 0:
                self.speed -= 2

        if self.speed < 0:
            self.speed = 0

        # Update distance traveled (km)
        self.distance += self.speed / 3600  # Assuming update called once per second

        # Update distance to next junction
        self.junction.distance -= self.speed / 3600
        if self.junction.distance <= 0:
            stopped = self.junction.approach(self)
            if stopped:
                # Reset environment when player chooses a new route at junction
                self.current_speed_limit = TrackSpeed()
                self.track_steepness = TrackSteepness()
                self.weather = Weather()
                self.terrain = Terrain()
                self.junction = Junction()

    def status(self):
        """
        Display the current status of the train:
        - Boiler status
        - Speed and distance
        - Track and environmental information
        """
        self.boiler.status()  # Show boiler stats
        print(f"Speed: {self.speed} km/h")
        print(f"Distance traveled: {self.distance:.2f} km")
        print(f"Track speed limit: {self.current_speed_limit.speed_limit} km/h")

        # Map numeric steepness to descriptive string
        steep_map = {0: "Flat", 1: "Mild", 2: "Steep", 3: "Very Steep"}
        print(f"Track steepness: {steep_map[self.track_steepness.steepness]}")

        print(f"Weather: {self.weather.condition}")
        print(f"Terrain: {self.terrain.type}")
        print(f"Distance to next junction: {self.junction.distance:.2f} km\n")