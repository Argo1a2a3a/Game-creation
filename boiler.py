from colorama import Fore, Back, Style, init

class Boiler:
    def __init__(self):
        """
        Initialize the Boiler object with default levels for water, coal, and pressure.
        Also track whether the fire is lit and if the train is running.
        """
        self.water_level = 100      # Current water in the boiler (max 100 units)
        self.coal_in_fire = 0       # Coal currently burning in the firebox
        self.tender_coal = 500      # Total coal supply in the tender
        self.tender_water = 500     # Total water supply in the tender
        self.pressure = 0           # Current boiler pressure in psi
        self.max_pressure = 250     # Maximum allowable pressure
        self.is_running = True      # If the train is running
        self.fire_lit = False       # Status of the fire (lit or not)

    def light_fire(self):
        """
        Light the fire in the boiler.
        Can only be done if there is coal in the firebox.
        """
        if not self.fire_lit and self.coal_in_fire > 0:
            self.fire_lit = True
            print("You strike a match and light the fire. The firebox glows warmly.")
        elif self.fire_lit:
            print("The fire is already burning.")
        else:
            print("You need coal in the firebox to light it.")

    def extinguish_fire(self):
        """
        Extinguish the fire in the boiler if it is currently burning.
        """
        if self.fire_lit:
            self.fire_lit = False
            print("You douse the flames. The fire is extinguished.")
        else:
            print("The fire is already out.")

    def add_coal(self, amount=5):
        """
        Add coal to the firebox from the tender.
        Default amount is 5 units, cannot exceed tender supply.
        """
        if self.tender_coal >= amount:
            self.coal_in_fire += amount
            self.tender_coal -= amount
            print(f"You shovel {amount} coal into the firebox.")
        else:
            print("Not enough coal in the tender!")

    def add_water(self):
        """
        Add water to the boiler from the tender.
        Only works if train is running and does not exceed max water level.
        """
        if not self.is_running:
            return

        amount = 5  # Water units added per action

        if self.tender_water <= 0:
            print("No water left in the tender!")
            return

        if self.water_level + amount > 100:
            print("Unable to add more water.")
            return

        self.water_level += amount
        self.tender_water -= amount

        # Ensure tender water never goes negative
        if self.tender_water < 0:
            self.tender_water = 0

        print(f"You add {amount} units of water to the boiler.")

    def update(self, train_speed):
        """
        Update the boiler state for one iteration.
        - Burns coal if fire is lit
        - Increases pressure from fire
        - Slowly reduces pressure naturally
        - Consumes water while fire is burning
        - Checks for boiler explosion or out-of-coal conditions
        """
        if not self.is_running:
            return

        if self.fire_lit:
            if self.coal_in_fire > 0:
                # Burn one unit of coal
                self.coal_in_fire -= 1
                if self.coal_in_fire < 0:
                    self.coal_in_fire = 0

                # Increase pressure from fire
                self.pressure += 5

                # Small natural pressure loss
                self.pressure -= 1
                if self.pressure < 0:
                    self.pressure = 0

                # Consume water while fire is burning
                self.water_level -= 1
                if self.water_level < 0:
                    self.water_level = 0
            else:
                # Fire goes out if no coal remains
                self.fire_lit = False
                print("The fire has gone out because the firebox is empty!")

        # Explosion check: fire lit but no water
        if self.fire_lit and self.water_level <= 0 and self.coal_in_fire > 0:
            print("BOOM! The boiler exploded due to no water.")
            self.is_running = False

        # Out-of-coal and fire gone → train stops
        if self.tender_coal <= 0 and self.coal_in_fire <= 0 and not self.fire_lit:
            print("No coal left at all. The train grinds to a halt.")
            self.is_running = False

    def status(self):
        """
        Display the current status of the boiler in a formatted way.
        Shows water, coal, tender resources, pressure, and fire state.
        Also adds some visual coloring using colorama.
        """
        # Dynamic spacing for printing
        gap1 = 2 if self.water_level == 100 else 4 if self.water_level < 10 else 3
        gap2 = 8 if self.coal_in_fire < 10 else 7 if self.coal_in_fire < 100 else 6
        gap3 = 4 if self.tender_coal >= 100 else 6 if self.tender_coal < 10 else 5
        gap4 = 3 if self.tender_water >= 100 else 5 if self.tender_water < 10 else 4
        gap5 = 11 if self.pressure < 10 else 10 if self.pressure < 100 else 9
        gap6 = 13 if self.fire_lit else 14

        print(" __________________________")
        print("|                          |")
        print(f"|Water in boiler: {self.water_level}/100" + " " * gap1 + "|")
        print(f"|Coal in firebox: {self.coal_in_fire}" + " " * gap2 + "|")
        print(f"|Tender coal: {self.tender_coal} units" + " " * gap3 + "|")
        print(f"|Tender water: {self.tender_water} units" + " " * gap4 + "|")
        print(f"|Pressure: {self.pressure} psi" + " " * gap5 + "|")
        print(f"|Fire lit: {'Yes' if self.fire_lit else 'No'}" + " " * gap6 + "|")
        print("|__________________________|")

        # Color-coded bars
        init()
        textc = "|     |"
        textw = "     |"
        textf1 = "              |"
        textf2 = "______________|"

        colored_textc = textc.replace(" ", f"{Back.BLACK} {Style.RESET_ALL}")
        colored_textw = textw.replace(" ", f"{Back.BLUE} {Style.RESET_ALL}")
        colored_textf2 = textf2.replace("_", f"{Back.RED} {Style.RESET_ALL}")
        colored_textf1 = textf1.replace(" ", f"{Back.RED} {Style.RESET_ALL}")

        # Show coal, water, and fire visually
        c = colored_textc if self.tender_coal > 400 else textc
        w = colored_textw if self.tender_water > 400 else textw
        f = colored_textf1 if self.fire_lit else textf1
        print(c + w + f)

        c = colored_textc if self.tender_coal >= 400 else textc
        w = colored_textw if self.tender_water >= 400 else textw
        f = colored_textf2 if self.fire_lit else textf2
        print(c + w + f)
        
        c = colored_textc if self.tender_coal >= 300 else textc
        w = colored_textw if self.tender_water >= 300 else textw
        print(c + w)

        c = colored_textc if self.tender_coal >= 200 else textc
        w = colored_textw if self.tender_water >= 200 else textw
        print(c + w)

        c = colored_textc if self.tender_coal >= 100 else textc
        w = colored_textw if self.tender_water >= 100 else textw
        print(c + w)