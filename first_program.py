# first_opengl.py
import pygame
from OpenGL.GL import (glClear,
    GL_COLOR_BUFFER_BIT,glClearColor)
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()
# Create a window (800x600 pixels)
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Main game loop
while True:
    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Set background color to blue (R=0, G=0, B=0.5, A=1)
    glClearColor(0.0, 0.0, 0.5, 0.1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)