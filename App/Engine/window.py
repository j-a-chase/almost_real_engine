################################################################################
# File: window.py
# Date: 13 February 2024
# Description:
#
# Class file for making a window
#
################################################################################

# imports
import pygame

class Window():
    def __init__(self, width: int=800, height: int=600, caption: str="New Pygame Application") -> None:
        '''
        Constructor for Window class

        Parameters:
            - width: integer defaulting to 800px
            - height: integer defaulting to 600px
            - caption: string defaulting to 'New Pygame Application'
        '''
        pygame.init()

        pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

if __name__ == '__main__': assert False, 'This is a class file. Import its \
    contents into another file.'
