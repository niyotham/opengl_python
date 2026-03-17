# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation angle for animation
angle = 0


# -------------------- INITIALIZATION --------------------
def init():
    # Set background color (black)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Enable depth testing (important for 3D)
    glEnable(GL_DEPTH_TEST)


# -------------------- DRAW COLORED CUBE --------------------
def draw_cube():
    # Start drawing quadrilaterals (cube faces)
    glBegin(GL_QUADS)

    # -------- FRONT FACE (RED) --------
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # -------- BACK FACE (GREEN) --------
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    # -------- LEFT FACE (BLUE) --------
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # -------- RIGHT FACE (YELLOW) --------
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    # -------- TOP FACE (CYAN) --------
    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # -------- BOTTOM FACE (MAGENTA) --------
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # End drawing
    glEnd()


# -------------------- DISPLAY FUNCTION --------------------
def display():
    global angle

    # Clear screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Set camera (position, look-at, up direction)
    gluLookAt(3, 3, 5,   # Camera position
              0, 0, 0,   # Looking at center
              0, 1, 0)   # Up direction

    # Rotate cube
    glRotatef(angle, 1, 1, 0)

    # Draw the colored cube
    draw_cube()

    # Swap buffers (smooth animation)
    glutSwapBuffers()


# -------------------- ANIMATION --------------------
def update(value):
    global angle

    # Increase rotation angle
    angle += 1

    # Redraw screen
    glutPostRedisplay()

    # Repeat every 16 ms (~60 FPS)
    glutTimerFunc(16, update, 0)


# -------------------- WINDOW RESIZE --------------------
def reshape(w, h):
    # Prevent division by zero
    if h == 0:
        h = 1

    # Set viewport
    glViewport(0, 0, w, h)

    # Projection setup
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)

    # Back to model view
    glMatrixMode(GL_MODELVIEW)


# -------------------- MAIN FUNCTION --------------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Adding Colors to 3D Objects")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()


# Run program
if __name__ == "__main__":
    main()