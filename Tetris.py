import pygame
import random
import os
import sys

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

COLOR_TEXT = WHITE
COLOR_WALL = BLUE
COLOR_FON = BLACK
COLOR_SHADOW = GRAY
COLORS = (GREEN, YELLOW, RED, BLUE)
LCOLORS = (LBLUE, LGREEN, LRED, LYELLOW)

DOWN = 0.1
SIDE = 0.15

SHAPE_WIDTH = 5
SHAPE_HEIGHT = 5

POINT = '.'
FIELD = 20
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