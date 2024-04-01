# Final Project, Jacob Desha, v0.1
import pygame
from sys import exit 
import random

resolution = 0 # = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)
x = 0
y = 0

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()
pygame.display.set_caption('game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50) 

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

if difficulty == 1:
    pygame.display.set_caption('HITBOX: Easy Mode')
else:
    pygame.display.set_caption('HITBOX: Hard Mode')

screen = pygame.display.set_mode((x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


