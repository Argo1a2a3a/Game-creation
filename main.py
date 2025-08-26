# Import the main game loop function from the game module
from game import game_loop

# Standard Python idiom to ensure code only runs when this file is executed directly
# and not when it is imported as a module in another file
if __name__ == "__main__":
    # Start the game by calling the main game loop
    game_loop()