# The Ultimate Pygame by Jacob Desha v0.0

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all our elements
    # Update everything
    pygame.display.update()