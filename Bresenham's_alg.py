# Import required OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH = 500
HEIGHT = 500


# Function to draw a single pixel
def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


# Bresenham Line Drawing Algorithm
def bresenham_line(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        draw_pixel(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy


# Display callback function
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red line
    bresenham_line(100, 100, 400, 300)

    glFlush()


# Initialization function
def init():

    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glPointSize(3.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)


# Main function
def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Bresenham Line - Python OpenGL")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()