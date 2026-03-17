# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# # Rotation angle
# angle = 0

# def init():
#     # Enable depth testing
#     glEnable(GL_DEPTH_TEST)

#     # Enable lighting
#     glEnable(GL_LIGHTING)
#     glEnable(GL_LIGHT0)

#     # Set light position (x, y, z, w)
#     light_position = [1.0, 1.0, 1.0, 1.0]
#     glLightfv(GL_LIGHT0, GL_POSITION, light_position)

#     # Set light color (white)
#     light_color = [1.0, 1.0, 1.0, 1.0]
#     glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)

#     # Enable color tracking
#     glEnable(GL_COLOR_MATERIAL)
#     glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

# def draw_cube():
#     glBegin(GL_QUADS)

#     # Front face
#     glNormal3f(0, 0, 1)
#     glVertex3f(-1, -1, 1)
#     glVertex3f(1, -1, 1)
#     glVertex3f(1, 1, 1)
#     glVertex3f(-1, 1, 1)

#     # Back face
#     glNormal3f(0, 0, -1)
#     glVertex3f(-1, -1, -1)
#     glVertex3f(-1, 1, -1)
#     glVertex3f(1, 1, -1)
#     glVertex3f(1, -1, -1)

#     # Left face
#     glNormal3f(-1, 0, 0)
#     glVertex3f(-1, -1, -1)
#     glVertex3f(-1, -1, 1)
#     glVertex3f(-1, 1, 1)
#     glVertex3f(-1, 1, -1)

#     # Right face
#     glNormal3f(1, 0, 0)
#     glVertex3f(1, -1, -1)
#     glVertex3f(1, 1, -1)
#     glVertex3f(1, 1, 1)
#     glVertex3f(1, -1, 1)

#     # Top face
#     glNormal3f(0, 1, 0)
#     glVertex3f(-1, 1, -1)
#     glVertex3f(-1, 1, 1)
#     glVertex3f(1, 1, 1)
#     glVertex3f(1, 1, -1)

#     # Bottom face
#     glNormal3f(0, -1, 0)
#     glVertex3f(-1, -1, -1)
#     glVertex3f(1, -1, -1)
#     glVertex3f(1, -1, 1)
#     glVertex3f(-1, -1, 1)

#     glEnd()

# def display():
#     global angle
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#     glLoadIdentity()
#     gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)

#     glRotatef(angle, 1, 1, 0)

#     glColor3f(0.2, 0.7, 1.0)  # Object color
#     draw_cube()

#     glutSwapBuffers()

# def update(value):
#     global angle
#     angle += 1
#     glutPostRedisplay()
#     glutTimerFunc(16, update, 0)

# def reshape(w, h):
#     glViewport(0, 0, w, h)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(45, w / h, 1, 50)
#     glMatrixMode(GL_MODELVIEW)

# def main():
#     glutInit()
#     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
#     glutInitWindowSize(800, 600)
#     glutCreateWindow(b"Basic Lighting in OpenGL (Python)")

#     init()

#     glutDisplayFunc(display)
#     glutReshapeFunc(reshape)
#     glutTimerFunc(0, update, 0)

#     glutMainLoop()

# if __name__ == "__main__":
#     main()

# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# This variable will control cube rotation
angle = 0


# -------------------- INITIALIZATION --------------------
def init():
    # Enable depth testing (important for 3D so objects overlap correctly)
    glEnable(GL_DEPTH_TEST)

    # Enable lighting in OpenGL
    glEnable(GL_LIGHTING)

    # Enable light source 0 (OpenGL supports multiple lights)
    glEnable(GL_LIGHT0)

    # Set the position of the light (x, y, z, w)
    # w = 1 means it's a positional light (like a bulb)
    light_position = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Set the color of the light (white light)
    light_color = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)

    # Allow object color (glColor) to affect lighting
    glEnable(GL_COLOR_MATERIAL)

    # Apply color to front faces using ambient and diffuse lighting
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


# -------------------- DRAWING THE CUBE --------------------
def draw_cube():
    # Start drawing quadrilateral faces (4-sided polygons)
    glBegin(GL_QUADS)

    # -------- FRONT FACE --------
    # Normal vector (points outward, used for lighting)
    glNormal3f(0, 0, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # -------- BACK FACE --------
    glNormal3f(0, 0, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    # -------- LEFT FACE --------
    glNormal3f(-1, 0, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # -------- RIGHT FACE --------
    glNormal3f(1, 0, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    # -------- TOP FACE --------
    glNormal3f(0, 1, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # -------- BOTTOM FACE --------
    glNormal3f(0, -1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # End drawing
    glEnd()


# -------------------- DISPLAY FUNCTION --------------------
def display():
    global angle

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Set camera position
    # eye(x,y,z), look at point, up direction
    gluLookAt(3, 3, 5,   # Camera position
              0, 0, 0,   # Looking at origin
              0, 1, 0)   # Up direction

    # Rotate the cube continuously
    glRotatef(angle, 1, 1, 0)

    # Set object color (blue-ish)
    glColor3f(0.2, 0.7, 1.0)

    # Draw the cube
    draw_cube()

    # Swap buffers (for smooth animation)
    glutSwapBuffers()


# -------------------- ANIMATION --------------------
def update(value):
    global angle

    # Increase rotation angle
    angle += 1

    # Tell OpenGL to redraw the screen
    glutPostRedisplay()

    # Call this function again after 16ms (~60 FPS)
    glutTimerFunc(16, update, 0)


# -------------------- WINDOW RESIZE --------------------
def reshape(w, h):
    # Set viewport to match window size
    glViewport(0, 0, w, h)

    # Switch to projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set perspective (3D view)
    gluPerspective(45, w / h, 1, 50)

    # Switch back to model view
    glMatrixMode(GL_MODELVIEW)


# -------------------- MAIN FUNCTION --------------------
def main():
    # Initialize GLUT
    glutInit()

    # Set display mode (double buffer + RGB + depth)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Set window size
    glutInitWindowSize(800, 600)

    # Create window with title
    glutCreateWindow(b"Basic Lighting in OpenGL (Python)")

    # Call initialization
    init()

    # Register display function
    glutDisplayFunc(display)

    # Register reshape function
    glutReshapeFunc(reshape)

    # Start animation loop
    glutTimerFunc(0, update, 0)

    # Start main loop
    glutMainLoop()


# Run the program
if __name__ == "__main__":
    main()