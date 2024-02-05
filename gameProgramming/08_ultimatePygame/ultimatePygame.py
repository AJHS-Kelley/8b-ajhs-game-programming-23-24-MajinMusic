# The Ultimate Pygame by Jacob Desha v0.5
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) #(Font type, font size)


sky_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\sky1.png").convert()
ground_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\ground.png").convert()
text_surface = test_font.render('My game', False, 'Blue') #(text, AA, color)

snail_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (0, 375))

player_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\player.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 390))
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all our elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (-250, 0))
    screen.blit(text_surface, (300, 50))
    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800

    if player_rect.colliderect(snail_rect):
        print('collision')

    # Update everything
    pygame.display.update()
    clock.tick(60)
