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

k = 3 # количество мишеней
time_min = 2 * parametrs[3] # минимальное время появления бомбы
time_max = 6 * parametrs[3] # максимальное время появления бомбы
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
mean_level = 7 # колчисетво попаданий, необходимых для достижения ульты
mean_rockets = 3 # максимальное количество ракет, при достижении ульты обновляется
kolvo_rockets = mean_rockets # количество ракет в определенный момент времени, готовых к выстрелу.
a_goals = 50 # ширина мишени
b_goals = 20 # высота мишени
speed_goals = 2 # скорость мишеней
a_gun = 60 # длина пушки
b_gun = 10 # высота пушки
speed_gun = 3 # скорость пушки
rad_rockets = 5 # радиус ракеты
speed_rockets = 3 # скорость ракеты
rad_shots = 5 # радиус выстрела
speed_shots = 0.12 # скорость выстрела
rad_bomb = 5 # радиус бомбы
speed_bomb = 0.01 # скорость бомбы
rad_rockets_anim = 5 # радиус анимации ракет
rasst_rockets_anim = 10 # расстояние между анимацией ракет
a_calibers = 4 # ширина калибра
b_calibers = 10 # длина калибра
boost_calibers = 1.02 # ускорение калибра
speed_calibers = 4 # начальная скорость калибра
time_ult1 = 0.25 * parametrs[3] # время действия первой ульты
thickness_ult1 = 2 # ширина первой ульты
time_caliber = 15 * parametrs[3] # время перезарядки калибра
height_caliber_ult = 100 # высота прямоугольника перезарядки калибра
width_caliber_ult = 20 # ширина треугольника перезарядки калибра
rasst_gr_gun = 10 # расстояние пушки до нижней границы
coord_default = (-100, -100)

'''Э'''
thickness = 3

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

coord_default = (-100, -100)
coord = coord_default
coord_mouse = coord_default
''''''
