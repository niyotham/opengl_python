import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    glBegin(GL_QUADS)
    # front (red)
    glColor3f(1,0,0)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    # back (green)
    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f( 1, 1,-1)
    glVertex3f( 1,-1,-1)
    # left (blue)
    glColor3f(0,0,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)
    # right (yellow)
    glColor3f(1,1,0)
    glVertex3f(1,-1,-1)
    glVertex3f(1, 1,-1)
    glVertex3f(1, 1, 1)
    glVertex3f(1,-1, 1)
    # top (magenta)
    glColor3f(1,0,1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,1, 1)
    glVertex3f( 1,1, 1)
    glVertex3f( 1,1,-1)
    # bottom (cyan)
    glColor3f(0,1,1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)
    glVertex3f( 1,-1, 1)
    glVertex3f(-1,-1, 1)
    glEnd()

def main():
    pygame.init()
    display = (800,600)

    # REQUEST 24-BIT DEPTH BUFFER
    pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5,0.7,1.0,1.0)

    # Camera initial position
    cam_x, cam_y, cam_z = 0,0,10

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Simple WASD movement
        keys = pygame.key.get_pressed()
        speed = 5*dt
        if keys[pygame.K_w]: cam_z -= speed
        if keys[pygame.K_s]: cam_z += speed
        if keys[pygame.K_a]: cam_x -= speed
        if keys[pygame.K_d]: cam_x += speed

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-cam_x, -cam_y, -cam_z)

        # Draw cubes at fixed positions
        positions = [(0,0,0),(3,0,-3),(-3,0,-3)]
        for pos in positions:
            glPushMatrix()
            glTranslatef(*pos)
            draw_cube()
            glPopMatrix()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()