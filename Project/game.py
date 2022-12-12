from function import *
from variabls import *

pygame.init()
screen = pygame.display.set_mode((parametrs[0], parametrs[1]))

new_image = pygame.image.load('image_1_new.jpg').convert_alpha()
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
new_image = pygame.image.load('level_1.png').convert_alpha()
image_level_1 = pygame.transform.scale(new_image, (a_level_1, b_level_1))
new_image = pygame.image.load('level_2.png').convert_alpha()
image_level_2 = pygame.transform.scale(new_image, (a_level_2, b_level_2))
new_image = pygame.image.load('level_3.png').convert_alpha()
image_level_3 = pygame.transform.scale(new_image, (a_level_3, b_level_3))
new_image = pygame.image.load('image_3.png').convert_alpha()
image_3 = pygame.transform.scale(new_image, (parametrs[0], parametrs[1]))
new_image = pygame.image.load('image_menu.png').convert_alpha()
image_menu = pygame.transform.scale(new_image, (a_menu, b_menu))
new_image = pygame.image.load('image_exit.png').convert_alpha()
image_exit = pygame.transform.scale(new_image, (a_exit_victory, b_exit_victory))
new_image = pygame.image.load('image_victory.png').convert_alpha()
image_victory = pygame.transform.scale(new_image, (a_victory, b_victory))

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

time_caliber_new = 0

flag_update_rockets = True
flag_1 = True
flag_2 = False
flag_game_1 = False
flag_game_2 = False
flag_game_3 = False
flag_easy = True
flag_normal = False
flag_hard = False
flag_level_screen_1 = False
flag_level_screen_2 = False
flag_level_screen_3 = False
flag_folstart_shot = True
flag_movement_gun_left = False
flag_movement_gun_right = False
flag_victory = False
l = 0

