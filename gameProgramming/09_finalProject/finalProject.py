# Final Project, Jacob Desha, v0.1
import pygame
from sys import exit 
import random
x = 0
y = 0
xAxis = x
yAxis = y
width = 100
height = 200
vel = 10

resolution = 0 # = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)



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
test_background = pygame.image.load('img/sky1.png').convert_alpha()

#create player
test_surface = pygame.image.load('img\square.png').convert_alpha()
test_SRect = test_surface.get_rect(midtop = (100,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
        
                


                
                    
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                test_SRect.x += vel

                

    screen.blit(test_background, (100, 200))
    screen.blit(test_surface, test_SRect)
    print(test_SRect.x)
            
    pygame.display.update()
    clock.tick(60)

