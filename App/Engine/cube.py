################################################################################
# File: cube.py
# Date: 21 March 2024
# Description:
#
# Class file for the Cube child class
#
################################################################################

# imports
from .shape import Shape
from OpenGL.GL import glBegin, glEnd, glVertex3f, GL_QUADS
from typing import Tuple

class Cube(Shape):
    def __init__(self, side_length: float,
                 color: Tuple[float, float, float]=(1.0, 1.0, 1.0),
                 position: Tuple[float, float, float]=(0.0, 0.0, 0.0)) -> None:
        '''
        Constructor

        Parameters:
            - side_length: float representing the side length
            - color: tuple of floats representing the color
            - position: tuple of floats representing the position

        Returns: None
        '''
        # call parent constructor
        super().__init__(color, position)

        # initialize side length
        self.side_length = side_length

    def draw_shape(self) -> None:
        '''
        Overridden draw_shape function to draw the cube

        Parameters: None

        Returns: None
        '''
        # Manually draw cube using immediate mode
        side = self.side_length / 2

        glBegin(GL_QUADS)

        # Front face
        glVertex3f(-side, -side, side)
        glVertex3f(side, -side, side)
        glVertex3f(side, side, side)
        glVertex3f(-side, side, side)

        # Back face
        glVertex3f(-side, -side, -side)
        glVertex3f(side, -side, -side)
        glVertex3f(side, side, -side)
        glVertex3f(-side, side, -side)

        # Top face
        glVertex3f(-side, side, -side)
        glVertex3f(side, side, -side)
        glVertex3f(side, side, side)
        glVertex3f(-side, side, side)

        # Bottom face
        glVertex3f(-side, -side, -side)
        glVertex3f(side, -side, -side)
        glVertex3f(side, -side, side)
        glVertex3f(-side, -side, side)

        # Left face
        glVertex3f(-side, -side, -side)
        glVertex3f(-side, side, -side)
        glVertex3f(-side, side, side)
        glVertex3f(-side, -side, side)

        # Right face
        glVertex3f(side, -side, -side)
        glVertex3f(side, side, -side)
        glVertex3f(side, side, side)
        glVertex3f(side, -side, side)

        glEnd()

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
