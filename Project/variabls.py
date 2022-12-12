# главные параметры - ГП (ширина, высота, высота линии от низа, FPS)
parametrs = [1000, 600, 200, 60]

# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_ORANGE = (255, 140, 0)
DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
ORANGE = (255, 157, 10)

''''''

video_death = "C:/Users/User/Downloads/001.mp4"

parametrs3_hard = 150

k_1 = 3
k_2 = 5
k_3 = 7

time_max_1 = 6 * parametrs[3]
time_max_2 = 6 * parametrs[3]
time_max_3 = 5 * parametrs[3]
time_max = time_max_1

mean_level_easy = 6
mean_level_normal = 8
mean_level_hard = 10
mean_level = mean_level_easy

mean_rockets_easy = 5
mean_rockets_normal = 4
mean_rockets_hard = 3
mean_rockets = mean_rockets_easy

speed_goals_easy = 2
speed_goals_normal = 2
speed_goals_hard = 3
speed_goals = speed_goals_easy

speed_bomb_easy = 2.5
speed_bomb_normal = 3
speed_bomb_hard = 3.5
speed_bomb = speed_bomb_easy

time_caliber_easy = 10 * parametrs[3]
time_caliber_normal = 15 * parametrs[3]
time_caliber_hard = 20 * parametrs[3]
time_caliber = time_caliber_easy

a_goals_easy = 50
a_goals_normal = 45
a_goals_hard = 40
a_goals = a_goals_easy

b_goals_easy = 20
b_goals_normal = 18
b_goals_hard = 16
b_goals = b_goals_easy

mean_level_1_stop = 20
mean_level_2_stop = 25
mean_level_3_stop = 30
''''''

k = k_1 # количество мишеней
time_min = 2 * parametrs[3] # минимальное время появления бомбы
g = 0.05 # ускорение свободного падения (УСП)
time_anim_sm = int(0.4 * parametrs[3] // 1) # время показа маленькой анимации
tick_shot = 0 # вначале переменная равна нулю, дальше показывает время зажатия ЛКМ для выстрела
time_nag_limit = 2 * parametrs[3] # максимальное время зажатия ЛКМ, в случае, если время больше данного,
                                                                            # то используется time_nag_limit
mean = 0 # количество попаданий, в начале mean = 0
mean_ult_new = 0
mean_ult = 0 # количество шкал ульты, не превосходит mean_level
rad_anim_sm = 20 # радиус маленькой анимации
height = 10 # высота одной шкалы прямоугольника ульты
width = 30 # ширина прямоугольника ульты
thickness = 2 # толщина прямоугольника ульты и прямоугольника калибра
rasst_gr = 10 # расстояние от прямоугольника ульты попаданий до границ (справа)
kolvo_rockets = mean_rockets # количество ракет в определенный момент времени, готовых к выстрелу.
a_gun = 60 # длина пушки
b_gun = 20 # высота пушки
speed_gun = 3 # скорость пушки
rad_rockets = 5 # радиус ракеты
speed_rockets = 3 # скорость ракеты
rad_shots = 5 # радиус выстрела
speed_shots = 0.12 # скорость выстрела
rad_bomb = 5 # радиус бомбы
rad_rockets_anim = 5 # радиус анимации ракет
rasst_rockets_anim = 10 # расстояние между анимацией ракет
a_calibers = 4 # ширина калибра
b_calibers = 10 # длина калибра
boost_calibers = 1.02 # ускорение калибра
speed_calibers = 4 # начальная скорость калибра
time_ult1 = 0.25 * parametrs[3] # время действия первой ульты
thickness_ult1 = 2 # ширина первой ульты
height_caliber_ult = 100 # высота прямоугольника перезарядки калибра
width_caliber_ult = 20 # ширина треугольника перезарядки калибра
rasst_gr_gun = 10 # расстояние пушки до нижней границы
coord_default = (-100, -100)

'''Э'''
a_name = 500
b_name = 100
y_name = 100

a_options = 200
b_options = 50
y_options = 300

a_play = 200
b_play = 50
y_play = 400

a_easy = 200
b_easy = 50
y_easy = (parametrs[1] - 3 * b_easy) / 4

a_normal = a_easy
b_normal = b_easy
y_normal = (parametrs[1] - 3 * b_easy) * 2 / 4 + b_easy

a_hard = a_easy
b_hard = b_easy
y_hard = (parametrs[1] - 3 * b_easy) * 3 / 4 + 2 * b_easy

a_level = 200
b_level = 50
y_level = 500

a_level_1 = 320
b_level_1 = 80
time_level_1 = 4 * parametrs[3]

a_level_2 = a_level_1
b_level_2 = b_level_1
time_level_2 = time_level_1

a_level_3 = a_level_1
b_level_3 = b_level_1
time_level_3 = time_level_1

frame_width = 20 # ширина черной рамки в заставке LEVEL

coord = coord_default
coord_mouse = coord_default
''''''
