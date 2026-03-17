# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# from PIL import Image

# texture_id = None


# # -------------------- LOAD TEXTURE --------------------
# def load_texture():
#     global texture_id

#     image = Image.open("texture.jpg")
#     image = image.transpose(Image.FLIP_TOP_BOTTOM)
#     img_data = image.convert("RGB").tobytes()

#     texture_id = glGenTextures(1)
#     glBindTexture(GL_TEXTURE_2D, texture_id)

#     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
#     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
#                  image.width, image.height,
#                  0, GL_RGB, GL_UNSIGNED_BYTE, img_data)


# # -------------------- INITIALIZATION --------------------
# def init():
#     glEnable(GL_TEXTURE_2D)
#     load_texture()


# # -------------------- DRAW RECTANGLE --------------------
# def display():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glLoadIdentity()

#     glBindTexture(GL_TEXTURE_2D, texture_id)

#     glBegin(GL_QUADS)

#     # Bottom-left corner
#     glTexCoord2f(0, 0)
#     glVertex2f(-1, -1)

#     # Bottom-right
#     glTexCoord2f(1, 0)
#     glVertex2f(1, -1)

#     # Top-right
#     glTexCoord2f(1, 1)
#     glVertex2f(1, 1)

#     # Top-left
#     glTexCoord2f(0, 1)
#     glVertex2f(-1, 1)

#     glEnd()

#     glutSwapBuffers()


# # -------------------- MAIN --------------------
# def main():
#     glutInit()
#     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
#     glutInitWindowSize(600, 600)
#     glutCreateWindow(b"Texture Coordinates")

#     init()
#     glutDisplayFunc(display)

#     glutMainLoop()


# if __name__ == "__main__":
#     main()

# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Import image library (for loading textures)
from PIL import Image

# Rotation angle
angle = 0

# Texture ID
texture_id = None


# -------------------- LOAD TEXTURE --------------------
def load_texture():
    global texture_id

    # Load image using Pillow
    image = Image.open("rachel_image.jpg")  # Make sure this file exists
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    # Convert image to bytes
    img_data = image.convert("RGB").tobytes()

    # Generate texture ID
    texture_id = glGenTextures(1)

    # Bind texture
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Create texture
    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 GL_RGB,
                 image.width,
                 image.height,
                 0,
                 GL_RGB,
                 GL_UNSIGNED_BYTE,
                 img_data)


# -------------------- INITIALIZATION --------------------
def init():
    glEnable(GL_DEPTH_TEST)

    # Enable textures
    glEnable(GL_TEXTURE_2D)

    # Load texture
    load_texture()


# -------------------- DRAW TEXTURED CUBE --------------------
def draw_cube():
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)

    # -------- FRONT FACE --------
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)

    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)

    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)

    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)

    # -------- BACK FACE --------
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)

    glTexCoord2f(1, 0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(1, 1)
    glVertex3f(1, 1, -1)

    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, -1)

    # (Other faces can be added similarly)

    glEnd()


# -------------------- DISPLAY --------------------
def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera
    gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)

    # Rotate cube
    glRotatef(angle, 1, 1, 0)

    draw_cube()

    glutSwapBuffers()


# -------------------- ANIMATION --------------------
def update(value):
    global angle
    angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


# -------------------- RESHAPE --------------------
def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)

    glMatrixMode(GL_MODELVIEW)


# -------------------- MAIN --------------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Texture Mapping in OpenGL")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()