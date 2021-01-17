import pygame
import random
import os
import sys
import time
from pygame.locals import *
import sqlite3

FPS = 25
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (190, 190, 190)
RED = (255, 0, 0)
LRED = (220, 20, 60)
YELLOW = (255, 140, 0)
LYELLOW = (255, 165, 0)
GREEN = (50, 205, 50)
LGREEN = (154, 205, 50)
BLUE = (30, 144, 255)
LBLUE = (0, 191, 255)

COLORS = (GREEN, YELLOW, RED, BLUE)
LCOLORS = (LGREEN, LYELLOW, LRED, LBLUE)

DOWN = 0.1
SIDE = 0.15

SHAPE_WIDTH = 5
SHAPE_HEIGHT = 5

POINT = '.'
FIELD = 20  # занимаемое фигурой место (фигура всегда состоит из 4 элементов)
FH = 20
FW = 10
HIGH = 50
LEFTSIDE = 30

SHAPE_1 = [['.....',
            '.....',
            '..OO.',
            '.OO..',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '...O.',
            '.....']]

SHAPE_2 = [['.....',
            '.....',
            '.OO..',
            '.OO..',
            '.....']]

SHAPE_3 = [['.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '..OO.',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....'],
           ['.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....']]

SHAPE_4 = [['.....',
            '.....',
            '.OO..',
            '..OO.',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....']]

SHAPE_5 = [['.....',
            '.O...',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '...O.',
            '.....'],
           ['.....',
            '..O..',
            '..O..',
            '.OO..',
            '.....'],
           ['.....',
            '..OO.',
            '..O..',
            '..O..',
            '.....']]

SHAPE_6 = [['.....',
            '..O..',
            '.OOO.',
            '.....',
            '.....'],
           ['.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'],
           ['.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....']]

SHAPE_7 = [['..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'],
           ['.....',
            '.....',
            'OOOO.',
            '.....',
            '.....']]

ALL_SHAPES = {'ONE': SHAPE_1,
              'TWO': SHAPE_2,
              'THREE': SHAPE_3,
              'FOUR': SHAPE_4,
              'FIVE': SHAPE_5,
              'SIX': SHAPE_6,
              'SEVEN': SHAPE_7}

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 180)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 110)


def print_text(text):
    text_disp, text_rect = parameter(text, font3, WHITE)
    text_rect.center = (247, 247)
    screen.blit(text_disp, text_rect)
    while check_key() == None:
        pygame.display.update()
        clock.tick()


def parameter(text, font, color):
    disp = font.render(text, True, color)
    return disp, disp.get_rect()


def check_key():
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN or event.type == KEYUP:
            return event.key
    return is_quit()


def load_image(name, colorkey=None):
    fullname = os.path.join(r'materials', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def main():
    intro_text1 = ['Tetris']
    intro_text2 = ['Нажмите enter, чтобы начать']
    intro_text3 = ['',
                   '• p - пауза',
                   '• стрелка вверх - поворот фигуры по',
                   'часовой стрелке',
                   '• / - поворот фигуры против часовой стрелки',
                   '• перемещение фигур осуществляется',
                   'стрелками: влево, вниз, вправо']
    last = ['GAME OVER']

    fon = pygame.transform.scale(load_image('Интро.png'), (500, 500))
    screen.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 180)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 110)
    text_coord = 30
    for line in intro_text1:
        string_rendered = font1.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 35
        intro_rect.x = 80
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in intro_text2:
        string_rendered = font2.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 160
        intro_rect.x = 110
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in intro_text3:
        string_rendered = font2.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.load('tetris_sound.mp3')
                pygame.mixer.music.play(-1)
                play()
                pygame.mixer.music.stop()
                fon = pygame.transform.scale(load_image('Интро.png'), (500, 500))
                screen.blit(fon, (0, 0))
                for line in last:
                    string_rendered = font3.render(line, 1, WHITE)
                    intro_rect = string_rendered.get_rect()
                    intro_rect.top = 200
                    intro_rect.x = 20
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)

        pygame.display.flip()
        clock.tick(FPS)


