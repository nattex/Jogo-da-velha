# -*- coding: utf-8 -*-
"""jogodaVelha

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QwxKQQy_qvtEQbb9h33f4YTuB7gOQ4er
"""

import pygame
import math
import panda as pd

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0, 0, 255)
cinza = (150,150,150)

window = pg.display.set_mode((1000,600))
window.fill(branco)

pg.font.init()
fonte = pg.font.SysFont("Comic Sans MS", 30)

board_array = [['n','n','n'],
               ['n','n','n'],
               ['n','n','n']]

click_last_status = 0
click_on_off = 0
click_position_x = -1
click_position_y = -1

X_or_O_turn = 'x'

end_game = 0

def grade_do_tabuleiro(window):
    pg.draw.line(window, preto, (205,0), (205,600), 10)
    pg.draw.line(window, preto, (405,0), (405,600), 10)
    pg.draw.line(window, preto, (0, 205), (600,205), 10)
    pg.draw.line(window, preto, (0,405), (600,405), 10)

def click_logic(click_on_off,click_last_status,x,y):
    if click[0] == 0 and click_last_status == 1:
        click_on_off = 1
        x = (math.ceil(mouse[0] / 200) -1)
        y = (math.ceil(mouse[1] / 200) -1)
    elif click[0] == 0 and click_last_status == 0:
        click_on_off = 0
        x = -1
        y = -1
    return click_on_off, click_last_status,x,y

def drawn_selected_cell(window, board_array):
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] == 'x':
                jogador_x(window, n, nn)
            elif board_array[nn][n] == 'o':
                jogador_o(window, n. nn)
            else:
                pass

def board_array_data(board_array,X_or_turn, end_game,x,y):
    if x < 3 and y < 3:
        if X_or_O_turn == 'x' and board_array[y][x] == 'n' and x != -1 and y != -1 and end_game == 0:
            board_array[y][x] = 'x'
            X_or_O_turn = 'o'
        if X_or_O_turn == 'o' and board_array[y][x] == 'n' and x != -1 and y != -1 and end_game == 0:
            board_array[y][x] = 'x'
            X_or_O_turn = 'o'
    return board_array, X_or_O_turn

def win_line(window, board_array, end_game, X_or_O_turn):
    if board_array[0][0] == 'x' and board_array[0][1] == 'x' and board_array[0][2] == 'x' \
    or  board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
          pg.draw.line(window, verde, (30,100), (570,100), 10)
          end_game = 1
          X_or_O_turn = 'x'

    elif  board_array[1][0] == 'x' and board_array[1][1] == 'x' and board_array[1][2] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (30,300), (570,300), 10)
          end_game = 1
          X_or_O_turn = 'x'

    elif  board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x' \
    or  board_array[2][0] == 'o' and board_array[2][1] == 'o' and board_array[2][2] == 'o':
          pg.draw.line(window, verde, (30,500), (100,580), 10)
          end_game = 1
          X_or_O_turn = 'x'
        
    elif  board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][0] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (100,30), (570,300), 10)
          end_game = 1
          X_or_O_turn = 'x'
    
    elif  board_array[0][1] == 'x' and board_array[1][1] == 'x' and board_array[2][1] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (300,30), (300,580), 10)
          end_game = 1
          X_or_O_turn = 'x'

    elif  board_array[0][2] == 'x' and board_array[1][2] == 'x' and board_array[2][2] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (500,30), (500,580), 10)
          end_game = 1
          X_or_O_turn = 'x'
        
    elif  board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (30,30), (580,580), 10)
          end_game = 1
          X_or_O_turn = 'x'

    elif  board_array[2][0] == 'x' and board_array[1][1] == 'x' and board_array[0][2] == 'x' \
    or  board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
          pg.draw.line(window, verde, (580,30), (30,580), 10)
          end_game = 1
          X_or_O_turn = 'x'
        
        
    



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()


    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    click = pg.mouse.get_pressed()


    grade_do_tabuleiro(window)
    click_on_off, click_last_status, click_position_x, click_position_y = click_logic(click_on_off,click_last_status, click_position_x, click_position_y)
    drawn_selected_cell(window, board_array)
    board_array, X_or_O_turn = board_array_data(board_array,X_or_turn, end_game, click_position_x, click_position_y)
    end_game, X_or_O_turn = win_line(window, board_array, end_game, X_or_O_turn)

    if click[0] == 1:
        click_last_status = 1
    else:
        click_last_status = 0

    pg.display.update()