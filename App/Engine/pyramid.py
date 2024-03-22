################################################################################
# File: pyramid.py
# Date: 21 March 2024
# Description:
#
# Class file for the Pyramid child class
#
################################################################################

# imports
from .shape import Shape
from typing import Tuple
from OpenGL.GL import GL_TRIANGLES, glBegin, glEnd, glVertex3f

class Pyramid(Shape):
    def __init__(self, base: float=1.0,
                 color: Tuple[float, float, float]=(1.0, 1.0, 1.0),
                 position: Tuple[float, float, float]=(0.0, 0.0, 0.0)) -> None:
        '''
        Constructor

        Parameters:
            - base: a float representing the base size
            - color: tuple of floats representing the color
            - position: tuple of floats representing the position

        Returns: None
        '''
        # call parent constructor
        super().__init__(color, position)

        # initialize base and height values (height is always proportional to
        # base, can change later if needed)
        self.base = base
        self.height = base * 1.5

    def draw_shape(self) -> None:
        '''
        Overridden draw_shape function to draw the pyramid

        Parameters: None

        Returns: None
        '''
        # Manually draw pyramid using immediate mode
        glBegin(GL_TRIANGLES)

        # Base
        glVertex3f(-self.base, -self.base, 0)
        glVertex3f(self.base, -self.base, 0)
        glVertex3f(self.base, self.base, 0)
        glVertex3f(-self.base, self.base, 0)

        # Sides
        glVertex3f(0, 0, self.height)
        glVertex3f(-self.base, -self.base, 0)
        glVertex3f(self.base, -self.base, 0)

        glVertex3f(0, 0, self.height)
        glVertex3f(self.base, -self.base, 0)
        glVertex3f(self.base, self.base, 0)

        glVertex3f(0, 0, self.height)
        glVertex3f(self.base, self.base, 0)
        glVertex3f(-self.base, -self.base, 0)

        glVertex3f(0, 0, self.height)
        glVertex3f(-self.base, self.base, 0)
        glVertex3f(-self.base, -self.base, 0)

        glEnd()

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
