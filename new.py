# Bresenham's Line Drawing using OpenGL in Python

# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width = 500
height = 500


# Function to draw a pixel
def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


# Bresenham's Line Algorithm
def bresenham_line(x1, y1, x2, y2):

    dx = abs(x2 - x1)   # change in x
    dy = abs(y2 - y1)   # change in y

    sx = 1 if x1 < x2 else -1   # step direction in x
    sy = 1 if y1 < y2 else -1   # step direction in y

    err = dx - dy   # error value

    while True:
        draw_pixel(x1, y1)   # draw current pixel

        # stop when end point reached
        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err = err - dy
            x1 = x1 + sx

        if e2 < dx:
            err = err + dx
            y1 = y1 + sy


# Display function
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # draw line in red

    # Draw line from (100,100) to (400,300)
    bresenham_line(100, 100, 400, 300)

    glFlush()


# Initialization
def init():

    glClearColor(1.0, 1.0, 1.0, 1.0)  # white background
    glColor3f(0.0, 0.0, 0.0)          # default color
    glPointSize(3.0)                  # pixel size

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set coordinate system
    gluOrtho2D(0, width, 0, height)


# Main function
def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Bresenham Line Drawing")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


# Run the program
main()