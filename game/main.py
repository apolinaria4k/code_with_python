import pygame
import pygame.locals
from pygame.locals import *


COLOR_SCREEN = (123, 65, 234)
COLOR_BALL = (56, 165, 54)
size = 640, 250
width, height = size

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("img/ball1.gif")
rect = ball.get_rect()
speed = [2, 2]

caption = "WELCOME"
pygame.display.set_caption(caption)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if pygame.key.get_pressed()[K_LEFT]:
        if rect.left > 0:
            speed = [-1, 0]
            rect = rect.move(speed)
        else:
            speed = [0, 0]
            rect = rect.move(speed)

    elif pygame.key.get_pressed()[K_RIGHT]:
        if rect.right < width:
            speed = [1, 0]
            rect = rect.move(speed)
        else:
            speed[0] = 0
            rect = rect.move(speed)

    elif pygame.key.get_pressed()[K_UP]:
        if rect.top > 0:
            speed = [0, -1]
            rect = rect.move(speed)
        else:
            speed = [0, 0]
            rect = rect.move(speed)

    elif pygame.key.get_pressed()[K_DOWN]:
        if rect.bottom < height:
            speed = [0, 1]
            rect = rect.move(speed)
        else:
            speed = [0, 0]
            rect = rect.move(speed)


    screen.fill(COLOR_SCREEN)
    pygame.draw.rect(screen, COLOR_BALL, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()


pygame.quit()