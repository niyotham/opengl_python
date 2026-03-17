from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

angle = 90  # Rotation angle around Y axis


def draw_axes():
    """Draw 3D coordinate axes in red"""
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


def draw_cube():
    """Draw wireframe cube"""
    glColor3f(1.0, 1.0, 1.0)
    glutWireCube(1.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Move camera backward
    glTranslatef(0.0, 0.0, -6)

    # Draw axes (no rotation)
    draw_axes()

    # Move cube away from origin
    glTranslatef(2.0, 1.0, 0.0)

    # Rotate cube around Y axis (like glm::rotate(..., vec3(0,1,0)))
    glRotatef(angle, 0, 1, 0)

    draw_cube()

    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.45, 0.58, 0.72, 1.0)  # Background similar to image


# --------- Main ---------
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"OpenGL Renderer")

init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()