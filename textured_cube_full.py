# textured_cube_full.py

# -------------------- IMPORT LIBRARIES --------------------
import pygame                 # For window creation and event handling
from pygame.locals import *   # Constants like DOUBLEBUF, OPENGL
from OpenGL.GL import *       # OpenGL functions
from OpenGL.GLU import *      # Utility library (gluPerspective)
from PIL import Image         # To load images as textures

# -------------------- LOAD TEXTURE FUNCTION --------------------
def load_texture(filename):
    """
    Load an image file as an OpenGL texture and return its ID.
    """
    # Load image using PIL
    image = Image.open(filename)

    # Flip image vertically for OpenGL
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    # Convert image to RGBA format
    image_data = image.convert("RGBA").tobytes()

    # Generate texture ID
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Load texture into OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 image.width, image.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id

# -------------------- DRAW COMPLETE TEXTURED CUBE --------------------
def draw_complete_textured_cube(texture_ids):
    """
    Draw a cube with 6 faces, each mapped with a texture.
    """
    faces = [
        # FRONT
        {"vertices": [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1]], "tex": [(1,1),(1,0),(0,0),(0,1)]},
        # RIGHT
        {"vertices": [[1,1,-1],[1,-1,-1],[1,-1,1],[1,1,1]], "tex": [(1,1),(1,0),(0,0),(0,1)]},
        # BACK
        {"vertices": [[-1,1,-1],[-1,-1,-1],[1,-1,-1],[1,1,-1]], "tex": [(1,1),(1,0),(0,0),(0,1)]},
        # LEFT
        {"vertices": [[-1,1,1],[-1,-1,1],[-1,-1,-1],[-1,1,-1]], "tex": [(1,1),(1,0),(0,0),(0,1)]},
        # TOP
        {"vertices": [[1,1,-1],[1,1,1],[-1,1,1],[-1,1,-1]], "tex": [(1,1),(1,0),(0,0),(0,1)]},
        # BOTTOM
        {"vertices": [[1,-1,1],[1,-1,-1],[-1,-1,-1],[-1,-1,1]], "tex": [(1,1),(1,0),(0,0),(0,1)]}
    ]

    glEnable(GL_TEXTURE_2D)
    for i, face in enumerate(faces):
        # Bind texture for this face (reuse if fewer textures)
        glBindTexture(GL_TEXTURE_2D, texture_ids[i % len(texture_ids)])

        glBegin(GL_QUADS)
        for j in range(4):
            glTexCoord2fv(face["tex"][j])   # Set texture coordinates
            glVertex3fv(face["vertices"][j]) # Set vertex positions
        glEnd()
    glDisable(GL_TEXTURE_2D)

# -------------------- MAIN PROGRAM --------------------
def main():
    pygame.init()
    display = (800, 600)

    # Create OpenGL window
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rotating Textured Cube")

    # Set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move camera back
    glTranslatef(0.0, 0.0, -7)

    # Enable depth testing
    glEnable(GL_DEPTH_TEST)

    # Load textures (make sure these files exist in the same folder)
    texture_files = [
        "front.jpg",
        "right.jpg",
        "back.jpg",
        "left.jpg",
        "top.jpg",
        "bottom.jpg"
    ]
    texture_ids = [load_texture(f) for f in texture_files] # Load all textures using list comprehension

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Rotate cube slowly
        glRotatef(1, 1, 1, 0)

        # Draw the textured cube
        draw_complete_textured_cube(texture_ids)

        # Swap buffers
        pygame.display.flip()
        clock.tick(60)  # Limit FPS to 60

    pygame.quit()

# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()