################################################################################
# File: physics.py
# Date: 13 February 2024
# Description:
#
# Class file for the physics engine
#
################################################################################

# imports
import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

class Physics():
    def __init__(self, room_size):
        '''
        Constructor for Physics class

        Parameters: None

        Returns: None
        '''
        self.room_size = room_size
        
    def check_collision(self, position, room_size):
        half_width, half_height, half_length = room_size[0] / 2, room_size[1] / 2, room_size[2] / 2
        
        if position[0] < -half_width or position[0] > half_width:
            return True
        if position[1] < -half_height or position[1] > half_height:
            return True
        if position[2] < -half_length or position[2] > half_length:
            return True
        return False



if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
