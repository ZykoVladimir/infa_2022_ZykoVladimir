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
line = 200
k = 3
time_min = 2 * FPS
time_max = 6 * FPS
g = 0.05
time_tick_anim_sm = 0.5 * FPS
tick = 0
time_nag_limit = 2
mean = 0
rad_anim_sm = 20


class Goal:
    """Goal"""
    a = 50
    b = 20
    speed = 2

    def __init__(self):
        self.napr = np.array([float(randint(-self.speed, self.speed)),
                              float(randint(-self.speed, self.speed))])
        self.coord = np.array([float(randint(0, xx - self.a)),
                               float(randint(0, yy - line - self.b))])


def rasst_gr_x0(f):
    """Distance to the left border"""
    if f.coord[0] > 0:
        return True
    else:
        return False


def rasst_gr_y0(f):
    """Distance to the upper border"""
    if f.coord[1] > 0:
        return True
    else:
        return False


def rasst_gr_xx(f):
    """Distance to the right border"""
    if (xx - f.coord[0]) > f.a:
        return True
    else:
        return False


def rasst_gr_line(f):
    """Distance to the line"""
    if (yy - line - f.coord[1]) > f.b:
        return True
    else:
        return False


def new_goal(goal_f):
    """Creating new goals"""
    while len(goal_f) < k:
        new_goal = Goal()
        if rasst_gr_x0(new_goal) and \
                rasst_gr_y0(new_goal) and \
                rasst_gr_xx(new_goal) and \
                rasst_gr_line(new_goal):
            goal_f.append(new_goal)


def smena_napr_and_coord(goal_f):
    """Changing the direction of movement of the target when interacting with the boundary in a random direction"""
    if not rasst_gr_y0(goal_f):
        goal_f.napr = np.array([float(randint(-goal_f.speed, goal_f.speed)), float(randint(0, goal_f.speed))])
    if not rasst_gr_xx(goal_f):
        goal_f.napr = np.array([float(randint(-goal_f.speed, 0)), float(randint(-goal_f.speed, goal_f.speed))])
    if not rasst_gr_line(goal_f):
        goal_f.napr = np.array([float(randint(-goal_f.speed, goal_f.speed)), float(randint(-goal_f.speed, 0))])
    if not rasst_gr_x0(goal_f):
        goal_f.napr = np.array([float(randint(0, goal_f.speed)), float(randint(-goal_f.speed, goal_f.speed))])
    goal_f.coord += goal_f.napr


def displey_goals(goals_f):
    """Goals mapping"""
    for i in goals_f:
        pygame.draw.ellipse(screen, RED, (i.coord[0], i.coord[1], i.a, i.b))


def displey_line():
    """Line mapping"""
    rect(screen, WHITE, (0, yy - line, xx, 1))


class Bomb:
    """Bomb"""
    rad_bomb = 5
    a_bomb = 50
    b_bomb = 20
    speed_bomb_inverted = 140

    def __init__(self, goal, gun):
        self.napr = np.array([((gun.a_gun / 2) + gun.coord[0] - goal.coord[0]) / self.speed_bomb_inverted,
                              ((gun.b_gun / 2) + gun.coord[1] - goal.coord[1]) / self.speed_bomb_inverted])
        self.coord = np.array([(goal.coord[0] + (self.a_bomb / 2)), (goal.coord[1] + (self.b_bomb / 2))])


def displey_bomb(bombs_f):
    """Bombs mapping"""
    for i in bombs_f:
        circle(screen, BLUE, (i.coord[0], i.coord[1]), i.rad_bomb)


def napr_bomb(bombs_f):
    """Direction bomb"""
    for i in bombs_f:
        i.coord += i.napr


class Gun:
    """Gun"""
    a_gun = 60
    b_gun = 10
    speed_gun = 20

    def __init__(self):
        self.coord = np.array([(xx - self.a_gun) / 2, (yy - 20)])


def displey_gun(gun_f):
    """Gun mapping"""
    rect(screen, WHITE, (gun_f.coord[0], gun_f.coord[1], gun_f.a_gun, gun_f.b_gun))


