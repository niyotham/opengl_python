# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation variable
angle = 0


# -------------------- INITIALIZATION --------------------
def init():
    # Background color (black)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Enable depth testing (3D)
    glEnable(GL_DEPTH_TEST)

    # Enable blending (required for transparency)
    glEnable(GL_BLEND)

    # Set blending function
    # This makes transparency work properly
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


# -------------------- DRAW OBJECTS --------------------
def draw_objects():
    
    # --------- OBJECT 1: RGB COLOR ---------
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)   # Pure RED (RGB mode)
    glVertex3f(-2, -1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(-1, 1, 0)
    glVertex3f(-2, 1, 0)
    glEnd()

    
    # --------- OBJECT 2: RGBA (TRANSPARENCY) ---------
    glBegin(GL_QUADS)
    glColor4f(0.0, 1.0, 0.0, 0.5)  # GREEN with 50% transparency
    glVertex3f(-0.5, -1, 0)
    glVertex3f(0.5, -1, 0)
    glVertex3f(0.5, 1, 0)
    glVertex3f(-0.5, 1, 0)
    glEnd()


    # --------- OBJECT 3: BYTE COLOR (0–255) ---------
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 255)  # BLUE using byte values
    glVertex3f(1, -1, 0)
    glVertex3f(2, -1, 0)
    glVertex3f(2, 1, 0)
    glVertex3f(1, 1, 0)
    glEnd()


# -------------------- DISPLAY FUNCTION --------------------
def display():
    global angle

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Camera setup
    gluLookAt(0, 0, 5,   # Camera position
              0, 0, 0,   # Looking at origin
              0, 1, 0)   # Up direction

    # Rotate scene slightly
    glRotatef(angle, 0, 1, 0)

    # Draw shapes
    draw_objects()

    # Swap buffers
    glutSwapBuffers()


# -------------------- ANIMATION --------------------
def update(value):
    global angle

    angle += 1  # Rotate slowly
    glutPostRedisplay()

    glutTimerFunc(16, update, 0)


# -------------------- WINDOW RESIZE --------------------
def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)

    glMatrixMode(GL_MODELVIEW)


# -------------------- MAIN FUNCTION --------------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Color Modes in OpenGL")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()


# Run program
if __name__ == "__main__":
    main()