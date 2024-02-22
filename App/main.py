################################################################################
# File: main.py
# Date: 13 February 2024
# Description:
#
# Main file for our game application
#
################################################################################

# imports
from Engine.engine import Engine

def main() -> None:
    '''
    Main Function

    Parameters: None

    Returns: None
    '''
    game = Engine()
    game.run()

if __name__ == "__main__": main()
