import sys
from random import randint

import pygame

pygame.init()

screen_width: int = 800
screen_height: int = 600
screen_color = (31, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('My pygame')
clock = pygame.time.Clock()

rect_width: int = 100
rect_height: int = 200
# Разместим прямоугольник по центру
rect_x: float = screen_width / 2 - rect_width / 2
rect_y: float = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')
STEP = 10
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            elif event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            elif event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            elif event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP

    # screen.fill((255, 0, 0))
    screen.fill(screen_color)
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
    # clock.tick(1)  # события теперь 1 раз в секунду
