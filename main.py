import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(current_time,False,64,64,64)
    score_rect = score_surf.get_rect(center = 400,50)
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font.ttf',50)
game_active = True

sky_surface = pygame.image.load('sky.png').convert_alpha()
ground_surface = pygame.image.load('ground.png').convert_alpha()

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # # pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
        # screen.blit(score_surf, score_rect)
        display_score()

        snail_rect.x -=4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)

        # Player
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('yellow')



    pygame.display.update()
    clock.tick(60)