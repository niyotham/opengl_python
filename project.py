import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, radians
class FirstPersonCamera:
    def __init__(self):
        self.pos = [0, 0, 0]
        self.rot = [0, 0]  # [pitch, yaw]
        self.speed = 0.1
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Movement
        if keys[pygame.K_w]:  # Forward
            self.pos[0] += sin(radians(self.rot[1])) * self.speed
            self.pos[2] -= cos(radians(self.rot[1])) * self.speed
        if keys[pygame.K_s]:  # Backward
            self.pos[0] -= sin(radians(self.rot[1])) * self.speed
            self.pos[2] += cos(radians(self.rot[1])) * self.speed
        if keys[pygame.K_a]:  # Left
            self.pos[0] -= cos(radians(self.rot[1])) * self.speed
            self.pos[2] -= sin(radians(self.rot[1])) * self.speed
        if keys[pygame.K_d]:  # Right
            self.pos[0] += cos(radians(self.rot[1])) * self.speed
            self.pos[2] += sin(radians(self.rot[1])) * self.speed
    
    def apply(self):
        # Apply camera transformations
        glRotatef(-self.rot[0], 1, 0, 0)  # Look up/down
        glRotatef(-self.rot[1], 0, 1, 0)  # Look left/right
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])