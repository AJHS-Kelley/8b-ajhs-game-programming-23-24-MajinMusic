# Number SLider by Jacob Desha, based on a project by Al Sweigart, v0.1

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating System Commands) 

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for Game Board
BOARDWIDTH = 4 # Columns
BOARDHEIGHT = 4 # Rows
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # This is a maximum value! Won't make a slow computer run faster.

BLANK = None