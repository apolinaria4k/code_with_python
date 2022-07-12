import math
import turtle
import pygame
import pygame.locals
from pygame.locals import *
from tkinter import *


WHITE = (225, 225, 225)
size = (640, 640)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

caption = "WELCOME"
pygame.display.set_caption(caption)
screen.fill(WHITE)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_l:

                def xt(t):
                    return 16 * math.sin(t) ** 3


                def yt(t):
                    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)


                t = turtle.Turtle()
                t.speed(500)
                turtle.colormode(255)
                turtle.Screen().bgcolor(0, 0, 0)

                for i in range(500):
                    t.goto((xt(i) * 20, yt(i) * 20))
                    t.pencolor(146, 12, 247)
                    t.goto(0, 0)

                t.hideturtle()
                turtle.update()
                turtle.mainloop()

pygame.quit()