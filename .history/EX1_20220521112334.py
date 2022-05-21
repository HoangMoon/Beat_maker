
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
beats = 8
instruments =6


# vẽ giao diện 
def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT- 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_front.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_front.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    floor_text = label_front.render('Bass Drum', True, white)
    screen.blit(floor_text, (15, 230))
    crash_text = label_front.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_front.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_text = label_front.render('Floor Tom', True, white)
    screen.blit(floor_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
    
    for i in range(beats):
        for j in range(instruments):
            rect =pygame.draw.rect(screen, gray, [i * ((WIDTH - 200) // beats) + 200, (j *100), ((WIDTH - 200)// beats), ((HEIGHT - 200)//instruments)], 5, 5)



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