while not finished:
    clock.tick(parametrs[3])

    '''Экран 1'''
    if flag_1:
        mean = 0
        goals = []
        gun = Gun(a_gun, b_gun, speed_gun, parametrs, screen, DARK_RED, rasst_gr_gun)
        bombs = []
        shots = []
        anim_sm = []
        color_anim_sm = []
        rockets = []
        calibers = []
        ult1s = []
        mean_ult = 0
        kolvo_rockets = mean_rockets
        time_caliber_new = 0
        aboba = 0
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
            flag_level_screen_1 = True

        if (coord_mouse[0] >= parametrs[0] / 2 - a_exit / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_exit / 2) and \
                (coord_mouse[1] >= y_exit) and \
                (coord_mouse[1] <= y_exit + b_exit):
            finished = True

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

        if (coord[0] >= parametrs[0] / 2 - a_exit / 2) and \
                (coord[0] <= parametrs[0] / 2 + a_exit / 2) and \
                (coord[1] >= y_exit) and \
                (coord[1] <= y_exit + b_exit):
            screen.blit(image_exit, (parametrs[0] / 2 - a_exit / 2, y_exit))
            rect(screen, WHITE, (parametrs[0] / 2 - a_exit / 2 - thickness,
                                 y_exit - thickness, a_exit + 2 * thickness,
                                 b_exit + 2 * thickness), thickness)
        else:
            screen.blit(image_exit, (parametrs[0] / 2 - a_exit / 2, y_exit))

        if flag_easy:
            screen.blit(image_easy, (parametrs[0] / 2 - a_level / 2, y_level))

        if flag_normal:
            screen.blit(image_normal, (parametrs[0] / 2 - a_level / 2, y_level))

        if flag_hard:
            screen.blit(image_hard, (parametrs[0] / 2 - a_level / 2, y_level))

        screen.blit(image_name, (parametrs[0] / 2 - a_name / 2, y_name))

        if flag_easy:
            mean_level = mean_level_easy
            mean_rockets = mean_rockets_easy
            speed_goals = speed_goals_easy
            speed_bomb = speed_bomb_easy
            time_caliber = time_caliber_easy
            a_goals = a_goals_easy
            b_goals = b_goals_easy
            kolvo_rockets = mean_rockets_easy

        if flag_normal:
            mean_level = mean_level_normal
            mean_rockets = mean_rockets_normal
            speed_goals = speed_goals_normal
            speed_bomb = speed_bomb_normal
            time_caliber = time_caliber_normal
            a_goals = a_goals_normal
            b_goals = b_goals_normal
            kolvo_rockets = mean_rockets_normal

        if flag_hard:
            mean_level = mean_level_hard
            mean_rockets = mean_rockets_hard
            speed_goals = speed_goals_hard
            speed_bomb = speed_bomb_hard
            time_caliber = time_caliber_hard
            a_goals = a_goals_hard
            b_goals = b_goals_hard
            kolvo_rockets = mean_rockets_hard
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

    '''Level 1 screen'''
    if flag_level_screen_1:
        if l > time_level_1:
            flag_game_1 = True
            flag_level_screen_1 = False
            l = 0
        else:
            screen.fill(ORANGE)
            rect(screen, BLACK, (0, 0, parametrs[0], parametrs[1]), frame_width)
            screen.blit(image_level_1, (parametrs[0] / 2 - a_level_1 / 2, parametrs[1] / 2 - b_level_1 / 2))
            l += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    ''''''

    '''Level 2 screen'''
    if flag_level_screen_2:
        if l > time_level_2:
            flag_game_2 = True
            l = 0
            flag_level_screen_2 = False
        else:
            screen.fill(ORANGE)
            rect(screen, BLACK, (0, 0, parametrs[0], parametrs[1]), frame_width)
            screen.blit(image_level_2, (parametrs[0] / 2 - a_level_2 / 2, parametrs[1] / 2 - b_level_2 / 2))
            l += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    ''''''

    '''Level 3 screen'''
    if flag_level_screen_3:
        if l > time_level_3:
            flag_game_3 = True
            l = 0
            flag_level_screen_3 = False
        else:
            screen.fill(ORANGE)
            rect(screen, BLACK, (0, 0, parametrs[0], parametrs[1]), frame_width)
            screen.blit(image_level_3, (parametrs[0] / 2 - a_level_3 / 2, parametrs[1] / 2 - b_level_3 / 2))
            l += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    ''''''

    '''Экран игры'''
    if flag_game_1 or flag_game_2 or flag_game_3:
        screen.fill(BLACK) # Дисплей в цвет
        screen.blit(image_1, (0, 0)) # Отображение картинки

        new_goal(goals, k, screen, RED, a_goals, b_goals, parametrs, speed_goals) # Создание мишеней
        tick_shot += 1 # Переменная всегда увеличивается, в случае активации ЛКМ, она сбрасывается до 0.
        time_caliber_new -= 1 # Переменная, отвечающая за перезарядку калибра

        '''Модуль обработки данных с клавиатуры и мыши'''
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.KEYDOWN: # Клавиатура
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
    
        if pygame.key.get_pressed()[pygame.K_a] and gun.coord[0] > 0:
            zag_left = True
        else:
            zag_left = False
        if pygame.key.get_pressed()[pygame.K_d] and parametrs[0] - gun.coord[0] > gun.a:
            zag_right = True
        else:
            zag_right = False
        if zag_left:
            gun.coord -= [gun.speed, 0]
            flag_movement_gun_left = True
        else:
            flag_movement_gun_left = False
        if zag_right:
            gun.coord += [gun.speed, 0]
            flag_movement_gun_right = True
        else:
            flag_movement_gun_right = False
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
                bombs.append(Bomb(goals[i], gun, rad_bomb, speed_bomb, screen,
                                  flag_movement_gun_left, flag_movement_gun_right))
                time[i] = randint(time_min, time_max)
        ''''''

        '''Проверка попадания бомбы в пушку, если True, выход из цикла'''
        if chek_bombs(bombs, gun):
            video = cv2.VideoCapture(video_death)
            success, video_image = video.read()
            fps = video.get(cv2.CAP_PROP_FPS)
            
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

            flag_1 = True
            flag_game_1 = False
            flag_game_2 = False
            flag_game_3 = False
        ''''''

        '''Модуль удаления ненужных компонентов программы'''
        delete(rockets)
        delete(shots)
        delete(calibers)
        delete_bomb(bombs, parametrs)
        ''''''

        off(rockets, coord_prediction) # Проверка ракет на достижение курсора мыши

        if mean >= mean_level_1_stop and flag_game_1:
            flag_game_1 = False
            flag_level_screen_2 = True
            mean = 0
            goals = []
            gun = Gun(a_gun, b_gun, speed_gun, parametrs, screen, DARK_RED, rasst_gr_gun)
            bombs = []
            shots = []
            anim_sm = []
            color_anim_sm = []
            rockets = []
            calibers = []
            ult1s = []
            mean_ult = 0
            kolvo_rockets = mean_rockets
            time_caliber_new = 0
            k = k_2
            time_max = time_max_2
            coord = coord_default
            coord_mouse = coord_default
            for i in range(k):
                time.append(randint(time_min, time_max))

        if mean >= mean_level_2_stop and flag_game_2:
            flag_game_2 = False
            flag_level_screen_3 = True
            mean = 0
            goals = []
            gun = Gun(a_gun, b_gun, speed_gun, parametrs, screen, DARK_RED, rasst_gr_gun)
            bombs = []
            shots = []
            anim_sm = []
            color_anim_sm = []
            rockets = []
            calibers = []
            ult1s = []
            mean_ult = 0
            kolvo_rockets = mean_rockets
            time_caliber_new = 0
            k = k_3
            time_max = time_max_3
            coord = coord_default
            coord_mouse = coord_default
            for i in range(k):
                time.append(randint(time_min, time_max))

        if mean >= mean_level_3_stop and flag_game_3:
            flag_game_3 = False
            flag_victory = True
            mean = 0
            goals = []
            gun = Gun(a_gun, b_gun, speed_gun, parametrs, screen, DARK_RED, rasst_gr_gun)
            bombs = []
            shots = []
            anim_sm = []
            color_anim_sm = []
            rockets = []
            calibers = []
            ult1s = []
            mean_ult = 0
            kolvo_rockets = mean_rockets
            time_caliber_new = 0
            coord = coord_default
            coord_mouse = coord_default
    ''''''

    ''''''
    if flag_victory:
        screen.blit(image_3, (0, 0))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEMOTION:
                coord = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord_mouse = event.pos

        if (coord[0] >= parametrs[0] / 2 - a_menu / 2) and \
                (coord[0] <= parametrs[0] / 2 + a_menu / 2) and \
                (coord[1] >= y_menu) and \
                (coord[1] <= y_menu + b_menu):
            screen.blit(image_menu, (parametrs[0] / 2 - a_menu / 2, y_menu))
            rect(screen, WHITE, (parametrs[0] / 2 - a_menu / 2 - thickness,
                                 y_menu - thickness, a_menu + 2 * thickness,
                                 b_menu + 2 * thickness), thickness)
        else:
            screen.blit(image_menu, (parametrs[0] / 2 - a_menu / 2, y_menu))

        if (coord[0] >= parametrs[0] / 2 - a_exit_victory / 2) and \
                (coord[0] <= parametrs[0] / 2 + a_exit_victory / 2) and \
                (coord[1] >= y_exit_victory) and \
                (coord[1] <= y_exit_victory + b_exit_victory):
            screen.blit(image_exit, (parametrs[0] / 2 - a_exit_victory / 2, y_exit_victory))
            rect(screen, WHITE, (parametrs[0] / 2 - a_exit_victory / 2 - thickness,
                                 y_exit_victory - thickness, a_exit_victory + 2 * thickness,
                                 b_exit_victory + 2 * thickness), thickness)
        else:
            screen.blit(image_exit, (parametrs[0] / 2 - a_exit_victory / 2, y_exit_victory))

        screen.blit(image_victory, (parametrs[0] / 2 - a_victory / 2, y_victory))

        if (coord_mouse[0] >= parametrs[0] / 2 - a_menu / 2) and \
                    (coord_mouse[0] <= parametrs[0] / 2 + a_menu / 2) and \
                    (coord_mouse[1] >= y_menu) and \
                    (coord_mouse[1] <= y_menu + b_menu):
            coord_mouse = coord_default
            flag_1 = True
            flag_victory = False

        if (coord_mouse[0] >= parametrs[0] / 2 - a_exit_victory / 2) and \
                (coord_mouse[0] <= parametrs[0] / 2 + a_exit_victory / 2) and \
                (coord_mouse[1] >= y_exit_victory) and \
                (coord_mouse[1] <= y_exit_victory + b_exit_victory):
            coord_mouse = coord_default
            finished = True
    ''''''

    pygame.display.update() # Обновление дисплея

pygame.quit()