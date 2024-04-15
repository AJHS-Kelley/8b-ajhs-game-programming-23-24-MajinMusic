# Final Project, Jacob Desha, v0.1.2
import pygame
from sys import exit 
import random
xAxis = 100
yAxis = 200
width = 100
height = 200
vel = 10

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
mainFont = pygame.font.Font(None, 50) 
gameActive = True
health = 0
cpuHealth = 0
damage = 0
cpudamage = 0
moveSpeed = 1

# difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

# if difficulty == 1:
#     pygame.display.set_caption('HITBOX: Easy Mode')
# else:
#     pygame.display.set_caption('HITBOX: Hard Mode')

screen = pygame.display.set_mode((x, y))
test_surface = pygame.image.load('img/player.png').convert_alpha()
test_SRect = test_surface.get_rect(midtop = (100,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
        
                


                
                    
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveSpeed += 10

                

    if gameActive:
        screen.blit(test_surface, test_SRect)
    print(test_SRect.x)

    moveSpeed += 10
    test_SRect.x += moveSpeed
            
    pygame.display.update()
    clock.tick(60)

if gameActive:
        screen.blit(test_surface, test_SRect)