import pygame
from game import *
from variabls import *

if flag_level_1:
    screen.fill(ORANGE)
    rect(screen, BLACK, (parametrs[0], 20, 0, 0))
    screen.blit(image_level_1, (0, 0))