def play():
    board = board_creation()
    score = 0
    con = sqlite3.connect(r'materials\topscore.db')
    cur = con.cursor()
    tops = cur.execute("""SELECT top FROM tabl
                WHERE id=1""").fetchall()
    for elem in tops:
        tops = elem[0]
    con.close()
    move_left = False
    move_down = False
    move_right = False
    ld = time.time()  # движение вниз
    ls = time.time()  # движение в сторону
    lf = time.time()  # падение
    frequency = how_often_fall(score)
    now = new_figure()
    next = new_figure()

    while True:
        if now == None:  # если нет падающей фигуры на поле
            now = next
            next = new_figure()
            lf = time.time()

            if not falling(board, now):
                return

        is_quit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_p:
                    pygame.mixer.music.stop()
                    fon = pygame.transform.scale(load_image('Интро.png'), (500, 500))
                    screen.blit(fon, (0, 0))
                    print_text('Paused')
                    pygame.mixer.music.play(-1)
                    lf = time.time()
                    ld = time.time()
                    ls = time.time()
                elif event.key == K_LEFT:
                    move_left = False
                elif event.key == K_RIGHT:
                    move_right = False
                elif event.key == K_DOWN:
                    move_down = False

            elif event.type == KEYDOWN:
                if event.key == K_LEFT and falling(board, now, field_x=-1):
                    now['x'] -= 1
                    move_left = True
                    move_right = False
                    ls = time.time()

                elif event.key == K_DOWN:
                    move_down = True
                    if falling(board, now, field_y=1):
                        now['y'] += 1
                    ld = time.time()

                elif event.key == K_RIGHT and falling(board, now, field_x=1):
                    now['x'] += 1
                    move_right = True
                    move_left = False
                    ls = time.time()

                elif event.key == K_UP:
                    now['turn'] = (now['turn'] + 1) % len(ALL_SHAPES[now['shape']])
                    if not falling(board, now):
                        now['turn'] = (now['turn'] - 1) % len(ALL_SHAPES[now['shape']])
                elif event.key == K_SLASH:
                    now['turn'] = (now['turn'] - 1) % len(ALL_SHAPES[now['shape']])
                    if not falling(board, now):
                        now['turn'] = (now['turn'] + 1) % len(ALL_SHAPES[now['shape']])

                elif event.key == K_SPACE:
                    move_down = False
                    move_left = False
                    move_right = False
                    for i in range(1, FH):
                        if not falling(board, now, field_y=i):
                            break
                    now['y'] += i - 1

        if (move_left or move_right) and time.time() - ls > SIDE:
            if move_left and falling(board, now, field_x=-1):
                now['x'] -= 1
            elif move_right and falling(board, now, field_x=1):
                now['x'] += 1
            ls = time.time()

        if move_down and time.time() - ld > DOWN and falling(board, now, field_y=1):
            now['y'] += 1
            ld = time.time()

        if time.time() - lf > frequency:
            if not falling(board, now, field_y=1):
                append_f(board, now)
                score += del_line(board)
                con = sqlite3.connect(r'materials\topscore.db')
                cur = con.cursor()
                if tops < score:
                    tops = cur.execute("""UPDATE tabl
                            SET top = top + 1
                            WHERE id=1""").fetchall()
                    tops = cur.execute("""SELECT top FROM tabl
                                WHERE id=1""").fetchall()
                    for elem in tops:
                        tops = elem[0]
                else:
                    tops = cur.execute("""SELECT top FROM tabl
                                WHERE id=1""").fetchall()
                    for elem in tops:
                        tops = elem[0]
                con.commit()
                con.close()
                frequency = how_often_fall(score)
                now = None
            else:
                now['y'] += 1
                lf = time.time()

        screen.fill(BLACK)
        set_board(board)
        print_score(score)
        print_topscore(tops)
        set_next(next)

        if now != None:
            set_figure(now)

        pygame.display.update()
        clock.tick(FPS)


def board_creation():
    board = []
    for i in range(500):
        board.append([POINT] * 500)
    return board


