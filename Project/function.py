import pygame
from pygame.draw import *
from random import randint
import numpy as np
import math
import cv2
np.seterr(divide='ignore') # Игнорирование ошибки деления на ноль


# Goal
class Goal:
    '''Мишени, (ширина, высота, скорость, ГП, Э, цвет)'''
    def __init__(self, a, b, speed, parametrs, screen, color):
        self.color = color
        self.screen = screen
        self.parametrs = parametrs
        self.speed = speed
        self.a = a
        self.b = b
        self.napr = np.array([float(randint(-self.speed, self.speed)),
                              float(randint(-self.speed, self.speed))])
        self.coord = np.array([float(randint(0, self.parametrs[0] - self.a)),
                               float(randint(0, self.parametrs[1] - self.parametrs[2] - self.b))])


def rasst_gr_x0(f):
    '''True, если мишень коснулась левой границы (мишень)'''
    if f.coord[0] > 0:
        return True
    else:
        return False


def rasst_gr_y0(f):
    '''True, если мишень коснулась верхней границы (мишень)'''
    if f.coord[1] > 0:
        return True
    else:
        return False


def rasst_gr_xx(f):
    '''True, если мишень коснулась правой границы (мишень)'''
    if (f.parametrs[0] - f.coord[0]) > f.a:
        return True
    else:
        return False


def rasst_gr_line(f):
    '''True, если мишень коснулась нижней границы - линии (мишень)'''
    if (f.parametrs[1] - f.parametrs[2] - f.coord[1]) > f.b:
        return True
    else:
        return False


def new_goal(goal_f, k, screen, color, a, b, parametrs, speed):
    '''Создание новых мишеней в случае уничтожения (мишени, количество мишеней, Э,
    цвет, высота, ширина, ГП, скорость)'''
    while len(goal_f) < k:
        new_goal = Goal(a, b, speed, parametrs, screen, color)
        if rasst_gr_x0(new_goal) and \
                rasst_gr_y0(new_goal) and \
                rasst_gr_xx(new_goal) and \
                rasst_gr_line(new_goal):
            goal_f.append(new_goal)


def napr_goals(goals):
    '''Смена напрваления мишеней в случае столкновения со стенкой в случайном направлении (мишень)'''
    for i in goals:
        if not rasst_gr_y0(i):
            i.napr = np.array([float(randint(-i.speed, i.speed)), float(randint(0, i.speed))])
        if not rasst_gr_xx(i):
            i.napr = np.array([float(randint(-i.speed, 0)), float(randint(-i.speed, i.speed))])
        if not rasst_gr_line(i):
            i.napr = np.array([float(randint(-i.speed, i.speed)), float(randint(-i.speed, 0))])
        if not rasst_gr_x0(i):
            i.napr = np.array([float(randint(0, i.speed)), float(randint(-i.speed, i.speed))])
        i.coord += i.napr


def displey_goals(goals_f, image_2, color):
    '''Отображение мишеней (мишени, Э, картинка)'''
    for i in goals_f:
        i.screen.blit(image_2, (i.coord[0], i.coord[1]))
        #pygame.draw.ellipse(i.screen, color, (i.coord[0], i.coord[1], i.a, i.b))


# Line
def displey_line(screen, color, parametrs):
    '''Отображение линии (Э, цвет, ГП)'''
    rect(screen, color, (0, parametrs[1] - parametrs[2], parametrs[0], 1))


# Gan
class Gun:
    '''Пушка (ширина, высота, скорость, ГП, Э, увет)'''
    def __init__(self, a, b, speed, parametrs, screen, color, rasst_gr_gun):
        self.color = color
        self.screen = screen
        self.a = a
        self.b = b
        self.speed = speed
        self.coord = np.array([(parametrs[0] - self.a) / 2, (parametrs[1] - self.b - rasst_gr_gun)])


def displey_gun(gun, image):
    '''Отображение пушки (пушка)'''
    gun.screen.blit(image, (gun.coord[0], gun.coord[1]))
    #rect(gun.screen, gun.color, (gun.coord[0], gun.coord[1], gun.a, gun.b))


