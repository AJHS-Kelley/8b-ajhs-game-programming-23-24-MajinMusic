# Final Project, Jacob Desha, v0.2
import pygame
from sys import exit 
import random
import time 

start = pygame.USEREVENT + 1

x = 0
y = 0
yAxis = y
width = 100
height = 200
vel = 10
gravity = 0
moveSpeed = 0

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

# difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD.\n"))

# if difficulty == 1:
#     pygame.display.set_caption('HITBOX: Easy Mode')
# else:
#     pygame.display.set_caption('HITBOX: Hard Mode')

screen = pygame.display.set_mode((x, y))
test_background = pygame.image.load('img/background.png').convert()

#create player 
test_surface = pygame.image.load('img\square.png').convert()
test_SRect = test_surface.get_rect(midbottom = (100,200))
xAxis = test_SRect.x
yAxis = test_SRect.y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_d]:
        #     test_SRect.x += vel


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moveSpeed = 20
                moveSpeed += 1


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveSpeed = -20
                moveSpeed -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                moveSpeed = 0

        if keys[pygame.K_SPACE]: 
            gravity = -20

                     
    gravity += 1
    test_SRect.x += moveSpeed
    test_SRect.y += gravity
    print(test_SRect.bottom)
    print(moveSpeed)
    if test_SRect.bottom > 401: 
        test_SRect.bottom = 400
        screen.blit(test_surface, test_SRect)
    screen.blit(test_background, (0, 0))
    screen.blit(test_surface, test_SRect)

            
    pygame.display.update()
    clock.tick(60)

