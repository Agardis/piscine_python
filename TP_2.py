import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# L'image de fond
background_image = pygame.image.load("D:\\Pictures\\Fond_0.jpg")
background_rect = background_image.get_rect()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

object_image = pygame.image.load("D:\\Pictures\\H59313961ea744338abc840b766af6366k.jpg_640x640Q90.jpg_.png")
object_rect = object_image.get_rect()
object_rect.center = (400, 300)  # Position de l'apparition du joueur

# L'image des murs
obstacle1_image = pygame.image.load("D:\\Pictures\\H59313961ea744338abc840b766af6366k.jpg_640x640Q90.jpg_.png")
obstacle1_rect = obstacle1_image.get_rect(topleft=(600, 200), bottomright=(680, 320))

obstacle2_image = pygame.image.load("D:\\Pictures\\H59313961ea744338abc840b766af6366k.jpg_640x640Q90.jpg_.png")
obstacle2_rect = obstacle2_image.get_rect(topleft=(200, 500), bottomright=(320, 580))

obstacle3_image = pygame.image.load("D:\\Pictures\\H59313961ea744338abc840b766af6366k.jpg_640x640Q90.jpg_.png")
obstacle3_rect = obstacle3_image.get_rect(topleft=(100, 400), bottomright=(200, 450))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_rect)  # L'image de fond

    # L'image des murs
    screen.blit(object_image, object_rect)
    screen.blit(obstacle1_image, obstacle1_rect.topleft)
    screen.blit(obstacle2_image, obstacle2_rect.topleft)
    screen.blit(obstacle3_image, obstacle3_rect.topleft)

    pygame.draw.circle(screen, "red", (int(player_pos.x), int(player_pos.y)), player_radius)

    keys = pygame.key.get_pressed()
    player_speed = 300  # Vitesse du joueur

    # Rollback du joueur
    old_player_pos = player_pos.copy()

    if keys[pygame.K_z]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_q]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt

    # Délimitation des collisions
    player_pos.x = max(player_radius, min(player_pos.x, screen.get_width() - player_radius))
    player_pos.y = max(player_radius, min(player_pos.y, screen.get_height() - player_radius))

    # Délimitation de la map
    player_rect = pygame.Rect(player_pos.x - player_radius, player_pos.y - player_radius, player_radius * 2, player_radius * 2)

    # Collision entre le joueur et les murs
    if object_rect.colliderect(player_rect) or obstacle1_rect.colliderect(player_rect) or obstacle2_rect.colliderect(player_rect) or obstacle3_rect.colliderect(player_rect):
        # Roll back player position to the previous position to avoid collision
        player_pos = old_player_pos

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
