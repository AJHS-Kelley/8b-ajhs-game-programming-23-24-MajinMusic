# The Ultimate Pygame by Jacob Desha v0.13
import pygame
from sys import exit
from random import randint



def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 375: screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(bird_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50) #(Font type, font size)
start = pygame.font.Font(None, 20)
game_active = False
start_time = 0
score = 0
# mouse_pos = pygame.mouse.get_pos()


sky_surf = pygame.image.load("img/sky1.png").convert()
ground_surf = pygame.image.load("img/ground.png").convert()

# score_surf = test_font.render('My game', False, (64, 64, 64)) #(te)xt, AA, color)
# score_rect = score_surf.get_rect(midbottom = (400, 50))

# Obstacles
snail_surf = pygame.image.load("img/snail1.png").convert_alpha()
snail_surf = pygame.transform.rotozoom(snail_surf, 0, 0.25)
bird_surf = pygame.image.load("img/bird.png").convert_alpha()
bird_surf = pygame.transform.rotozoom(bird_surf, 0, 0.075)
bird_surf = pygame.transform.flip(bird_surf, 180, 0)


obstacle_rect_list = []

player_surf = pygame.image.load("img/player.png").convert_alpha()
player_surf = pygame.transform.rotozoom(player_surf, 0, 0.75)
player_rect = player_surf.get_rect(midbottom = (50, 390))
player_gravity = 0

gameName_surf = font.render('Snail Jumper',False, (111,196,69))
rules_surf = font.render('Press the Spacebar to jump and start!', False, (111,196,69))
gameName_rect = gameName_surf.get_rect(center = (400, 50))
rules_rect = rules_surf.get_rect(center = (400, 350))

# Intro screen
player_stand = pygame.image.load("img/player.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 0.75)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True: 
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 375)))
            else:
                obstacle_rect_list.append(bird_surf.get_rect(bottomright = (randint(900,1100), 125)))
            


# (300, 50)
    if game_active:
        # Draw all our elements
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf, (-250, 0))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
        pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
        # pygame.draw.line(screen, 'Gold', (0,0), (800, 400), 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 380: player_rect.bottom = 380
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions(player_rect,obstacle_rect_list)
        
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = font.render(f'Your score: {score}', False, (111,196,69))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(gameName_surf,gameName_rect)

        if score == 0: screen.blit(rules_surf,rules_rect)
        else: screen.blit(score_message, score_message_rect)
        




    # Update everything
    pygame.display.update()
    clock.tick(60)
