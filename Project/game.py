from function import *
from variabls import *

pygame.init()
screen = pygame.display.set_mode((parametrs[0], parametrs[1]))

new_image = pygame.image.load('image_1.png').convert_alpha()
image_1 = pygame.transform.scale(new_image, (parametrs[0], parametrs[1] - parametrs[2]))
new_image = pygame.image.load('image_2.png').convert_alpha()
image_2 = pygame.transform.scale(new_image, (a_goals, b_goals))
new_image = pygame.image.load('image_caliber.png').convert_alpha()
image_caliber = pygame.transform.scale(new_image, (a_calibers, b_calibers))
new_image = pygame.image.load('image_gun.png').convert_alpha()
image_gun = pygame.transform.scale(new_image, (a_gun, b_gun))
new_image = pygame.image.load('image_3.png').convert_alpha()
image_3 = pygame.transform.scale(new_image, (parametrs[0], parametrs[1]))
new_image = pygame.image.load('image_options.png').convert_alpha()
image_options = pygame.transform.scale(new_image, (a_options, b_options))
new_image = pygame.image.load('image_play.png').convert_alpha()
image_play = pygame.transform.scale(new_image, (a_play, b_play))
new_image = pygame.image.load('image_name.png').convert_alpha()
image_name = pygame.transform.scale(new_image, (a_name, b_name))
new_image = pygame.image.load('image_easy.png').convert_alpha()
image_easy = pygame.transform.scale(new_image, (a_easy, b_easy))
new_image = pygame.image.load('image_normal.png').convert_alpha()
image_normal = pygame.transform.scale(new_image, (a_normal, b_normal))
new_image = pygame.image.load('image_hard.png').convert_alpha()
image_hard = pygame.transform.scale(new_image, (a_hard, b_hard))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

goals = [] # массив мишеней
gun = Gun(a_gun, b_gun, speed_gun, parametrs, screen, DARK_RED, rasst_gr_gun) # создание пушки
bombs = [] # массив бомб
time = [] # массив времени зажатия для каждого выстрела
shots = [] # массив выстрелов
anim_sm = [] # массив маленькой анимации
color_anim_sm = [] # массив начальных цветов маленькой анимации
rockets = [] # массив рокет
calibers = [] # массив калибров
ult1s = []

# переменные, которые могут быть не определены
tick_shot = tick_shot
kolvo_rockets = kolvo_rockets
mean_ult_new = mean_ult_new
mean_ult = mean_ult
coord_mouse = coord_mouse
coord = coord
coord_prediction = coord_default

for i in range(k): # рандомное время появления бомбы каждой мишени в начале
    time.append(randint(time_min, time_max))
flag_update_rockets = True

time_caliber_new = 0

flag_1 = True
flag_2 = False
flag_game = False
flag_easy = True
flag_normal = False
flag_hard = False
flag_folstart_shot = True

