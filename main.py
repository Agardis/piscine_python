import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("brown")

    pygame.draw.circle(screen, "red", player_pos, player_radius)

    keys = pygame.key.get_pressed()
    player_speed = 300  # On peut ajuster la vitesse de notre perso

    if keys[pygame.K_z]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_q]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt

    # Permet de bloquer le joueur à la limite de la fenêtre
    player_pos.x = max(player_radius, min(player_pos.x, screen.get_width() - player_radius))
    player_pos.y = max(player_radius, min(player_pos.y, screen.get_height() - player_radius))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
