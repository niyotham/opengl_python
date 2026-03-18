import pygame

# Initialize and create a world surface larger than the display
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WORLD_WIDTH, WORLD_HEIGHT = 1600, 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
world_surf = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
# ... (Fill world_surf with background/objects)

# Camera state
camera_pos = pygame.Vector2(0, 0)
player = pygame.Rect(WORLD_WIDTH//2, WORLD_HEIGHT//2, 32, 32)
speed = 5

running = True
while running:
    # 1. Update (Player moves in World Space)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= speed
    # ... (other directions)
    
    # 2. Update Camera (Follow player, center-screen)
    camera_pos.x = player.centerx - SCREEN_WIDTH // 2
    camera_pos.y = player.centery - SCREEN_HEIGHT // 2
    # Clamp camera to boundaries
    camera_pos.x = max(0, min(camera_pos.x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_pos.y = max(0, min(camera_pos.y, WORLD_HEIGHT - SCREEN_HEIGHT))

    # 3. Draw (Offset everything by -camera_pos)
    screen.fill((0, 0, 0))
    screen.blit(world_surf, (-camera_pos.x, -camera_pos.y))
    # Draw player (player rect is in world space, sub camera_pos)
    pygame.draw.rect(screen, (0, 255, 0), player.move(-camera_pos.x, -camera_pos.y))
    pygame.display.flip()
