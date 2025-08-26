import time
from train import Train

def intro():
    """
    Display the introduction sequence for the game.
    Uses timed pauses to create dramatic effect and
    sets the scene for the player.
    """
    print("")
    time.sleep(2)
    print("==============================================================")
    print("The train races through the cold winter countryside,")
    print("wheels thundering on the tracks.")
    print("==============================================================")
    
    time.sleep(2)
    print("You are sleeping in your bed.")
    print("==============================================================")
    
    time.sleep(2)
    print("A sharp jolt wakes you.")
    print("The train is slowing down and stopping...")
    print("==============================================================")
    
    time.sleep(2)
    print("A guard pokes his head into your room.")
    print("==============================================================")
    
    time.sleep(2)
    print("“Please sir, you are our only hope in getting to our location”")
    print("==============================================================")
    
    time.sleep(3)
    print("The guard takes you to the cab of the engine and")
    print("informs you that the driver and fireman have both collapsed.")
    print("==============================================================")
    
    time.sleep(3)
    print("\nIt’s up to YOU to drive the train!\n")


def game_loop():
    """
    Main loop of the game.
    - Creates a Train object.
    - Displays the game introduction.
    - Repeatedly asks the player for input to control the train.
    - Updates train state based on player actions.
    - Ends the game when the boiler is no longer running or player quits.
    """
    train = Train()  # Create a new Train instance
    intro()          # Run the introductory sequence

    print("Welcome to the Steam Train Simulator!")
    print("Keep the fire burning, water filled,")
    print("and pressure steady to keep running.")

    # Main game loop runs while the boiler is operational
    while train.boiler.is_running:
        train.status()  # Display current status of train and boiler
        
        # Show player options
        print("What do you want to do?")
        print("1. Add coal")
        print("2. Add water")
        print("3. Light fire")
        print("4. Extinguish fire")
        print("5. Open throttle")
        print("6. Apply brake")
        print("7. Wait")
        print("8. Quit")

        choice = input("> ")  # Get player input

        # Perform action based on player choice
        if choice == "1":
            train.boiler.add_coal()
        elif choice == "2":
            train.boiler.add_water()
        elif choice == "3":
            train.boiler.light_fire()
        elif choice == "4":
            train.boiler.extinguish_fire()
        elif choice == "5":
            train.apply_throttle()
        elif choice == "6":
            train.apply_brake()
        elif choice == "7":
            print("You wait...")
        elif choice == "8" or choice.lower() == "q":
            # Quit the game
            break
        else:
            print("Invalid option.")

        train.update()  # Update train state (speed, pressure, distance)
        time.sleep(1)   # Pause briefly for game pacing

    print("Game Over.")  # End message when the game loop finishes