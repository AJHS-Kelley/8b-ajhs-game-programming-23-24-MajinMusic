# The Ultimate Pygame by Jacob Desha v0.4

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) #(Font type, font size)


sky_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\sky.jpg")
ground_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\ground.jpg")
text_surface = test_font.render('My game', False, 'Blue') #(text, AA, color)

snail_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\download.png")
snail_x_pos = 600

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all our elements
    screen.blit(sky_surface,(100,0))
    screen.blit(ground_surface, (50,300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 200))
    # Update everything
    pygame.display.update()
    clock.tick(60)
