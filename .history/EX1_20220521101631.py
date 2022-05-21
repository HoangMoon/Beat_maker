
from turtle import Screen, left
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
# vẽ giao diện 
def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT- 200, WIDTH, 200], 5)




run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()

