# #  first_opengl.py
# import pygame
# from OpenGL.GL import *
# from OpenGL.GLUT import *

# # Initialize Pygame
# pygame.init()
# # Create a window (800x600 pixels)
# display = (800, 600)
# pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# # Main game loop
# while True:
#     # Handle events (like closing window)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
    
#     # Set background color to blue (R=0, G=0, B=0.5, A=1)
#     glClearColor(0.0, 0.0, 0.5, 1.0)
#     glClear(GL_COLOR_BUFFER_BIT)
    
#     # Update the display
#     pygame.display.flip()
#     pygame.time.wait(10)

# triangle.py
import pygame
from OpenGL.GL import *

def draw_triangle():
    # Start drawing triangles
    glBegin(GL_TRIANGLES)
    
    # First vertex (bottom-left) - Red
    glColor3f(1.0, 0.0, 0.0)  # RGB: Red
    glVertex2f(-0.5, -0.5)    # X, Y coordinates
    
    # Second vertex (bottom-right) - Green
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex2f(0.5, -0.5)     # X, Y
    
    # Third vertex (top-center) - Blue
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex2f(0.0, 0.5)      # X, Y
    
    glEnd()  # End drawing

# Main program
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle()  # Draw our triangle
    pygame.display.flip()