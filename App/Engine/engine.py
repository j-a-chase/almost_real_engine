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
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from OpenGL.GLU import gluLookAt
# class imports
from .window import Window
from .physics import Physics


class Engine():
    def __init__(self) -> None:
        '''
        Constructor for Engine class

        Parameters: None

        Returns: None
        '''
        pygame.init()
        self.window = None
        self.camera_pos = [0.0, 0.0, 5.0]
        self.camera_front = [0.0, 0.0, -1.0]
        self.camera_up = [0.0, 1.0, 0.0]
        self.yaw = -90.0  # yaw is initialized to -90.0 degrees since a yaw of 0.0 results in a direction vector pointing to the right
        self.pitch = 0.0
        self.lastX, self.lastY = 400, 300
        self.first_mouse = True
        pygame.mouse.set_visible(False)
        
        self.room_size = [50, 10, 50]
        self.physics = Physics(self.room_size)
        

    def run(self, width: int=800, height: int=600, caption: str="New Pygame Application") -> None:
        '''
        Runs the engine.

        Parameters: None

        Returns: None
        '''
        self.window = Window(width=width, height=height, caption=caption)
        pygame.mouse.set_pos((self.lastX, self.lastY))
        pygame.event.set_grab(True)

        room_width = self.room_size[0]
        room_height = self.room_size[1]
        room_length = self.room_size[2]
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Check if ESC key is pressed
                        self.close_game()  # Call close_game to exit
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_movement(*event.rel)
                    
            self.handle_input()
            self.draw_room(room_width, room_height, room_length)

    def close_game(self) -> None:
        '''
        Handles events that cause the game to close

        Parameters: None

        Returns: None
        '''
        pygame.quit()
        exit()

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()
        camera_speed = 0.005
        new_pos = self.camera_pos[:]  # Copy of the camera position for testing potential movement

        # Calculate potential new position based on input
        if keys[pygame.K_w]:
            for i in range(3):
                new_pos[i] += self.camera_front[i] * camera_speed
        if keys[pygame.K_s]:
            for i in range(3):
                new_pos[i] -= self.camera_front[i] * camera_speed
        if keys[pygame.K_a] or keys[pygame.K_d]:
            # Calculate right vector
            cross_product = [self.camera_front[1] * self.camera_up[2] - self.camera_front[2] * self.camera_up[1],
                            self.camera_front[2] * self.camera_up[0] - self.camera_front[0] * self.camera_up[2],
                            self.camera_front[0] * self.camera_up[1] - self.camera_front[1] * self.camera_up[0]]
            norm = math.sqrt(sum(i**2 for i in cross_product))
            right = [i / norm for i in cross_product]

            # Apply movement
            if keys[pygame.K_a]:
                for i in range(3):
                    new_pos[i] -= right[i] * camera_speed
            if keys[pygame.K_d]:
                for i in range(3):
                    new_pos[i] += right[i] * camera_speed

    # Check for collision with the new position before applying
        if not self.physics.check_collision(new_pos, self.room_size):
            self.camera_pos = new_pos

            
    def handle_mouse_movement(self, xoffset, yoffset, sensitivity=0.05):
            if self.first_mouse:
                self.lastX, self.lastY = pygame.mouse.get_pos()
                self.first_mouse = False

            xoffset *= sensitivity
            yoffset *= sensitivity * -1

            self.yaw += xoffset
            self.pitch += yoffset

            if self.pitch > 89.0:
                self.pitch = 89.0
            if self.pitch < -89.0:
                self.pitch = -89.0

            direction = [
            math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
            math.sin(math.radians(self.pitch)),
            math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        ]
            norm = math.sqrt(sum(i**2 for i in direction))
            self.camera_front = [i / norm for i in direction]

    def draw_room(self, width: float, height: float, length: float) -> None:
        '''
        Draws a room on the screen

        Parameters:
        - width: float, the width of the room
        - height: float, the height of the room
        - length: float, the length of the room

        Returns: None
        '''
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (self.window.width / self.window.height), 0.1, 100.0)
        eye = [self.camera_pos[i] + self.camera_front[i] for i in range(3)]
        gluLookAt(self.camera_pos[0], self.camera_pos[1], self.camera_pos[2],
                  eye[0], eye[1], eye[2],
                  self.camera_up[0], self.camera_up[1], self.camera_up[2])

        # Draw the room
        glBegin(GL_QUADS)

        # Floor
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(-width/2, -height/2, -length/2)
        glVertex3f(width/2, -height/2, -length/2)
        glVertex3f(width/2, -height/2, length/2)
        glVertex3f(-width/2, -height/2, length/2)

        # Ceiling
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(-width/2, height/2, -length/2)
        glVertex3f(width/2, height/2, -length/2)
        glVertex3f(width/2, height/2, length/2)
        glVertex3f(-width/2, height/2, length/2)

        # Walls
        glColor3f(0.5, 0.0, 0.0)
        glVertex3f(-width/2, -height/2, -length/2)
        glVertex3f(-width/2, height/2, -length/2)
        glVertex3f(-width/2, height/2, length/2)
        glVertex3f(-width/2, -height/2, length/2)

        glColor3f(0.0, 0.5, 0.0)
        glVertex3f(width/2, -height/2, -length/2)
        glVertex3f(width/2, height/2, -length/2)
        glVertex3f(width/2, height/2, length/2)
        glVertex3f(width/2, -height/2, length/2)

        glColor3f(0.0, 0.0, 0.5)
        glVertex3f(-width/2, -height/2, -length/2)
        glVertex3f(width/2, -height/2, -length/2)
        glVertex3f(width/2, height/2, -length/2)
        glVertex3f(-width/2, height/2, -length/2)

        glColor3f(0.5, 0.5, 0.0)
        glVertex3f(-width/2, -height/2, length/2)
        glVertex3f(width/2, -height/2, length/2)
        glVertex3f(width/2, height/2, length/2)
        glVertex3f(-width/2, height/2, length/2)
        glEnd()

        pygame.display.flip()

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
