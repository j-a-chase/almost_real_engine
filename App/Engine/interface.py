################################################################################
# File: interface.py
# Date: 13 February 2024
# Description:
#
# Class file for the user interface
#
################################################################################

# imports
import pygame
from pygame.locals import *

class UserInterface:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.window_size = (800, 600)  # Set window size
        self.screen = pygame.display.set_mode(self.window_size)  # Create Pygame window
        self.clock = pygame.time.Clock()  # Create clock for controlling frame rate
        self.font = pygame.font.Font(None, 36)  # Load font for rendering text

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check for quit event
                    running = False  # Exit the loop if the window is closed
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
                    # Check if the mouse click was inside the start button
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_inside_button(mouse_pos, self.start_button_pos, 200, 50):
                        print("Start button clicked!")
                        # Run your start button logic here
                    # Check if the mouse click was inside the quit button
                    elif self.is_inside_button(mouse_pos, self.quit_button_pos, 200, 50):
                        print("Quit button clicked!")
                        running = False  # Exit the loop if the quit button is clicked

            self.screen.fill((0, 0, 0))  # Fill the screen with black

            # Calculate button positions
            self.start_button_pos = (self.window_size[0] // 2, self.window_size[1] // 2 - 100)
            self.quit_button_pos = (self.window_size[0] // 2, self.window_size[1] // 2 + 100)

            # Render buttons
            self.render_button(self.start_button_pos, "START", (0, 255, 0))  # Green color for start button
            self.render_button(self.quit_button_pos, "QUIT", (255, 0, 0))   # Red color for quit button

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

    def render_button(self, position, text, color):
        x, y = position
        button_width = 200
        button_height = 50
        button_rect = pygame.Rect(x - button_width / 2, y - button_height / 2, button_width, button_height)
        pygame.draw.rect(self.screen, color, button_rect)  # Draw button rectangle

        text_surface = self.font.render(text, True, (255, 255, 255))  # Render button text
        text_rect = text_surface.get_rect(center=button_rect.center)  # Get text rectangle
        self.screen.blit(text_surface, text_rect)  # Blit text onto button rectangle

    def is_inside_button(self, mouse_pos, button_pos, button_width, button_height):
        x, y = button_pos
        # Check if the mouse position is inside the button rectangle
        return x - button_width / 2 <= mouse_pos[0] <= x + button_width / 2 and \
               y - button_height / 2 <= mouse_pos[1] <= y + button_height / 2

if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
