# The Ultimate Pygame by Jacob Desha v0.8
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) #(Font type, font size)
# mouse_pos = pygame.mouse.get_pos()


sky_surf = pygame.image.load("img\sky1.png").convert()
ground_surf = pygame.image.load("img\ground.png").convert()

score_surf = test_font.render('My game', False, (64, 64, 64)) #(te)xt, AA, color)
score_rect = score_surf.get_rect(midbottom = (400, 50))
snail_surf = pygame.image.load("img\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (0, 375))
player_surf = pygame.image.load("img\player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 390))
while True: 
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')
# (300, 50)
    # Draw all our elements
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf, (-250, 0))
    pygame.draw.rect(screen, '#c0e8ec', score_rect,)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
    pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
    # pygame.draw.line(screen, 'Gold', (0,0), (800, 400), 10)
    screen.blit(score_surf, score_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(snail_surf, snail_rect)



    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800



    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # Update everything
    pygame.display.update()
    clock.tick(60)