def chek_bombs(bombs_f, gun_f):
    '''Проверка попадания бомбы в пушку (бомбы, пушка)'''
    for i in bombs_f:
        if (gun_f.coord[1] - i.rad <= i.coord[1]) and \
                (i.coord[1] <= gun_f.coord[1] + gun_f.b + i.rad) and \
                (gun_f.coord[0] - i.rad <= i.coord[0]) and \
                (i.coord[0] <= gun_f.coord[0] + gun_f.a + i.rad):
            return True

# Bomb
class Bomb:
    '''Бомба (мишень, пушка, радиус, скорость, Э)'''
    def __init__(self, goal, gun, rad, speed, screen, flag_moverment_gun_left, flag_moverment_gun_right):
        self.screen = screen
        self.rad = rad
        self.randint = randint(0, 1)
        self.speed = speed / ((abs(((gun.a / 2) + gun.coord[0] - goal.coord[0])))**2 +
                              (abs(((gun.b / 2) + gun.coord[1] - goal.coord[1])))**2)**0.5
        if self.randint == 0:
            self.napr = np.array([((gun.a / 2) + gun.coord[0] - goal.coord[0] - goal.a / 2) * self.speed,
                              ((gun.b / 2) + gun.coord[1] - goal.coord[1] - goal.b / 2) * self.speed])
        if self.randint == 1:
            if flag_moverment_gun_left:
                self.napr = np.array([((gun.a / 2) + gun.coord[0] - goal.coord[0] - goal.a / 2) * self.speed - gun.speed,
                                  ((gun.b / 2) + gun.coord[1] - goal.coord[1] - goal.b / 2) * self.speed])
            elif flag_moverment_gun_right:
                self.napr = np.array([((gun.a / 2) + gun.coord[0] - goal.coord[0] - goal.a / 2) * self.speed + gun.speed,
                                  ((gun.b / 2) + gun.coord[1] - goal.coord[1] - goal.b / 2) * self.speed])
            elif not flag_moverment_gun_right and not flag_moverment_gun_right:
                self.napr = np.array([((gun.a / 2) + gun.coord[0] - goal.coord[0] - goal.a / 2) * self.speed,
                              ((gun.b / 2) + gun.coord[1] - goal.coord[1] - goal.b / 2) * self.speed])
        self.coord = np.array([(goal.coord[0] + (goal.a / 2)), (goal.coord[1] + (goal.b / 2))])


def displey_bomb(bombs_f, color):
    '''Отображение бомб (бомбы, цвет)'''
    for i in bombs_f:
        circle(i.screen, color, (i.coord[0], i.coord[1]), i.rad)


def napr_bomb(bombs_f):
    '''Смена координат бомб (бомбы)'''
    for i in bombs_f:
        i.coord += i.napr


def delete_bomb(bombs_f, parametrs):
    '''Удаление бомбы в случае её выхода за границы экрана,
    где граница экрана больше на 0.1x, чем параметры экрана (бомбы, ГП)'''
    for i in bombs_f:
        if i.coord[0] <= - 0.1 * parametrs[0] or i.coord[0] > 1.1 * parametrs[0] or \
                        i.coord[1] <= - 0.1 * parametrs[1] or i.coord[1] > 1.1 * parametrs[1]:
            bombs_f.remove(i)


# Shot
class Shot:
    '''Выстрел (пушка, позиция выстрела, время нажатия, радиус, скорость, УСП, ГП)'''
    def __init__(self, gun, position, time_nag, rad, speed, screen, g, parametrs):
        self.parametrs = parametrs
        self.g = g
        self.screen = screen
        self.rad = rad
        self.speed = speed
        self.rasst = ((position[0] - gun.coord[0] + (gun.a / 2))**2 +
                      (position[1] - gun.coord[1] - (gun.b / 2))**2)**(1 / 2)
        self.coord = np.array([(gun.coord[0] + (gun.a / 2)), (gun.coord[1] + (gun.b / 2))])
        self.mod_x = (position[0] - gun.coord[0] - (gun.a / 2))
        self.mod_y = (position[1] - gun.coord[1] + (gun.b / 2))
        self.napr = np.array([(self.speed * time_nag * (self.mod_x / self.rasst)),
                              (self.speed * time_nag * (self.mod_y / self.rasst))])
        self.time = 0


