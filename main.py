import pygame
from pygame.draw import *

pygame.init()
fps = 30
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


def draw_bear(surface, x, y, height, width, color):
    x_head = x
    y_head = y
    height_head = 0.2 * height
    width_head = height_head

    x_body = x - width_head//2
    y_body = y_head - height_head // 2
    body_height = 0.5 * height
    body_width = height_head * 2

    draw_head(surface, x_head, y_head, height_head, width_head, color)

    draw_body(surface, x_body, y_body, body_height, body_width, color)


def draw_head(surface, x, y, height, width, color):
    circle(surface,color, (x, y), height*2)


def draw_body(surface, x, y, height, width, color):
    ellipse(surface, color, (x, y, height, width))


draw_bear(screen, 250, 250, 100, 100, (200, 200, 200))

pygame.display.update()
finished = False
while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