def chek_bombs(bombs_f, gun_f):
    """Checking for hitting the gun"""
    for i in bombs_f:
        if (gun_f.coord[1] - i.rad_bomb <= i.coord[1]) and \
                (i.coord[1] <= gun_f.coord[1] + gun_f.b_gun + i.rad_bomb) and \
                (gun_f.coord[0] - i.rad_bomb <= i.coord[0]) and \
                (i.coord[0] <= gun_f.coord[0] + gun_f.a_gun + i.rad_bomb):
            return True


class Shot:
    """Shot"""
    speed_shot = 0.12
    rad_shot = 5

    def __init__(self, gun, position, time_nag):
        self.rasst = ((position[0] - gun.coord[0] + (gun.a_gun / 2))**2 +
                      (position[1] - gun.coord[1] - (gun.b_gun / 2))**2)**(1 / 2)
        self.coord = np.array([(gun.coord[0] + (gun.a_gun / 2)), (gun.coord[1] + (gun.b_gun / 2))])
        self.mod_x = (position[0] - gun.coord[0] - (gun.a_gun / 2))
        self.mod_y = (position[1] - gun.coord[1] + (gun.b_gun / 2))
        self.napr = np.array([(self.speed_shot * time_nag * (self.mod_x / self.rasst)),
                              (self.speed_shot * time_nag * (self.mod_y / self.rasst))])
        self.time_life = 0


def napr_shots(shots_f):
    """Direction shots"""
    for i in shots_f:
        i.time_life += 1
        i.coord[0] += i.napr[0]
        i.coord[1] += i.napr[1] + (g * i.time_life)


def displey_shots(shots_f):
    """Shots mapping"""
    for i in shots_f:
        circle(screen, WHITE, i.coord, i.rad_shot)


def chek_shots(shots_f, goals_f):
    """Checking for hitting the goal"""
    coff = 0
    for i in shots_f:
        for j in goals_f:
            if (j.coord[0] - i.rad_shot <= i.coord[0] <= j.coord[0] + j.a + i.rad_shot) and \
                            (j.coord[1] - i.rad_shot <= i.coord[1] <= j.coord[1] + j.b + i.rad_shot):
                coff += 1
                shots_f.remove(i)
                goals_f.remove(j)
                goals_f.append(Goal())
                break
    return coff


def displey_text(size, color, position, text):
    """Text mapping"""
    f_font = pygame.font.Font(None, size)
    f_text = f_font.render(text, True, color)
    f_position = position
    return screen.blit(f_text, f_position)


goals = []
gun = Gun()
bombs = []
time = []
shots = []
anim_coord = []
time_anim_sm = []
anim_sm = []
yellow_anim_sm = []
for i in range(k):
    time.append(randint(time_min, time_max))

while not finished:
    new_goal(goals)
    clock.tick(FPS)
    tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if gun.coord[0] > 0:
                    gun.coord -= [gun.speed_gun, 0]
            if event.key == pygame.K_RIGHT:
                if xx - gun.coord[0] > gun.a_gun:
                    gun.coord += [gun.speed_gun, 0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                tick = 0
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if tick >= time_nag_limit * FPS:
                    shots.append(Shot(gun, event.pos, time_nag_limit * FPS))
                    tick = 0
                else:
                    shots.append(Shot(gun, event.pos, tick))
                    tick = 0

    for i in range(k):
        time[i] -= 1
        if time[i] == 0:
            bombs.append(Bomb(goals[i], gun))
            time[i] = randint(time_min, time_max)
    for i in goals:
        smena_napr_and_coord(i)
    napr_bomb(bombs)
    displey_bomb(bombs)
    displey_goals(goals)
    displey_line()
    displey_gun(gun)
    if chek_bombs(bombs, gun):
        finished = True
    napr_shots(shots)

    mean_new = chek_shots(shots, goals)
    mean += mean_new

    displey_shots(shots)
    displey_text(40, WHITE, (20, yy - line + 20), 'Score')
    displey_text(40, WHITE, (100, yy - line + 20), str(mean))

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()