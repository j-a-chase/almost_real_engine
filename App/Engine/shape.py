################################################################################
# File: shape.py
# Date: 21 March 2024
# Description:
#
# Class file for the Shape base class
#
################################################################################

# imports
from OpenGL.GL import glPushMatrix, glColor3f, glTranslatef, glPopMatrix
from typing import Tuple

class Shape:
    def __init__(self, color: Tuple[float, float, float],
                 position: Tuple[float, float, float]) -> None:
        '''
        Constructor

        Parameters:
            - color: a tuple containing three float values to represent the
                     color
            - position: a tuple containing three float values to represent the 
                     position

        Returns: None
        '''
        self.color = color
        self.position = position

    def draw(self) -> None:
        '''
        Draws the given shape based on the child class implementation.

        Parameters: None

        Returns: None
        '''
        # Set color and position
        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(*self.position)
        self.draw_shape()
        glPopMatrix()

    # virtual function to be overridden
    def draw_shape(self) -> None: return

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
