################################################################################
# File: sphere.py
# Date: 21 March 2024
# Description:
#
# Class file for the Sphere child class
#
################################################################################

# imports
from .shape import Shape
from OpenGL.GLU import gluNewQuadric, gluSphere
from typing import Tuple

class Sphere(Shape):
    def __init__(self, radius: float,
                 color: Tuple[float, float, float]=(1.0, 1.0, 1.0),
                 position: Tuple[float, float, float]=(0.0, 0.0, 0.0)) -> None:
        '''
        Constructor

        Parameters:
            - radius: float representing sphere radius
            - color: tuple of floats representing the color
            - position: tuple of floats representing the position

        Returns: None
        '''
        # call parent constructor
        super().__init__(color, position)

        # initialize radius
        self.radius = radius

    def draw_shape(self) -> None:
        '''
        Overridden draw_shape function to draw the sphere

        Parameters: None

        Returns: None
        '''
        # Use GLU quadric to draw the sphere
        quad = gluNewQuadric()
        gluSphere(quad, self.radius, 32, 32)

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
