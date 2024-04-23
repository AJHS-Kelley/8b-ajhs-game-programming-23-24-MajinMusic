# Final Project, Jacob Desha, v0.2.1
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
player1_gravity = 0
player1_Speed = 0
player2_Speed = 0
player2_gravity = 0

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

test_health = pygame.Surface((350, 25))
test_health.fill('White')
test_HRect = test_health.get_rect(midbottom = (190, 50))

test_Hfilling = pygame.Surface((340, 15))
test_Hfilling.fill('Red')
test_filling = test_Hfilling.get_rect(midbottom = (190, 45))

test_health2 = pygame.Surface((350, 25))
test_health2.fill('White')
test_HRect2 = test_health.get_rect(midbottom = (610, 50))

test_Hfilling2 = pygame.Surface((340, 15))
test_Hfilling2.fill('Red')
test_filling2 = test_Hfilling.get_rect(midbottom = (610, 45))

#create players
player1_surface = pygame.image.load('img\square.png').convert()
player1_rect = player1_surface.get_rect(midbottom = (100,200))
player2_surface = pygame.image.load('img\square.png').convert()
player2_rect = player2_surface.get_rect(midbottom = (400,400))


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
                player1_Speed = 20
                player1_Speed += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1_Speed = -20
                player1_Speed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                player1_Speed = 0
        if keys[pygame.K_SPACE]: 
            player1_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player2_Speed = 20
                player2_Speed += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2_Speed = -20
                player2_Speed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player2_Speed = 0
        if keys[pygame.K_UP]:
            player2_gravity = -20
            


    player2_gravity += 1
    player1_gravity += 1
    player2_rect.x += player2_Speed
    player1_rect.x += player1_Speed
    player1_rect.y += player1_gravity
    player2_rect.y += player2_gravity
    print(player1_rect.bottom)
    print(player1_Speed)

    if player1_rect.bottom > 401: 
        player1_rect.bottom = 400
        screen.blit(player1_surface, player1_rect)
    if player2_rect.bottom > 401:
        player2_rect.bottom = 400
        screen.blit(player2_surface, player2_rect)
    screen.blit(test_background, (0, 0))
    screen.blit(player1_surface, player1_rect)
    screen.blit(player2_surface, player2_rect)
    screen.blit(test_health, test_HRect)
    screen.blit(test_Hfilling, test_filling)
    screen.blit(test_health2, test_HRect2)
    screen.blit(test_Hfilling2, test_filling2)

            
    pygame.display.update()
    clock.tick(60)

