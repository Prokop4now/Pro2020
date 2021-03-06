import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
with open("WinUzers.txt", mode="r") as record_user_table:
    record = record_user_table.read().split()
    print('ЛУЧШИЙ ИГРОК ' + record[0] + ' набрал ' + record[1] + 'очков', sep=' ')

NAME = input("введите ваше имя:")

screen = pygame.display.set_mode((700, 700))
count_win = 0
count_lose = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
INITIAL_SCREEN_COLOR = (127, 180, 240)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def figur():
    """рисует  новый квадрат"""
    x_rect1 = randint(100, 600)
    x_rect2 = x_rect1 + 50
    y_rect1 = randint(100, 600)
    y_rect2 = y_rect1 + 50
    color = (0, 0, 0)
    rect(screen, color, (x_rect1, y_rect1, x_rect1+50, y_rect1+50))


# def click_new():
#     """возвращает True если клик вписывается в окружнонового шарика сть """
#     print(x_new, y_new, r_new)
#     """координаты круга"""
#     print(event.pos)
#     """координаты клика"""
#     x1_new, y2_new = event.pos
#     return ((x_new - x1_new)**2 + (y_new - y2_new)**2)**0.5 <= r


def click():
    """возвращает True если клик вписывается в окружность"""
    print(x, y, r)
    """координаты круга"""
    print(event.pos)
    """координаты клика"""
    x1, y2 = event.pos
    return ((x - x1) ** 2 + (y - y2) ** 2) ** 0.5 <= r


def new_ball():
    '''
    рисует новый шарик
    '''
    global x, y, r
    x = randint(100, 600)
    y = randint(100, 600)
    r = randint(10, 70)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


screen.fill(INITIAL_SCREEN_COLOR)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

change_figur = randint(2, 10)
cycle = 0

while not finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()
            if click() is True:
                count_win += 1
                print(count_win)
            else:
                count_lose += 1
        elif count_lose == 3:
            finished = True

    if cycle < change_figur:
        new_ball()
        pygame.display.update()
        screen.fill(INITIAL_SCREEN_COLOR)
        cycle += 1
    else:
        figur()
        pygame.display.update()
        screen.fill(INITIAL_SCREEN_COLOR)
        cycle = 0
        change_figur = randint(2, 10)



print("Вы проиграли, набрали очков - ", count_win)

if count_win > int(record[1]):
    print('ВЫ РЕКОРДСМЕН')
    with open("WinUzers.txt", mode="w") as best_user_table:
        best_user_table.write(NAME + ' ' + str(count_win))

pygame.quit()