def napr_shots(shots_f):
    '''Смена координаты выстрела с учетом УСП (выстрелы)'''
    for i in shots_f:
        i.time += 1
        i.coord[0] += i.napr[0]
        i.coord[1] += i.napr[1] + (i.g * i.time)


def displey_shots(shots_f, color):
    '''Отображение выстрелов (выстрелы)'''
    for i in shots_f:
        circle(i.screen, color, i.coord, i.rad)


def chek_shot(f, goals):
    '''Проверка попадания выстрела или ракеты'''
    if abs((f.coord[0] + f.rad) - (goals.coord[0] + (goals.a / 2))) \
            <= (f.rad + goals.a / 2) and \
            abs((f.coord[1] + f.rad) - (goals.coord[1] + (goals.b / 2))) \
            <= (f.rad + goals.b / 2):
        return f.coord, True
    else:
        return (-100, -100), False


def anim_sm_shot_and_rocket(f, goals, anim_sm, time_anim_sm, color_anim_sm, rad_anim_sm, screen):
    '''Уничтожение мишени и анимация взрыва при попадании выстрела или ракеты (калибры, мишени, массив sm анимации,
    время анимации, начальный цвет анимации, начальный радиус анимации, Э)'''
    color = [color_anim_sm[0], color_anim_sm[1], color_anim_sm[2]]
    T = time_anim_sm
    R = rad_anim_sm
    coff = 0
    del_f = False
    for i in f:
        for j in goals:
            coord, flag = chek_shot(i, j)
            if flag:
                anim_sm.append([[coord[0], coord[1]], time_anim_sm, color, rad_anim_sm])
                coff += 1
                goals.remove(j)
                del_f = True
        if del_f:
            f.remove(i)
    for i in anim_sm:
        if i[1] > 0:
            i[1] -= 1
            circle(screen, i[2], i[0], R - i[3])
            i[2][1] -= 4
            i[3] = i[3] * (i[1] / T)
    return coff


# Rocket
class Rocket:
    '''Ракета (пушка, позиция мыши, радиус, скорость, УСП, ГП)'''
    def __init__(self, gun, position, rad, speed, g, screen, parametrs):
        self.parametrs = parametrs
        self.screen = screen
        self.g = g
        self.rad = rad
        self.speed = speed
        self.coord = np.array([(gun.coord[0] + (gun.a / 2)), (gun.coord[1] + (gun.b / 2))])
        self.rasst = ((position[0] - gun.coord[0] + (gun.a / 2)) ** 2 +
                      (position[1] - gun.coord[1] - (gun.b / 2)) ** 2) ** (1 / 2)
        self.mod_x = (position[0] - gun.coord[0] - (gun.a / 2))
        self.mod_y = (position[1] - gun.coord[1] + (gun.b / 2))
        self.napr = np.array([(self.speed * (self.mod_x / self.rasst)),
                              (self.speed * (self.mod_y / self.rasst))])
        self.time = 0
        self.flag = True


def napr_rocket(rockets_f, position):
    '''Смеша координат ракеты (ракеты, положение мыши в данный момент)'''
    for i in rockets_f:
        if i.flag:
            i.rasst = ((position[0] - i.coord[0]) ** 2 +
                          (position[1] - i.coord[1]) ** 2) ** (1 / 2)
            i.mod_x = (position[0] - i.coord[0])
            i.mod_y = (position[1] - i.coord[1])
            i.napr = np.array([(i.speed * (i.mod_x / i.rasst)),
                                  (i.speed * (i.mod_y / i.rasst))])
            i.coord += i.napr
        else:
            i.time += 1
            i.coord[0] += i.napr[0]
            i.coord[1] += i.napr[1] + (i.g * i.time)


def displey_rocket(rockets_f, color):
    '''Отображение ракет (ракеты)'''
    for i in rockets_f:
        circle(i.screen, color, i.coord, i.rad)


