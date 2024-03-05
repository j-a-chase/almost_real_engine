################################################################################
# File: physics.py
# Date: 13 February 2024
# Description:
#
# Class file for the physics engine
#
################################################################################

# imports
from typing import Tuple

class Physics():
    def __init__(self, room_size: Tuple[int, int, int]) -> None:
        '''
        Constructor for Physics class

        Parameters:
            - room_size: A tuple of three integers indicating the room
                proportions

        Returns: None
        '''
        self.room_size = room_size
        
    def check_collision(self, position: Tuple[float, float, float]) -> bool:
        '''
        Checks for collision with the room walls, ceiling, and floor

        Parameters:
            - position: a tuple of three floats indicating the camera position

        Returns:
            - a boolean indicating whether or not the camera has run into a 
                wall, ceiling, or floor
        '''
        # calculate half values from room tuple
        half_width, half_height, half_length = self.room_size

        # bit shifting makes / or * by 2 more efficient
        half_width >>= 1
        half_height >>= 1
        half_length >>= 1

        # grab width, height, and length values from position tuple
        w, h, l = position
        
        # run collision test
        if (w < -half_width 
            or w > half_width
            or h < -half_height 
            or h > half_height
            or l < -half_length
            or l > half_length): return True
        return False

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
