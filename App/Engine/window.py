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
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

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
        pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(caption)

        self.width = width
        self.height = height
        
        self.angle = 0.0

        self.__setup()

    def __setup(self) -> None:
        '''
        OpenGL setup function

        Parameters: None

        Returns: None
        '''
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.width / self.height), 0.1, 10.0)
        glTranslatef(0.0, 0.0, -3.0)  # Move back so we can see the prism
        glMatrixMode(GL_MODELVIEW)

    def draw_prism(self) -> None:
        '''
        Draws a rotating prism on the screen

        Parameters: None

        Returns: None
        '''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glRotatef(self.angle, 0.0, 1.0, 0.2)

        # generate triangles
        glBegin(GL_TRIANGLES)

        # Front face
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.5, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, 0.5)

        # Right face
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(0.0, 0.5, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, 0.5)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)

        # Back face
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(0.0, 0.5, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, -0.5, -0.5)

        # Left face
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.0, 0.5, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glEnd()

        # generate bottom square
        glBegin(GL_QUADS)

        # Bottom face
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, 0.5)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        pygame.display.flip()

        self.angle += 1.0


if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