def off(rockets_f, coord_prediction_f):
    '''Отключение ракеты в случае достижения ею координат мыши (ракеты, коорданата мыши в данный момент)'''
    for i in rockets_f:
        R = ((i.coord[0] - coord_prediction_f[0])**2 +
             (i.coord[1] - coord_prediction_f[1])**2)**(1 / 2)
        if R < 10:
            i.flag = False


# Displey
def displey_text(size, color, position, text, screen):
    '''Отображение текста Score x (уровень, цвет, позиция, текст, Э)'''
    f_font = pygame.font.Font(None, size)
    f_text = f_font.render(text, True, color)
    f_position = position
    return screen.blit(f_text, f_position)


def displey_level(level, screen, color_gr, parametrs, width, height, rasst_gr,
                  k_level, thickness, color_1, color_2, color_3, width_caliber_ult):
    '''Отображение уровня ульты (кол-во заполнености шкалы, Э, цвет границы, ширина, высота, расстояние до границ,
    количество попаданий, необходимые для ульты, толщина, цвет 1, цвет 2, цвет 3)'''
    rect(screen, color_gr, (parametrs[0] - width - 2 * rasst_gr - width_caliber_ult,
                            parametrs[1] - parametrs[2] + rasst_gr, width, height * k_level + thickness), thickness)
    for i in range(k_level):
        if level >= k_level:
            rect(screen, color_1, (parametrs[0] - width - 2 * rasst_gr + thickness - width_caliber_ult,
                            parametrs[1] - parametrs[2] + rasst_gr + i * height + thickness,
                            width - 2 * thickness, height - thickness))
        if k_level // 2 < level < k_level:
            rect(screen, color_2, (parametrs[0] - width - 2 * rasst_gr + thickness - width_caliber_ult,
                            parametrs[1] - parametrs[2] + rasst_gr + i * height + thickness,
                            width - 2 * thickness, height - thickness))
        if level <= k_level // 2:
            rect(screen, color_3, (parametrs[0] - width - 2 * rasst_gr + thickness - width_caliber_ult,
                            parametrs[1] - parametrs[2] + rasst_gr + i * height + thickness,
                            width - 2 * thickness, height - thickness))
        rect(screen, color_gr, (parametrs[0] - width - 2 * rasst_gr - width_caliber_ult,
                                parametrs[1] - parametrs[2] + rasst_gr + i * height, width, thickness))
        for i in range(k_level - level):
            rect(screen, (0, 0, 0),
                 (parametrs[0] - width - 2 * rasst_gr + thickness - width_caliber_ult,
                  parametrs[1] - parametrs[2] + rasst_gr + i * height + thickness,
                  width - 2 * thickness, height - thickness))


def displey_k_rockets(kolvo_rockets_f, screen, color, rasst_gr, w, h, parametrs, width, width_caliber_ult):
    '''Отображение количества доступных ракет (количество ракет, Э, цвет, расстояние до границы, радиус,
    расстояние по вертикали между ракетами, ГП, ширина)'''
    for i in range(kolvo_rockets_f):
        circle(screen, color, (parametrs[0] - 2 * rasst_gr - width - w - w / 2 - width_caliber_ult,
                               parametrs[1] - parametrs[2] + rasst_gr + h / 2 + i * (h + 5)), w, h)


def displey_update_caliber(time_new, time, rasst_gr, height, width, screen, parametrs,
                           color1, color2, color_gr, thickness):
    '''Отображение уровня перезарядки калибра (время до конца перезарядки, время перезарядки,
    расстояние до границ, высота, ширина, Э, ГП, цвет готовности к выстрелу, цвет перезарядки,
    цвет границ, ширина линии)'''
    if time_new < 0:
        rect(screen, color_gr, (parametrs[0] - rasst_gr - width, parametrs[1] - parametrs[2] + rasst_gr,
                              width, height), thickness)
        rect(screen, color1, (parametrs[0] - rasst_gr - width + thickness,
                              parametrs[1] - parametrs[2] + rasst_gr + thickness, width - 2 * thickness,
                              height - 2 * thickness))
    else:
        rect(screen, color_gr, (parametrs[0] - rasst_gr - width, parametrs[1] - parametrs[2] + rasst_gr,
                                width, height), thickness)
        rect(screen, color2, (parametrs[0] - rasst_gr - width + thickness,
            parametrs[1] - parametrs[2] + rasst_gr + thickness + (height - 2 * thickness) *
            ((time_new) / time), width - 2 * thickness, (height - 2 * thickness) * ((time - time_new) / time) + 1))


