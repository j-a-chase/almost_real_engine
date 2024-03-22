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
from OpenGL.GLU import *
from OpenGL.GLUT import *
import tkinter as tk
from tkinter import simpledialog

# class imports
from .window import Window
from .physics import Physics
from .cube import Cube
from .sphere import Sphere
from .pyramid import Pyramid


class Engine():
    def __init__(self) -> None:
        '''
        Constructor for Engine class

        Parameters: None

        Returns: None
        '''
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        self.window = None

        # This is where you enable depth testing
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        # Initialize camera position, front direction, and up direction
        self.camera_pos = (0.0, 0.0, 5.0)
        self.camera_front = (0.0, 0.0, -1.0)
        self.camera_up = (0.0, 1.0, 0.0)

        # Initialize camera angles and mouse position
        self.yaw = -90.0
        self.pitch = 0.0
        self.lastX = 400
        self.lastY = 300
        self.first_mouse = True

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        # Initialize physics
        self.room_size = (50, 10, 50)
        self.physics = Physics(self.room_size)
        
        # Initialize objects
        self.objects = []

    def run(self, width: int=800, height: int=600, 
            caption: str="New Pygame Application") -> None:
        '''
        Runs the engine.

        Parameters:
            - width: an integer with a default value of 800. Represents window
                width
            - height: an integer with a default value of 600. Represents window
                height
            - caption: a string with the default value of 'New Pygame
                Application', holds the title of the window

        Returns: None
        '''
        # Create a window
        self.window = Window(width=width, height=height, caption=caption)
        
        # Set the mouse position to the center of the window
        pygame.mouse.set_pos((self.lastX, self.lastY))

        # Lock the mouse to the window
        pygame.event.set_grab(True)

        # Set the camera position to the center of the room
        room_width, room_height, room_length = self.room_size
        
        # Main game loop
        while True:
            
            # Clear buffers
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()
                if event.type == pygame.KEYDOWN:
                    # Check if ESC key is pressed
                    if event.key == pygame.K_ESCAPE:
                        # Call close_game to exit
                        self.close_game()
                    if ((event.key == pygame.K_o) and (event.mod & pygame.KMOD_CTRL)):
                        self.create_object()

                # Check for mouse movement
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_movement(*event.rel)
             
            # Handle keyboard input
            self.handle_keyboard_inp()
            
            # Enable depth testing
            glEnable(GL_DEPTH_TEST)
            glDepthFunc(GL_LESS)
            
            # Disable depth mask and backface culling
            glDepthMask(GL_FALSE)
            glDisable(GL_CULL_FACE)
            
            # Draw the room
            self.draw_room(room_width, room_height, room_length)
            
            # Draw the objects
            for obj in self.objects:
                obj.draw()
            
            # Re-enable depth mask and backface culling
            glDepthMask(GL_TRUE)
            glEnable(GL_CULL_FACE)
            
            # Update the display
            pygame.display.flip()

    def close_game(self) -> None:
        '''
        Handles events that cause the game to close

        Parameters: None

        Returns: None
        '''
        pygame.quit()
        exit()

    def handle_keyboard_inp(self) -> None:
        '''
        Handles certain input from the keyboard -> WASD for movement

        Parameters: None

        Returns: None
        '''
        # Get the keys that are currently pressed
        keys = pygame.key.get_pressed()
        
        # Set the camera speed
        camera_speed = 0.005

        # Copy of the camera position for testing potential movement
        new_pos = list(self.camera_pos)

        # Calculate potential new position based on input
        if keys[pygame.K_w]:
            for i in range(3):
                new_pos[i] += self.camera_front[i] * camera_speed
        if keys[pygame.K_s]:
            for i in range(3):
                new_pos[i] -= self.camera_front[i] * camera_speed
        if keys[pygame.K_a] or keys[pygame.K_d]:
            # Calculate right vector
            cross_product = (
                self.camera_front[1] * self.camera_up[2] - self.camera_front[2] * self.camera_up[1],
                self.camera_front[2] * self.camera_up[0] - self.camera_front[0] * self.camera_up[2],
                self.camera_front[0] * self.camera_up[1] - self.camera_front[1] * self.camera_up[0]
            )

            # Normalize the right vector
            norm = math.sqrt(sum(i * i for i in cross_product))
            right = tuple(i / norm for i in cross_product)

            # Apply movement
            if keys[pygame.K_a]:
                for i in range(3):
                    new_pos[i] -= right[i] * camera_speed
            if keys[pygame.K_d]:
                for i in range(3):
                    new_pos[i] += right[i] * camera_speed

        # Check for collision with the new position before applying
        if not self.physics.check_collision(new_pos):
            self.camera_pos = tuple(new_pos)

    def handle_mouse_movement(self, xoffset: float, yoffset: float,
                              sensitivity: float = 0.05) -> None:
        '''
        Handles mouse movement, makes it look like you're looking around the
        room.

        Parameters:
            - xoffset: a float representing the offset in the x-direction
            - yoffset: a float representing the offset in the y-direction
            - sensitivity: a float representing the mouse sensitivity

        Returns: None
        '''
        # If this is the first mouse movement, set the last position to the 
        # current position
        if self.first_mouse:
            self.lastX, self.lastY = pygame.mouse.get_pos()
            self.first_mouse = False

        # Calculate the offset of the mouse position
        xoffset *= sensitivity
        yoffset *= sensitivity * -1

        # Update the last position
        self.yaw += xoffset
        self.pitch += yoffset

        # Constrain the pitch
        if self.pitch > 89.0:
            self.pitch = 89.0
        elif self.pitch < -89.0:
            self.pitch = -89.0

        # Update the camera front direction
        direction = (
            math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
            math.sin(math.radians(self.pitch)),
            math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        )

        # Normalize the direction
        norm = math.sqrt(sum(i * i for i in direction))
        self.camera_front = tuple(i / norm for i in direction)

    def draw_room(self, width: float, height: float, length: float) -> None:
        '''
        Draws a room on the screen

        Parameters:
        - width: float, the width of the room
        - height: float, the height of the room
        - length: float, the length of the room

        Returns: None
        '''

        # Clear the screen
        glLoadIdentity()

        # Set perspective
        gluPerspective(45, (self.window.width / self.window.height), 0.1, 100.0)

        # Set the camera position and direction
        eye = tuple(self.camera_pos[i] + self.camera_front[i] for i in range(3))
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
        
        
    def create_object(self) -> None:
        '''
        Opens a Tkinter dialog to create a new object with user-defined properties.

        Parameters: None

        Returns: None
        '''
        root = tk.Tk()
        root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

        # Simple dialog to get the shape type
        shape_type = simpledialog.askstring("Input", "Shape Type (Cube/Sphere/Pyramid):", parent=root)

        # Ask for size, color, and position
        size = simpledialog.askfloat("Input", "Size:", parent=root)
        color = simpledialog.askstring("Input", "Color (R,G,B):", parent=root)
        # Calculate the position in front of the camera
        position = (
            self.camera_pos[0] + self.camera_front[0] * (size + 1),
            self.camera_pos[1] + self.camera_front[1] * (size + 1),
            self.camera_pos[2] + self.camera_front[2] * (size + 1)
        )

        # Process color and position inputs
        color = tuple(map(float, color.split(',')))

        # Create the object based on the shape type
        if shape_type.lower() == 'cube':
            new_object = Cube(size, color, position)
        elif shape_type.lower() == 'sphere':
            new_object = Sphere(size, color, position)
        elif shape_type.lower() == 'pyramid':
            new_object = Pyramid(size, color, position)
        else:
            print("Unknown shape type.")
            return

        self.objects.append(new_object)
        print(f"New {shape_type} created!")

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