def new_figure():
    shape = random.choice(list(ALL_SHAPES.keys()))
    new = {'shape': shape,
           'color': random.randint(0, 3),
           'turn': random.randint(0, len(ALL_SHAPES[shape]) - 1),
           'x': 0,
           'y': -2}
    return new


def set_board(board):
    pygame.draw.rect(screen, WHITE, (LEFTSIDE - 3, HIGH - 7, (FW * FIELD) + 8, (FH * FIELD) + 8), 5)
    pygame.draw.rect(screen, BLACK, (LEFTSIDE, HIGH, FIELD * FW, FIELD * FH))
    for x in range(FW):
        for y in range(FH):
            set_field(x, y, board[x][y])


def set_next(figure):
    next_look = font2.render('Next:', True, WHITE)
    next_rect = next_look.get_rect()
    next_rect = (290, 140)
    screen.blit(next_look, next_rect)
    set_figure(figure, pix_x=290, pix_y=190)


def xy_pix(fx, fy):
    return (LEFTSIDE + (fx * FIELD)), (HIGH + (fy * FIELD))


def set_field(fx, fy, color, pix_x=None, pix_y=None):
    if color == POINT:
        return
    if pix_x == None and pix_y == None:
        pix_x, pix_y = xy_pix(fx, fy)
    pygame.draw.rect(screen, COLORS[color], (pix_x + 1, pix_y + 1, FIELD - 1, FIELD - 1))
    pygame.draw.rect(screen, LCOLORS[color], (pix_x + 1, pix_y + 1, FIELD - 4, FIELD - 4))
            
            
def print_score(score):
    score_look = font2.render('Score: %s' % score, True, WHITE)
    score_rect = score_look.get_rect()
    score_rect = (290, 90)
    screen.blit(score_look, score_rect)
    
    
def del_line(board):
    y = FH - 1
    n = 0
    while y >= 0:
        if done(board, y):
            for py in range(y, 0, -1):
                for x in range(FW):
                    board[x][py] = board[x][py-1]
            for x in range(FW):
                board[x][0] = POINT
            n += 1
        else:
            y -= 1
    return n


def done(board, y):
    for x in range(FW):
        if board[x][y] == POINT:
            return False
    return True


def append_f(board, figure):
    for x in range(SHAPE_WIDTH):
        for y in range(SHAPE_HEIGHT):
            if ALL_SHAPES[figure['shape']][figure['turn']][y][x] != POINT:
                board[x + figure['x']][y + figure['y']] = figure['color']
                

def set_figure(figure, pix_x=None, pix_y=None):
    set_shape = ALL_SHAPES[figure['shape']][figure['turn']]

    if pix_x == None and pix_y == None:
        pix_x, pix_y = xy_pix(figure['x'], figure['y'])

    for x in range(SHAPE_WIDTH):
        for y in range(SHAPE_HEIGHT):
            if set_shape[y][x] != POINT:
                set_field(None, None, figure['color'], pix_x + (x * FIELD), pix_y + (y * FIELD))
                

def falling(board, figure, field_x=0, field_y=0):
    for x in range(SHAPE_WIDTH):
        for y in range(SHAPE_HEIGHT):
            above = y + figure['y'] + field_y < 0
            if above or ALL_SHAPES[figure['shape']][figure['turn']][y][x] == POINT:
                continue
            if not within_the_board(x + figure['x'] + field_x, y + figure['y'] + field_y):
                return False
            if board[x + figure['x'] + field_x][y + figure['y'] + field_y] != POINT:
                return False
    return True


def is_quit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)
        
        
def within_the_board(x, y):
    return x >= 0 and x < FW and y < FH


def how_often_fall(score):
    frequency = 0.27 - ((int(score / 10) + 1) * 0.02)
    return frequency


def print_topscore(tops):
    score_look = font2.render('Topscore: %s' % tops, True, WHITE)
    score_rect = score_look.get_rect()
    score_rect = (290, 40)
    screen.blit(score_look, score_rect)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()