def delete(f):
    if len(f) > 0:
        for i in f:
            if i.coord[1] < -100 or i.coord[1] > i.parametrs[1] + 100:
                f.remove(i)

def screen_death(screen, video, parametrs):
    '''Экран после проигрыша'''
    video = cv2.VideoCapture(video)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(video_image.tobytes(), video_image.shape[1::-1], "BGR")
            video_surf = pygame.transform.scale(video_surf, (parametrs[0], parametrs[1]))
        else:
            run = False
        screen.blit(video_surf, (0, 0))
        pygame.display.flip()

    pygame.quit()
    exit()

# Caliber
class Caliber:
    '''Калибр (ширина, длина, начальная скорость, ускорение, Э, ГП, пушка)'''
    def __init__(self, a, b, speed, boost, screen, parametrs, gun):
        self.a = a
        self.b = b
        self.speed = speed
        self.boost = boost
        self.screen = screen
        self.parametrs = parametrs
        self.coord = np.array([gun.coord[0] + (gun.a / 2) - (self.a / 2), gun.coord[1] + (gun.b / 2) - (self.b / 2)])
        self.napr = np.array([0, self.speed])


def napr_caliber(calibers):
    '''Смена координаты калибра, имеется ускорение boost по вертикальной оси (калибры)'''
    for i in calibers:
        i.coord[1] -= i.napr[1]
        i.napr = i.napr * np.array([i.boost, i.boost])


def displey_caliber(calibers, color, image):
    '''Отображение килабров'''
    for i in calibers:
        i.screen.blit(image, (i.coord[0], i.coord[1]))
        #rect(i.screen, color, (i.coord[0], i.coord[1], i.a, i.b))


def chek_caliber(caliber, goals):
    '''Проверка попадания калибра в мишень'''
    if abs((caliber.coord[0] + (caliber.a / 2)) - (goals.coord[0] + (goals.a / 2))) \
            <= (caliber.a / 2 + goals.a / 2) and \
            abs((caliber.coord[1] + (caliber.b / 2)) - (goals.coord[1] + (goals.b / 2))) \
            <= (caliber.b / 2 + goals.b / 2):
        return caliber.coord, True
    else:
        return (-100, -100), False


def anim_sm_caliber(calibers, goals, anim_sm, time_anim_sm, color_anim_sm, rad_anim_sm, screen):
    '''Уничтожение мишени и анимация взрыва при попадании калибра (калибры, мишени, массив sm анимации,
    время анимации, начальный цвет анимации, начальный радиус анимации, Э)'''
    color = [color_anim_sm[0], color_anim_sm[1], color_anim_sm[2]]
    T = time_anim_sm
    R = rad_anim_sm
    coff = 0
    del_caliber = False
    for i in calibers:
        for j in goals:
            coord, flag = chek_caliber(i, j)
            if flag:
                anim_sm.append([[coord[0], coord[1]], time_anim_sm, color, rad_anim_sm])
                coff += 1
                goals.remove(j)
                del_caliber = True
        if del_caliber:
            calibers.remove(i)
    for i in anim_sm:
        if i[1] > 0:
            i[1] -= 1
            circle(screen, i[2], i[0], R - i[3])
            i[2][1] -= 4
            i[3] = i[3] * (i[1] / T)
    return coff


# Ult1
class Ult1:
    '''Первая ульта - лазер (Э, координаты положения мыши, пушка, ширина линии, ГП, время выстрела)'''
    def __init__(self, screen, coord, gun, thickness, parametrs, time):
        self.screen = screen
        self.coord = coord
        self.gun = gun
        self.thickness = thickness
        self.parametrs = parametrs
        self.time = time


