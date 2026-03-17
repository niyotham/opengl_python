# transformations_demo.py

# -------------------- IMPORT LIBRARIES --------------------
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# -------------------- DRAW SIMPLE CUBE FUNCTION --------------------
def draw_simple_cube(size):
    """
    Draw a simple cube centered at origin with given size.
    """
    s = size / 2  # Half-size for easier calculations

    # Cube vertices
    vertices = [
        [s, s, s], [s, -s, s], [-s, -s, s], [-s, s, s],   # Front face
        [s, s, -s], [s, -s, -s], [-s, -s, -s], [-s, s, -s]  # Back face
    ]

    # Cube faces (indices into vertices)
    faces = [
        [0,1,2,3],  # Front
        [4,5,6,7],  # Back
        [0,4,5,1],  # Right
        [3,7,6,2],  # Left
        [0,3,7,4],  # Top
        [1,5,6,2]   # Bottom
    ]

    # Colors for faces (RGB)
    colors = [
        [1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1]
    ]

    # Draw each face
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i % len(colors)])  # Assign color
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# -------------------- DRAW TRANSFORMED CUBES --------------------
def draw_transformed_cube():
    """
    Demonstrate Translation, Rotation, and Scaling transformations
    """
    glPushMatrix()  # Save current transformation state

    # -------- 1. TRANSLATION --------
    glTranslatef(2.0, 0.0, 0.0)  # Move cube 2 units to the right
    draw_simple_cube(0.5)        # Draw small cube

    # -------- 2. ROTATION --------
    glTranslatef(-4.0, 0.0, 0.0)  # Move 4 units left
    glRotatef(45, 0, 1, 0)        # Rotate 45° around Y-axis
    draw_simple_cube(0.5)

    # -------- 3. SCALING --------
    glTranslatef(0.0, 2.0, 0.0)   # Move cube up
    glScalef(1.5, 1.5, 1.5)       # Scale cube 1.5x
    draw_simple_cube(0.5)

    glPopMatrix()  # Restore original transformation state

# -------------------- MAIN PROGRAM --------------------
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Transformation Demo")

    # Set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move camera back
    glTranslatef(0.0, 0.0, -10)

    # Enable depth testing
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    running = True
    angle = 0  # Rotation angle for animation

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Optional: Rotate the entire scene for better view
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)
        draw_transformed_cube()
        glPopMatrix()

        # Update display
        pygame.display.flip()
        clock.tick(60)
        angle += 1  # Increment rotation angle

    pygame.quit()

# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()