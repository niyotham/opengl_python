# 3d_cube.py
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    # Define cube vertices (8 corners)
    vertices = [
        [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],  # Back face
        [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]   # Front face
    ]
    
    # Define edges (connections between vertices)
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Back face
        [4, 5], [5, 6], [6, 7], [7, 4],  # Front face
        [0, 4], [1, 5], [2, 6], [3, 7]   # Connecting edges
    ]
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Setup 3D perspective
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Set up 3D perspective view
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # Move camera back

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 3, 1, 1)  # Rotate cube slightly
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(10)