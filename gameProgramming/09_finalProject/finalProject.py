# Final Project, Jacob Desha, v0.0
import sys, random, pygame

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

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))


if difficulty == 1:
    pygame.display.set_caption('HITBOX\n Easy Mode')
else:
    pygame.display.set_caption('HITBOX\n Hard Mode')

screen = pygame.display.set_mode((x, y))
    




