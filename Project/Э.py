from variabls import *
from function import *

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

pygame.init()
screen = pygame.display.set_mode((parametrs[0], parametrs[1]))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

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

flag_1 = True
flag_2 = False
flag_easy = True
flag_normal = False
flag_hard = False

while not finished:
    clock.tick(parametrs[3])

    if (coord_mouse[0] >= parametrs[0] / 2 - a_options / 2) and \
                        (coord_mouse[0] <= parametrs[0] / 2 + a_options / 2) and \
                        (coord_mouse[1] >= y_options) and \
                        (coord_mouse[1] <= y_options + b_options) and flag_1:
        coord_mouse = coord_default
        flag_2 = True
        flag_1 = False

    ''''''
    if flag_1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEMOTION:
                coord = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coord_mouse = event.pos

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
            screen.blit(image_normal, (parametrs[0] / 2 - a_level/ 2, y_level))

        if flag_hard:
            screen.blit(image_hard, (parametrs[0] / 2 - a_level / 2, y_level))

        screen.blit(image_name, (parametrs[0] / 2 - a_name / 2, y_name))
    ''''''

    ''''''
    if flag_2:
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

    pygame.display.update()
    screen.blit(image_3, (0, 0))