def angle_rect(x0, y0, width, height, alpha, color, screen):
    '''Поворот прямоугольника на некоторый угол'''
    x1 = x0 + width * math.cos(alpha)
    y1 = y0 - width * math.sin(alpha)
    x2 = x1 + height * math.sin(alpha)
    y2 = y1 + height * math.cos(alpha)
    x3 = x0 + height * math.sin(alpha)
    y3 = y0 + height * math.cos(alpha)
    return polygon(screen, color, [(x0, y0), (x1, y1),
                (x2, y2), (x3, y3)])


def displey_ult1(ult1s, color):
    '''Отображения первой ульты (ульты1, увет)'''
    for i in ult1s:
        if math.atan((i.gun.coord[1] + i.gun.b / 2 - i.coord[1]) / (i.coord[0] - i.gun.coord[0] - i.gun.a / 2)) > 0:
            alpha = math.atan((i.gun.coord[1] + i.gun.b / 2 - i.coord[1]) /
                              (i.coord[0] - i.gun.coord[0] - i.gun.a / 2))
        else:
            alpha = math.pi + math.atan((i.gun.coord[1] + i.gun.b / 2 - i.coord[1]) /
                                        (i.coord[0] - i.gun.coord[0] - i.gun.a / 2))
        if i.time > 0:
            angle_rect(i.gun.coord[0] + i.gun.a / 2, i.gun.coord[1] + i.gun.b / 2,
                       3 * max(i.parametrs[0], i.parametrs[1]), i.thickness, alpha, color, i.screen)
            i.time -= 1
        if i.time == 0:
            ult1s.remove(i)


def chek_ult1(ult1, goal):
    '''Проверка попадания первой ульты в мишень (ульта1, мишень)'''
    if math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - ult1.coord[1]) /
                 (ult1.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2)) > 0:
        alpha = math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - ult1.coord[1]) /
                          (ult1.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2))
    else:
        alpha = math.pi + math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - ult1.coord[1]) /
                                    (ult1.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2))

    if math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - goal.coord[1]) /
                 (goal.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2)) > 0:
        phi1 = math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - goal.coord[1]) /
                          (goal.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2))
    else:
        phi1 = math.pi + math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - (goal.coord[1] + goal.b)) /
                                    (goal.coord[0] - ult1.gun.coord[0] - ult1.gun.a / 2))

    if math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - (goal.coord[1] + goal.b)) /
                 ((goal.coord[0] + goal.a) - ult1.gun.coord[0] - ult1.gun.a / 2)) > 0:
        phi2 = math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - (goal.coord[1] + goal.b)) /
                          ((goal.coord[0] + goal.a) - ult1.gun.coord[0] - ult1.gun.a / 2))
    else:
        phi2 = math.pi + math.atan((ult1.gun.coord[1] + ult1.gun.b / 2 - goal.coord[1]) /
                                    ((goal.coord[0] + goal.a) - ult1.gun.coord[0] - ult1.gun.a / 2))

    if phi2 <= alpha <= phi1:
        return goal.coord, True
    else:
        return (-100, -100), False


def anim_sm_ult1(ult1s, goals, anim_sm, time_anim_sm, color_anim_sm, rad_anim_sm, screen):
    '''Анимация sm в случае попадания ульты1 (ульты1, мишени, массив sm анимации, время действия анимации,
    начальный цвет анимации, радиус анимации, Э)'''
    color = [color_anim_sm[0], color_anim_sm[1], color_anim_sm[2]]
    T = time_anim_sm
    R = rad_anim_sm
    coff = 0
    for i in ult1s:
        for j in goals:
            coord, flag = chek_ult1(i, j)
            if flag:
                anim_sm.append([[coord[0] + j.a / 2, coord[1] + j.b / 2], time_anim_sm, color, rad_anim_sm])
                coff += 1
                goals.remove(j)
    for i in anim_sm:
        if i[1] > 0:
            i[1] -= 1
            circle(screen, i[2], i[0], R - i[3])
            i[2][1] -= 4
            i[3] = i[3] * (i[1] / T)
    return coff