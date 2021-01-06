import pygame
import random
import os
import sys
import time
from pygame.locals import *

FPS = 25
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (190, 190, 190)
RED = (155, 0, 0)
LRED = (175, 30, 30)
YELLOW = (155, 155, 0)
LYELLOW = (175, 175, 20)
GREEN = (0, 155, 0)
LGREEN = (30, 175, 20)
BLUE = (0, 0, 155)
LBLUE = (30, 30, 175)

COLORS = (GREEN, YELLOW, RED, BLUE)
LCOLORS = (LBLUE, LGREEN, LRED, LYELLOW)

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
    return None


def load_image(name, colorkey=None):
    fullname = os.path.join(r'c:\Users\user\PycharmProjects\Tetris', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def main():
    intro_text1 = ['Tetris']
    intro_text2 = ['Нажмите enter, чтобы начать']
    intro_text3 = ['',
                   'p - пауза',
                   'r - поворот фигуры по часовой стрелке',
                   'l - поворот фигуры против часовой стрелки',
                   'перемещение фигур осуществляется',
                   'стрелками: влево, вниз, вправо']
    last = ['GAME OVER']

    fon = pygame.transform.scale(load_image('Интро.png'), (500, 500))
    screen.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 180)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 110)
    text_coord = 40
    for line in intro_text1:
        string_rendered = font1.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 80
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in intro_text2:
        string_rendered = font2.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 180
        intro_rect.x = 110
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in intro_text3:
        string_rendered = font2.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 40
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

                elif event.key == K_UP or event.key == K_r:
                    now['turn'] = (now['turn'] + 1) % len(ALL_SHAPES[now['shape']])
                    if not falling(board, now):
                        now['turn'] = (now['turn'] - 1) % len(ALL_SHAPES[now['shape']])
                elif event.key == K_l:
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


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()