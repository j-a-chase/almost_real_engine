################################################################################
# File: engine.py
# Date: 13 February 2024
# Description:
#
# Class file for the engine
#
################################################################################

# module imports
import pygame

# class imports
from .window import Window

class Engine():
    def __init__(self) -> None:
        '''
        Constructor for Engine class

        Parameters: None

        Returns: None
        '''
        self.window = None

    def run(self, width: int=800, height: int=600, caption: str="New Pygame Application") -> None:
        '''
        Runs the engine.

        Parameters: None

        Returns: None
        '''
        self.window = Window(width=width, height=height, caption=caption)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()
            
            self.window.draw_prism()
            pygame.time.wait(10)

    def close_game(self) -> None:
        '''
        Handles events that cause the game to close

        Parameters: None

        Returns: None
        '''
        pygame.quit()
        exit()

if __name__ == '__main__': assert False, 'This is a class file. Import its \
    contents into another file.'