while not finished:
    clock.tick(parametrs[3])

    '''Экран 1'''
    if flag_1:
        screen.blit(image_3, (0, 0))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEMOTION:
                coord = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord_mouse = event.pos

        if (coord_mouse[0] >= parametrs[0] / 2 - a_options / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_options / 2) and \
                (coord_mouse[1] >= y_options) and \
                (coord_mouse[1] <= y_options + b_options) and flag_1:
            coord_mouse = coord_default
            flag_2 = True
            flag_1 = False

        if (coord_mouse[0] >= parametrs[0] / 2 - a_play / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_play / 2) and \
                (coord_mouse[1] >= y_play) and \
                (coord_mouse[1] <= y_play + b_play):
            coord_mouse = coord_default
            flag_1 = False
            flag_game = True

        if (coord[0] >= parametrs[0] / 2 - a_options / 2) and \
                (coord[0] <= parametrs[0] / 2 + a_options / 2) and \
                (coord[1] >= y_options) and \
                (coord[1] <= y_options + b_options):
            screen.blit(image_options, (parametrs[0] / 2 - a_options / 2, y_options))
            rect(screen, WHITE, (parametrs[0] / 2 - a_options / 2 - thickness,
                                 y_options - thickness, a_options + 2 * thickness,
                                 b_options + 2 * thickness), thickness)
        else:
            screen.blit(image_options, (parametrs[0] / 2 - a_options / 2, y_options))

        if (coord[0] >= parametrs[0] / 2 - a_play / 2) and \
                (coord[0] <= parametrs[0] / 2 + a_play / 2) and \
                (coord[1] >= y_play) and \
                (coord[1] <= y_play + b_play):
            screen.blit(image_play, (parametrs[0] / 2 - a_play / 2, y_play))
            rect(screen, WHITE, (parametrs[0] / 2 - a_play / 2 - thickness,
                                 y_play - thickness, a_play + 2 * thickness,
                                 b_play + 2 * thickness), thickness)
        else:
            screen.blit(image_play, (parametrs[0] / 2 - a_play / 2, y_play))

        if flag_easy:
            screen.blit(image_easy, (parametrs[0] / 2 - a_level / 2, y_level))

        if flag_normal:
            screen.blit(image_normal, (parametrs[0] / 2 - a_level / 2, y_level))

        if flag_hard:
            screen.blit(image_hard, (parametrs[0] / 2 - a_level / 2, y_level))

        screen.blit(image_name, (parametrs[0] / 2 - a_name / 2, y_name))
    ''''''

    '''Экран 2'''
    if flag_2:
        screen.blit(image_3, (0, 0))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEMOTION:
                coord = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord_mouse = event.pos

        if (coord[0] >= parametrs[0] / 2 - a_easy / 2) and \
                        (coord[0] <= parametrs[0] / 2 + a_easy / 2) and \
                        (coord[1] >= y_easy) and \
                        (coord[1] <= y_easy + b_easy):
            screen.blit(image_easy, (parametrs[0] / 2 - a_easy / 2, y_easy))
            rect(screen, WHITE, (parametrs[0] / 2 - a_easy / 2 - thickness,
                             y_easy - thickness, a_easy + 2 * thickness,
                             b_easy + 2 * thickness), thickness)
        else:
            screen.blit(image_easy, (parametrs[0] / 2 - a_easy / 2, y_easy))

        if (coord[0] >= parametrs[0] / 2 - a_normal / 2) and \
                        (coord[0] <= parametrs[0] / 2 + a_normal / 2) and \
                        (coord[1] >= y_normal) and \
                        (coord[1] <= y_normal + b_normal):
            screen.blit(image_normal, (parametrs[0] / 2 - a_normal / 2, y_normal))
            rect(screen, WHITE, (parametrs[0] / 2 - a_normal / 2 - thickness,
                             y_normal - thickness, a_normal + 2 * thickness,
                             b_normal + 2 * thickness), thickness)
        else:
            screen.blit(image_normal, (parametrs[0] / 2 - a_normal / 2, y_normal))

        if (coord[0] >= parametrs[0] / 2 - a_hard / 2) and \
                        (coord[0] <= parametrs[0] / 2 + a_hard / 2) and \
                        (coord[1] >= y_hard) and \
                        (coord[1] <= y_hard + b_hard):
            screen.blit(image_hard, (parametrs[0] / 2 - a_hard / 2, y_hard))
            rect(screen, WHITE, (parametrs[0] / 2 - a_hard / 2 - thickness,
                             y_hard - thickness, a_hard + 2 * thickness,
                             b_hard + 2 * thickness), thickness)
        else:
            screen.blit(image_hard, (parametrs[0] / 2 - a_hard / 2, y_hard))

        if (coord_mouse[0] >= parametrs[0] / 2 - a_easy / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_easy / 2) and \
                (coord_mouse[1] >= y_easy) and \
                (coord_mouse[1] <= y_easy + b_easy):
            coord_mouse = coord_default
            flag_easy = True
            flag_normal = False
            flag_hard = False
            flag_1 = True
            flag_2 = False

        if (coord_mouse[0] >= parametrs[0] / 2 - a_normal / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_normal / 2) and \
                (coord_mouse[1] >= y_normal) and \
                (coord_mouse[1] <= y_normal + b_normal):
            coord_mouse = coord_default
            flag_easy = False
            flag_normal = True
            flag_hard = False
            flag_1 = True
            flag_2 = False

        if (coord_mouse[0] >= parametrs[0] / 2 - a_hard / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_hard / 2) and \
                (coord_mouse[1] >= y_hard) and \
                (coord_mouse[1] <= y_hard + b_hard):
            coord_mouse = coord_default
            flag_easy = False
            flag_normal = False
            flag_hard = True
            flag_1 = True
            flag_2 = False
    ''''''

    '''Экран игры'''
    if flag_game:
        screen.fill(BLACK) # Дисплей в цвет
        #screen.blit(image_1, (0, 0)) # Отображение картинки

        new_goal(goals, k, screen, RED, a_goals, b_goals, parametrs, speed_goals) # Создание мишеней
        tick_shot += 1 # Переменная всегда увеличивается, в случае активации ЛКМ, она сбрасывается до 0.
        time_caliber_new -= 1 # Переменная, отвечающая за перезарядку калибра

        '''Модуль обработки данных с клавиатуры и мыши'''
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.KEYDOWN: # Клавиатура
                if event.key == pygame.K_a and \
                        gun.coord[0] > 0: # Проверка нажатия a
                    nag_left = True
                if event.key == pygame.K_d and \
                        parametrs[0] - gun.coord[0] > gun.a: # Проверка нажатия d
                    nag_right = True
                if event.key == pygame.K_SPACE and time_caliber_new < 0: # Проверка нажатия space, запуск calibers
                    calibers.append(Caliber(a_calibers, b_calibers,
                                        speed_calibers, boost_calibers, screen, parametrs, gun))
                    time_caliber_new = time_caliber
                if event.key == pygame.K_LSHIFT and coord_prediction[1] <= parametrs[1] - parametrs[2] \
                        and mean_ult >= mean_level:
                    ult1s.append(Ult1(screen, coord_prediction, gun, thickness_ult1, parametrs, time_ult1))
                    mean_ult = 0
                    flag_update_rockets = True

            if event.type == pygame.MOUSEBUTTONDOWN: # Нажатие на клавиши мыши
                if event.button == 1:
                    coord_mouse = event.pos
                if coord_mouse != coord_default:
                    flag_folstart_shot = False
                if event.button == 1 and not flag_folstart_shot: # ЛКМ, время подготовки выстрела
                    tick_shot = 0
                if event.button == 3 and kolvo_rockets > 0: # ПКМ, ракеты
                    rockets.append(Rocket(gun, event.pos,
                                      rad_rockets, speed_rockets, g, screen, parametrs))
                    coord_prediction = event.pos
                    kolvo_rockets -= 1

            if event.type == pygame.MOUSEBUTTONUP: # Отпускание клавиш мыши
                if event.button == 1 and not flag_folstart_shot: # ЛКМ, выстрел
                    if tick_shot >= time_nag_limit:
                        shots.append(Shot(gun, event.pos, time_nag_limit,
                                      rad_shots, speed_shots, screen, g, parametrs))
                        tick_shot = 0
                    else:
                        shots.append(Shot(gun, event.pos, tick_shot, rad_shots, speed_shots, screen, g, parametrs))
                        tick_shot = 0
                if event.button == 3: # ПКМ, если True, то далее применяется функция off
                    for i in rockets:
                        i.flag = False

            if event.type == pygame.MOUSEMOTION: # Курсор
                coord_prediction = event.pos
        ''''''

        '''Модуль движения пушки вправо и влево'''
        nag_left = False
        nag_right = False
        if pygame.key.get_pressed()[pygame.K_a] and gun.coord[0] > 0:
            zag_left = True
        else:
            zag_left = False
        if pygame.key.get_pressed()[pygame.K_d] and parametrs[0] - gun.coord[0] > gun.a:
            zag_right = True
        else:
            zag_right = False
        if nag_left or zag_left:
            gun.coord -= [gun.speed, 0]
        if nag_right or zag_right:
            gun.coord += [gun.speed, 0]
        ''''''

        '''Модуль смены координат всех компонент программы'''
        napr_rocket(rockets, coord_prediction)
        napr_goals(goals)
        napr_bomb(bombs)
        napr_shots(shots)
        napr_caliber(calibers)
        ''''''

        '''Модуль маленькой анимации, также подсчет очков для набора ульты'''
        mean_ult_new += anim_sm_shot_and_rocket(shots, goals, anim_sm, time_anim_sm, YELLOW, rad_anim_sm, screen)
        mean_ult_new += anim_sm_shot_and_rocket(rockets, goals, anim_sm, time_anim_sm, YELLOW, rad_anim_sm, screen)
        mean_ult_new += anim_sm_caliber(calibers, goals, anim_sm, time_anim_sm, YELLOW, rad_anim_sm, screen)

        mean_ult += mean_ult_new  # Уровень ульты

        mean_ult_new += anim_sm_ult1(ult1s, goals, anim_sm, time_anim_sm, YELLOW, rad_anim_sm, screen)

        mean += mean_ult_new  # Кол-во уничтоженных мишеней
        mean_ult_new = 0
        ''''''

        '''Модуль отображения компонент программы'''
        displey_bomb(bombs, BLUE)
        displey_goals(goals, image_2, RED)
        displey_line(screen, WHITE, parametrs)
        displey_ult1(ult1s, RED)
        displey_caliber(calibers, GREEN, image_caliber)
        displey_shots(shots, WHITE)
        displey_rocket(rockets, YELLOW)
        displey_gun(gun, image_gun)
        displey_text(40, WHITE, (20, parametrs[1] - parametrs[2] + 20), 'Score', screen)
        displey_text(40, WHITE, (100, parametrs[1] - parametrs[2] + 20), str(mean), screen)
        displey_k_rockets(kolvo_rockets, screen, WHITE, rasst_gr,
                        rad_rockets_anim, rasst_rockets_anim, parametrs, width, width_caliber_ult)
        displey_level(mean_ult, screen, WHITE, parametrs,
                    width, height, rasst_gr, mean_level, thickness, DARK_GREEN, DARK_ORANGE, DARK_RED, width_caliber_ult)
        displey_update_caliber(time_caliber_new, time_caliber, rasst_gr, height_caliber_ult, width_caliber_ult,
                           screen, parametrs, DARK_GREEN, DARK_ORANGE, WHITE, thickness)
        ''''''

        '''Обновление ракет в случае достижения ульты'''
        if mean_ult == mean_level and flag_update_rockets:
            kolvo_rockets = mean_rockets
            flag_update_rockets = False
        ''''''

        '''Определение случайного времени между выстрелами мишени(случайное время вылета бомбы)'''
        for i in range(k):
            time[i] -= 1
            if time[i] <= 0 and len(goals) == k:
                bombs.append(Bomb(goals[i], gun, rad_bomb, speed_bomb, screen))
                time[i] = randint(time_min, time_max)
        ''''''

        '''Проверка попадания бомбы в пушку, если True, выход из цикла'''
        if chek_bombs(bombs, gun):
            finished = True
        ''''''

        '''Модуль удаления ненужных компонентов программы'''
        delete(rockets)
        delete(shots)
        delete(calibers)
        delete_bomb(bombs, parametrs)
        ''''''

        off(rockets, coord_prediction) # Проверка ракет на достижение курсора мыши
    ''''''

    pygame.display.update() # Обновление дисплея

pygame.quit()