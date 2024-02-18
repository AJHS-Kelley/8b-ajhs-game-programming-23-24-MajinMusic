# The Ultimate Pygame by Jacob Desha v0.9
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) #(Font type, font size)
game_active = True
# mouse_pos = pygame.mouse.get_pos()


sky_surf = pygame.image.load("img\sky1.png").convert()
ground_surf = pygame.image.load("img\ground.png").convert()

score_surf = test_font.render('My game', False, (64, 64, 64)) #(te)xt, AA, color)
score_rect = score_surf.get_rect(midbottom = (400, 50))
snail_surf = pygame.image.load("img\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (0, 375))
player_surf = pygame.image.load("img\player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 390))
player_gravity = 0

while True: 
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
        
            


# (300, 50)
    if game_active:
        # Draw all our elements
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf, (-250, 0))
        pygame.draw.rect(screen, '#c0e8ec', score_rect,)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
        pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
        # pygame.draw.line(screen, 'Gold', (0,0), (800, 400), 10)
        screen.blit(score_surf, score_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 380: player_rect.bottom = 380
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
        




    # Update everything
    pygame.display.update()
    clock.tick(60)
