from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

# Base Shape class
class Shape:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        # Set color and position
        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(*self.position)
        self.draw_shape()
        glPopMatrix()

    def draw_shape(self):
        # Placeholder for shape-specific drawing logic
        pass

# Sphere class
class Sphere(Shape):
    def __init__(self, radius, color=(1.0, 1.0, 1.0), position=(0.0, 0.0, 0.0)):
        super().__init__(color, position)
        self.radius = radius

    def draw_shape(self):
        # Use GLU quadric to draw the sphere
        quad = gluNewQuadric()
        gluSphere(quad, self.radius, 32, 32)

        # pygame.display.flip()

# Cube class
class Cube(Shape):
    def __init__(self, side_length, color=(1.0, 1.0, 1.0), position=(0.0, 0.0, 0.0)):
        super().__init__(color, position)
        self.side_length = side_length

    def draw_shape(self):
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

        # pygame.display.flip()

# Pyramid class (keeping the immediate mode for educational purposes)
class Pyramid(Shape):
    def __init__(self, base=1.0, height=1.5, color=(1.0, 1.0, 1.0), position=(0.0, 0.0, 0.0)):
        super().__init__(color, position)
        self.base = base
        self.height = height

    def draw_shape(self):
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

        # pygame.display.flip()
