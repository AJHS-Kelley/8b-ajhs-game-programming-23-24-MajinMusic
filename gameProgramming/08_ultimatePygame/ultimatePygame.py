# The Ultimate Pygame by Jacob Desha v0.3

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

sky_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\sky.jpg")
ground_surface = pygame.image.load("C:\8b-ajhs-game-programming-23-24-MajinMusic\img\ground.jpg")


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all our elements
    screen.blit(sky_surface,(100,0))
    screen.blit(ground_surface, (0,300))
    # Update everything
    pygame.display.update()
    clock.tick(60)
