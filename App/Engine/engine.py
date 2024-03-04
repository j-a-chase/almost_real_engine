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
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

class Engine():
    def __init__(self) -> None:
        '''
        Constructor for Engine class

        Parameters: None

        Returns: None
        '''
        self.window = None
        self.angle = None

    def run(self, width: int=800, height: int=600, caption: str="New Pygame Application") -> None:
        '''
        Runs the engine.

        Parameters: None

        Returns: None
        '''
        self.window = Window(width=width, height=height, caption=caption)
        self.angle = 0.0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()
            
            self.draw_prism()
            pygame.time.wait(10)

    def close_game(self) -> None:
        '''
        Handles events that cause the game to close

        Parameters: None

        Returns: None
        '''
        pygame.quit()
        exit()

    
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

if __name__ == '__main__': assert False, 'This is a class file. Import its \
    contents into another file.'
