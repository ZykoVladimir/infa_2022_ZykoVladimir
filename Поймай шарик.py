import pygame
from pygame.draw import *
from random import randint
import numpy as np

xx = 1000
yy = 600
pygame.init()
screen = pygame.display.set_mode((xx, yy))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

FPS = 60
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WHITE = (255, 255, 255)
k = 5
TIME = FPS * 30
mean = 0
color_next = 0


class Sharik:
    '''Variables'''
    rad_max = 50
    rad_min = 20
    time_life = 2 * FPS

    '''Creating variables'''
    def __init__(self):
        self.__napr = np.array([float(randint(-10, 10)),
                                float(randint(-10, 10))])
        self.__rad = randint(self.rad_min, self.rad_max)
        self.__coord = np.array([float(randint(0, xx)),
                                 float(randint(0, yy))])
        self.__color = COLORS[randint(0, len(COLORS) - 1)]

    '''getters'''
    def get_napr(self):
        return self.__napr

    def get_rad(self):
        return self.__rad

    def get_coord(self):
        return self.__coord

    def get_color(self):
        return self.__color

    '''setters'''
    def set_coord(self, coord):
        self.__coord = coord

    def set_napr(self, napr):
        self.__napr = napr


def rasst_gr_x0(ball_f):
    '''Determining the distance from the center of the ball to the left border'''
    if ball_f.get_coord()[0] > ball_f.get_rad():
        return True
    else:
        return False


def rasst_gr_y0(ball_f):
    '''Determining the distance from the center of the ball to the upper boundary'''
    if ball_f.get_coord()[1] > ball_f.get_rad():
        return True
    else:
        return False


def rasst_gr_xx(ball_f):
    '''Determining the distance from the center of the ball to the right border'''
    if (xx - ball_f.get_coord()[0]) > ball_f.get_rad():
        return True
    else:
        return False


def rasst_gr_yy(ball_f):
    '''Determining the distance from the center of the ball to the lower border'''
    if (yy - ball_f.get_coord()[1]) > ball_f.get_rad():
        return True
    else:
        return False


def new_balls(balls_f):
    '''Creating an array of balls from k elements'''
    while len(balls_f) < k:
        new_ball = Sharik()
        if rasst_gr_x0(new_ball) and \
                rasst_gr_y0(new_ball) and \
                rasst_gr_xx(new_ball) and \
                rasst_gr_yy(new_ball):
            balls.append(new_ball)


def smena_napr(balls_f):
    '''Changing the direction of movement after hitting the border in a random direction'''
    if not rasst_gr_y0(balls_f):
        balls_f.set_napr(np.array([float(randint(-10, 10)), float(randint(0, 10))]))
    if not rasst_gr_xx(balls_f):
        balls_f.set_napr(np.array([float(randint(-10, 0)), float(randint(-10, 10))]))
    if not rasst_gr_yy(balls_f):
        balls_f.set_napr(np.array([float(randint(-10, 10)), float(randint(-10, 0))]))
    if not rasst_gr_x0(balls_f):
        balls_f.set_napr(np.array([float(randint(0, 10)), float(randint(-10, 10))]))


def displey_balls(balls_f):
    '''Displaying balls on the screen'''
    for i in balls_f:
        circle(screen, i.get_color(), i.get_coord(), i.get_rad())
        circle(screen, WHITE, i.get_coord(), i.get_rad(), 2)


def f_text_displey(size, color, position, text):
    '''Displaying text on the screen'''
    f_font = pygame.font.Font(None, size)
    f_text = f_font.render(text, True, color)
    f_position = position
    return screen.blit(f_text, f_position)


balls = []
vr = 0
font = pygame.font.Font(None, 50)
font_next = pygame.font.Font(None, 75)
font_large = pygame.font.Font(None, 100)

while not finished:
    vr += 1
    new_balls(balls)
    clock.tick(FPS)
    for i in balls:
        i.set_coord(i.get_coord() + i.get_napr())
        smena_napr(i)
    displey_balls(balls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in balls:
                if ((event.pos[0] - i.get_coord()[0]) ** 2 + (event.pos[1] - i.get_coord()[1]) ** 2) ** (1 / 2) \
                        < i.get_rad():
                    balls.remove(i)
                    mean += 1
    f_text_displey(50, WHITE, (10, 10), 'Score')
    f_text_displey(50, WHITE, (110, 10), str(mean))
    pygame.display.update()
    screen.fill(BLACK)
    if vr >= TIME:
        finished = True

finished = False
text1 = font_next.render('You scored', True, WHITE)
text1_position = text1.get_rect(center=(xx/2, (yy-100)/2))
text2 = font_next.render(str(mean), True, WHITE)
text2_position = text2.get_rect(center=(xx/2, (yy)/2))
text3_1 = font_large.render('Terrible result!', True, WHITE)
text3_1_position = text3_1.get_rect(center=(xx/2, (yy+125)/2))
text3_2 = font_large.render('Good!', True, WHITE)
text3_2_position = text3_2.get_rect(center=(xx/2, (yy+125)/2))
text3_3 = font_large.render('Excellent result!', True, WHITE)
text3_3_position = text3_3.get_rect(center=(xx/2, (yy+125)/2))

for i in range(2 * FPS):
    color_next += 1
    clock.tick(FPS)
    screen.fill([0, color_next, 0])
    screen.blit(text1, text1_position)
    screen.blit(text2, text2_position)
    if mean < 20:
        screen.blit(text3_1, text3_1_position)
    if 20 <= mean < 40:
        screen.blit(text3_2, text3_2_position)
    if 40 <= mean:
        screen.blit(text3_3, text3_3_position)
    pygame.display.update()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()