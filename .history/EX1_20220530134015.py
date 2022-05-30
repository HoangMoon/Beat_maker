
from math import fabs
from tkinter.ttk import Widget
from turtle import Screen, left
from numpy import delete
import pygame
from pygame import MOUSEBUTTONUP, mixer
from pyparsing import White
pygame.init()

#Color
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128,)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
dark_gray = (50, 50, 50)

#Screen property
WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker of Moon')
label_front = pygame.font.Font('Roboto-Bold.ttf', 32)
mediun_front = pygame.font.Font('Roboto-Bold.ttf', 24)


#Statement
fps = 60
timer= pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_list = [1 for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True
save_menu = False
load_menu = False
saved_beat = []
file = open('beat_save.txt', 'r')
for line in file:
    saved_beat.append(line)
beat_name = ''
typing = False

# load in sounds
hi_hat = mixer.Sound('sounds\hi hat.WAV')
snare = mixer.Sound('sounds\snare.WAV')
kick = mixer.Sound('sounds\kick.WAV')
crash = mixer.Sound('sounds\crash.WAV')
clap = mixer.Sound('sounds\clap.WAV')
tom = mixer.Sound('sounds\\tom.WAV')
pygame.mixer.set_num_channels(instruments * 3)



def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()


# vẽ giao diện 
def draw_grid(clicks, beat, actives):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT- 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_front.render('Hi Hat', True, colors[actives[0]])  #colors[active[0]]) == ? (màu dc gọi từ color(white, gray ,white)số ở active[i] là để xác định các dòng ko trùng lặp;có bn dòng sẽ tăng lên bấy nhiêu)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_front.render('Snare', True, colors[actives[1]])
    screen.blit(snare_text, (30, 130))
    floor_text = label_front.render('Bass Drum', True, colors[actives[2]])
    screen.blit(floor_text, (30, 230))
    crash_text = label_front.render('Crash', True, colors[actives[3]])
    screen.blit(crash_text, (30, 330))
    clap_text = label_front.render('Clap', True, colors[actives[4]])
    screen.blit(clap_text, (30, 430))
    floor_text = label_front.render('Floor Tom', True, colors[actives[5]])
    screen.blit(floor_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
    # load note
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                   color = green
                else:
                    color = dark_gray
            rect =pygame.draw.rect(screen, color,
                 [i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200) // beats) - 10,
                  ((HEIGHT - 200) // instruments) - 10], 0, 3)
            
            pygame.draw.rect(screen, gold,
                 [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)// beats), 
                 ((HEIGHT - 200) // instruments)], 5, 5)
            
            pygame.draw.rect(screen, black,
                 [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)// beats),
                  ((HEIGHT - 200) // instruments)], 2, 5)

            boxes.append((rect, (i, j)))
        
        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 200) // beats) + 200, 0, ((WIDTH -200) // beats), instruments * 100], 5 ,3 )
    return boxes

def draw_save_menu(beat_name, typing):
    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT] )
    menu_text = label_front.render('Save Menu: Enter a Name for Current Beat!! ', True, white)
    saving_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 150, HEIGHT *0.75, 300, 100], 0, 5)
    saving_text = label_front.render('Save the Beat', True, white)
    screen.blit(saving_text, (WIDTH // 2 - 100, HEIGHT * 0.75 + 30))
    screen.blit(menu_text, (400, 40))
    exit_btn = pygame.draw.rect(screen, gray, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_front.render('Close', True, white)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70)) 
    entry_rect = pygame.draw.rect(screen, gray, [400, 200, 600, 200], 5, 5)
    entry_text = label_front.render(f'{beat_name}', True, white)
    screen.blit(entry_text, (430, 250))
    return exit_btn, saving_btn, entry_rect


def draw_load_menu():
    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT] )
    menu_text = label_front.render('Load Menu: Give Me the Beat!! ', True, white)
    loading_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 200, HEIGHT *0.75, 200, 100], 0, 5)
    loading_text = label_front.render('Load the Beat', True, white)
    screen.blit(loading_text, (WIDTH // 2 - 70, HEIGHT * 0.75 + 30))
    delete_btn = pygame.draw.rect(screen, gray, [(WIDTH//2) - 500, HEIGHT * .75, 400, 100], 0, 5)
    delete_text = label_front.render('Drop the Beat', True, white)
    screen.blit(delete_text, ((WIDTH//2)-485, HEIGHT * .75 + 10))
    screen.blit(menu_text, (400, 40))
    exit_btn = pygame.draw.rect(screen, gray, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_front.render('Close', True, white)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))  
    return exit_btn, loading_btn, delete_btn



#Event Active
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
   
    boxes = draw_grid(clicked,active_beat,active_list)
    # load menu button
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT-150, 200, 100], 0, 5)
    play_text = label_front.render('Play/Pause', True, white)
    screen.blit(play_text, (70, HEIGHT-130))
    if playing:
        play_text2 = mediun_front.render('Playing', True, dark_gray)
    else :
        play_text2 = mediun_front.render('Pause', True, dark_gray)
    screen.blit(play_text2, (70, HEIGHT-100))
    
    #bpm stuff
    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpm_text = mediun_front.render('Beats Per Minute', True, white)
    screen.blit(bpm_text, (308, HEIGHT - 130))
    bpm_text2 = label_front.render(f'{bpm}', True, white)
    screen.blit(bpm_text2, (370, HEIGHT - 100))
    bpm_add_rect = pygame.draw.rect(screen, gray, [510, HEIGHT-150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, gray, [510, HEIGHT-100, 48, 48], 0, 5)
    add_text = mediun_front.render('+5', True, white)
    screen.blit(add_text, (520, HEIGHT - 140))
    sub_text = mediun_front.render('-5', True, white)
    screen.blit(sub_text, (520, HEIGHT - 90))
    
    #beats suff
    beat_rect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 200, 100], 5, 5)
    beat_text = mediun_front.render('Beats In Loop', True, white)
    screen.blit(beat_text, (612, HEIGHT - 130))
    beat_text2 = label_front.render(f'{beats}', True, white)
    screen.blit(beat_text2, (670, HEIGHT - 100))
    beat_add_rect = pygame.draw.rect(screen, gray, [810, HEIGHT-150, 48, 48], 0, 5)
    beat_sub_rect = pygame.draw.rect(screen, gray, [810, HEIGHT-100, 48, 48], 0, 5)
    add_text2 = mediun_front.render('+1', True, white)
    screen.blit(add_text2, (820, HEIGHT - 140))
    sub_text2 = mediun_front.render('-1', True, white)
    screen.blit(sub_text2, (820, HEIGHT - 90))

    # instruments react
    instruments_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instruments_rects.append(rect)

    # save and load stuff
    save_button = pygame.draw.rect(screen, gray, [900, HEIGHT - 150, 200, 48], 0, 5)
    save_text = label_front.render('Save Beat', True, white)
    screen.blit(save_text, (920, HEIGHT - 140))
    load_button = pygame.draw.rect(screen, gray, [900, HEIGHT - 100, 200, 48], 0, 5)
    load_text = label_front.render('Load Beat', True, white)
    screen.blit(load_text, (920, HEIGHT-90))
    #clear Board
    clear_button = pygame.draw.rect(screen, gray, [1150, HEIGHT - 150, 200, 100], 0, 5)
    clear_text = label_front.render('Clear All', True, white)
    screen.blit(clear_text, (1185, HEIGHT - 130))
    #save/load
    if save_menu:
        exit_button, saving_button, entry_reactangle = draw_save_menu(beat_name, typing)
    if load_menu:
        exit_button = draw_load_menu()

    if beat_changed:
        play_notes()
        beat_changed = False

    #event effect
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #box of beat
        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
            #control play/pause
        if event.type == pygame.MOUSEBUTTONUP  and not save_menu and not load_menu:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
                #control beat per minute
            if bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
        #number of beat loop
            if beat_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beat_add_rect.collidepoint(event.pos):
                beats -= 1
            elif beat_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            #clear button
            elif clear_button.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
            #save_button
            elif save_button.collidepoint(event.pos):
                save_menu = True
            elif load_button.collidepoint(event.pos):
                load_menu = True
            for i in range(len(instruments_rects)):
                if instruments_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1
        
                #all menu
        elif event.type == pygame.MOUSEBUTTONUP:
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True
                beat_name = ''
                typing = False
                #save beat menu
            elif entry_reactangle.collidepoint(event.pos):
                if typing:
                    typing = False
                elif not typing:
                    typing = True
                    #save beat in to file.txt
            elif saving_button.collidepoint(event.pos):
                file = open('beat_save.txt','w')
                saved_beat.append(f'\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                for i in range(len(saved_beat)):
                    file.write(str(saved_beat[i]))
                file.close()
                save_menu = False
                typing = False
                beat_name = ''



        if event.type == pygame.TEXTINPUT and typing:
            beat_name += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0 and typing:
                beat_name = beat_name[:-1]
 





    # event beat run
    beat_length = fps * 60 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats -1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True




    pygame.display.flip()
pygame.quit()

# 1:57:45

