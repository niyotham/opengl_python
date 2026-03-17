# textured_cube_complete.py

# -------------------- IMPORT LIBRARIES --------------------
import pygame                 # For window and event handling
from pygame.locals import *   # For constants like DOUBLEBUF, OPENGL
from OpenGL.GL import *       # OpenGL functions
from OpenGL.GLU import *      # OpenGL Utility Library (gluPerspective, etc.)
from PIL import Image         # For loading image files as textures

# -------------------- FUNCTION TO DRAW COMPLETE TEXTURED CUBE --------------------
def draw_complete_textured_cube(texture_ids):
    """
    Draw a full cube where each face can have a different texture.
    
    Parameters:
        texture_ids (list): List of OpenGL texture IDs.
    """
    
    # Define vertices and texture coordinates for all 6 cube faces
    faces = [
        # FRONT
        {"vertices": [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]},

        # RIGHT
        {"vertices": [[1,1,-1],[1,-1,-1],[1,-1,1],[1,1,1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]},

        # BACK
        {"vertices": [[-1,1,-1],[-1,-1,-1],[1,-1,-1],[1,1,-1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]},

        # LEFT
        {"vertices": [[-1,1,1],[-1,-1,1],[-1,-1,-1],[-1,1,-1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]},

        # TOP
        {"vertices": [[1,1,-1],[1,1,1],[-1,1,1],[-1,1,-1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]},

        # BOTTOM
        {"vertices": [[1,-1,1],[1,-1,-1],[-1,-1,-1],[-1,-1,1]],
         "tex": [(1,1),(1,0),(0,0),(0,1)]}
    ]

    # Enable texture mapping
    glEnable(GL_TEXTURE_2D)

    # Draw each face
    for i, face in enumerate(faces):
        # Select a texture for this face
        # If fewer textures provided, repeat using modulo operator
        glBindTexture(GL_TEXTURE_2D, texture_ids[i % len(texture_ids)])

        # Draw the face
        glBegin(GL_QUADS)
        for j in range(4):
            glTexCoord2fv(face["tex"][j])   # Set texture coordinate
            glVertex3fv(face["vertices"][j]) # Set vertex position
        glEnd()

    # Disable texture mapping after drawing
    glDisable(GL_TEXTURE_2D)