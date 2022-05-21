from cProfile import label
from turtle import Screen
import pygame
from pygame import mixer
from pyparsing import White
pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128,)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker of Moon')
label_front = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer= pygame.time.Clock()

run = True
while run:
    timer.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()

