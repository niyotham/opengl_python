# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


# Function to draw a circle (used for car wheels)
def draw_circle(cx, cy, r):
    glBegin(GL_TRIANGLE_FAN)     # Start drawing a filled circle
    glVertex2f(cx, cy)           # Center of the circle

    # Loop through angles from 0 to 360 degrees
    for i in range(0, 361):
        angle = i * math.pi / 180     # Convert degree to radians
        x = cx + r * math.cos(angle)  # Calculate x coordinate
        y = cy + r * math.sin(angle)  # Calculate y coordinate
        glVertex2f(x, y)              # Draw vertex of circle

    glEnd()  # Finish drawing


# Function that draws the car
def draw_car():

    # Set color for the car body (red)
    glColor3f(0.8, 0.1, 0.1)

    # Draw the main body of the car using a rectangle
    glBegin(GL_QUADS)
    glVertex2f(-0.6, -0.1)   # Bottom-left corner
    glVertex2f(0.6, -0.1)    # Bottom-right corner
    glVertex2f(0.6, 0.2)     # Top-right corner
    glVertex2f(-0.6, 0.2)    # Top-left corner
    glEnd()

    # Draw the roof of the car
    glBegin(GL_QUADS)
    glVertex2f(-0.3, 0.2)    # Bottom-left of roof
    glVertex2f(0.3, 0.2)     # Bottom-right of roof
    glVertex2f(0.2, 0.4)     # Top-right of roof
    glVertex2f(-0.2, 0.4)    # Top-left of roof
    glEnd()

    # Change color to black for wheels
    glColor3f(0, 0, 0)

    # Draw left wheel
    draw_circle(-0.35, -0.1, 0.12)

    # Draw right wheel
    draw_circle(0.35, -0.1, 0.12)


# Display function (called when window refreshes)
def display():

    glClear(GL_COLOR_BUFFER_BIT)   # Clear the screen
    glLoadIdentity()               # Reset transformations

    draw_car()                     # Call function to draw the car

    glFlush()                      # Render drawing to screen


# Initialization settings
def init():

    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-1, 1, -1, 1)  # Set 2D coordinate system


# Main function
def main():

    glutInit()   # Initialize GLUT

    # Set display mode (single buffer + RGB color)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set window size
    glutInitWindowSize(600, 600)

    # Set window position on screen
    glutInitWindowPosition(100, 100)

    # Create window with title
    glutCreateWindow(b"OpenGL Car in Python")

    init()                      # Call initialization
    glutDisplayFunc(display)   # Register display function
    glutMainLoop()             # Start OpenGL main loop


# Run the program
main()