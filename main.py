import pygame
from pygame.draw import *

pygame.init()
fps = 30
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
# здесь будут рисоваться фигуры
rect(screen, (255, 0, 255), (100,100,200,200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])

polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

# после чего, чтобы они отобразились на экране, экран нужно обновить:

# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
pygame.display.update()
finished = False
while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()