import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font.ttf',50)

sky_surface = pygame.image.load('sky.png').convert_alpha()
ground_surface = pygame.image.load('ground.png').convert_alpha()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos):
                #print('collision')
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
    screen.blit(score_surf, score_rect)


    snail_rect.x -=4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    keys = pygame.key.get_pressed()
    keys[pygame.K_SPACE]

    #if player_rect.colliderect(snail_rect):
        #print('collision')

    pygame.display.update()
    clock.tick(60)