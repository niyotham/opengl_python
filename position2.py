# Import OpenGL core functions
from OpenGL.GL import *

# Import GLUT for windowing and keyboard handling
from OpenGL.GLUT import *

# Import GLU for perspective projection
from OpenGL.GLU import *

import sys

# -----------------------------
# Global variables
# -----------------------------

angle = 90  # Rotation angle (Y-axis)

# Cube initial position (away from origin)
cube_x = 2.0
cube_y = 1.0
cube_z = 0.0


# -----------------------------
# Draw 3D Axes
# -----------------------------
def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)

    # X-axis
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)

    # Y-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)

    # Z-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 2)

    glEnd()


# -----------------------------
# Draw Wireframe Cube
# -----------------------------
def draw_cube():
    glColor3f(1.0, 1.0, 1.0)
    glutWireCube(1.0)


# -----------------------------
# Display Function
# -----------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Move camera backward
    glTranslatef(0.0, 0.0, -6)

    # Draw axes
    draw_axes()

    # Move cube using position variables
    glTranslatef(cube_x, cube_y, cube_z)

    # Rotate cube around Y-axis
    glRotatef(angle, 0, 1, 0)

    draw_cube()

    glutSwapBuffers()


# -----------------------------
# Keyboard Control
# -----------------------------
def keyboard(key, x, y):
    global cube_x, cube_y, cube_z

    # Press 'r' to reset cube to origin (0,0,0)
    if key == b'r':
        cube_x = 0.0
        cube_y = 0.0
        cube_z = 0.0

    glutPostRedisplay()


# -----------------------------
# Window Resize Function
# -----------------------------
def reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, w / h, 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)


# -----------------------------
# Initialization
# -----------------------------
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.45, 0.58, 0.72, 1.0)


# -----------------------------
# Main Program
# -----------------------------
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"OpenGL Renderer")

init()

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)

glutMainLoop()