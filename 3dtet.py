## This is the official 3 dimensional version

import pygame
import random

pygame.font.init() #Initializes PyGame

# GLOBALS VARIABLES
s_width = 800 #Width
s_height = 700 #Height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

#Orientation - XYZ, Z is the height

#Defining the shapes

I=[(-1,0,0),(0,0,0),(1,0,0),(2,0,0)]
L=[(-1,0,0),(0,0,0),(1,0,0),(-1,1,0)]
T=[(-1,0,0),(0,0,0),(1,0,0),(0,1,0)]
S=[(-1,0,0),(0,0,0),(0,1,0),(1,1,0)]
O=[(0,0,0),(1,0,0),(0,1,0),(1,1,0)]
A=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
B=[(0,0,0),(1,0,0),(0,1,0),(1,0,1)]
C=[(0,0,0),(1,0,0),(0,1,0),(0,1,1)]

SHAPES = [I,L,T,S,O,A,B,C]

#Defining the colors

COLORS = [(0,255,255),(0,0,255),(128,0,255),(255,0,0),(255,255,0),(255,128,0),(0,255,0),(255,0,255)]

ROTATION_MATRIX = {
"X+": [[1,0,0],[0,0,-1],[0,1,0]], ##x anticlockwise
"X-": [[1,0,0],[0,0,1],[0,-1,0]], ##x clockwise
"Y+": [[0,0,1],[0,1,0],[-1,0,0]], ##y anticlockwise
"Y-": [[0,0,-1],[0,1,0],[1,0,0]], ##y clockwise
"Z+": [[0,-1,0],[1,0,0],[0,0,1]], ##z anticlockwise
"Z-": [[0,1,0],[-1,0,0],[0,0,1]] ##z clockwise
}

class PIECE(object): ##A piece object
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shapeType): ## Initialization
        self.x = column
        self.y = row
        self.shape = SHAPES[shapeType] #shape
        self.color = COLORS[shapeType] #color

##Game object

class GAME(object):
    def __init__(self, level):  ## Initialization
        self.grid = [[[(0,0,0) for x in range(6)] for x in range(6)] for x in range(12)] #empty grid start
        self.level = level #usually level 1
        self.score=0
        self.mult=0
        self.currentPiece = PIECE(random.randint(0,7)) #current piece
        self.nextPieces = [PIECE(random.randint(0,7)) for x in range(3)] #next piece in sequence

def collisionDetection(grid, piece):



