## This is the official 3 dimensional version

import pygame
import random

pygame.font.init()  # Initializes PyGame

# GLOBALS VARIABLES
s_width = 800  # Width
s_height = 700  # Height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# Orientation - XYZ, Z is the height

# Defining the shapes

I = [(-1, 0, 0), (0, 0, 0), (1, 0, 0), (2, 0, 0)]
L = [(-1, 0, 0), (0, 0, 0), (1, 0, 0), (-1, 1, 0)]
T = [(-1, 0, 0), (0, 0, 0), (1, 0, 0), (0, 1, 0)]
S = [(-1, 0, 0), (0, 0, 0), (0, 1, 0), (1, 1, 0)]
O = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
A = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
B = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 0, 1)]
C = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 1)]

SHAPES = [I, L, T, S, O, A, B, C]

# Defining the colors

COLORS = [(0, 255, 255), (0, 0, 255), (128, 0, 255), (255, 0, 0), (255, 255, 0), (255, 128, 0), (0, 255, 0),
          (255, 0, 255)]

''' L I N E A R   A L G E B R A'''

ROTATION_MATRIX = {
    "X+": [[1, 0, 0], [0, 0, -1], [0, 1, 0]],  ##x anticlockwise
    "X-": [[1, 0, 0], [0, 0, 1], [0, -1, 0]],  ##x clockwise
    "Y+": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],  ##y anticlockwise
    "Y-": [[0, 0, -1], [0, 1, 0], [1, 0, 0]],  ##y clockwise
    "Z+": [[0, -1, 0], [1, 0, 0], [0, 0, 1]],  ##z anticlockwise
    "Z-": [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]  ##z clockwise
}


def addVec(x, y):  # adding two vectors
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def negVec(x):  # negate a vector
    return (-x[0], -x[1], -x[2])


def dotProd(x, y):  # dot product for matrix mult
    return x[0] * y[0] + x[1] * y[1] + x[2] * y[2]


def matrixMult(M, v):  # multiple a vector by a matrix
    return (dotProd(M[0], v), dotProd(M[1], v), dotProd(M[2], v))


def rotVec(rot, v):  # rotate a vector
    return matrixMult(ROTATION_MATRIX[rot], v)

def getVecPos(v,grid):  # takes a vector v and fetch that position from the grid
    if (min(v[0],v[1],v[2])<0 or v[0]>=len(grid) or v[1]>=len(grid[0]) or v[2]>=len(grid[0][0])):  # checks if it is an invalid position in the grid
        return (-1,-1,-1)  # if it is, it returns a color vector of all -1's
    return grid[v[0]][v[1]][v[2]]

class PIECE(object):  ##A piece object
    rows = 20  # y
    columns = 10  # x

    def __init__(self, shapeType, pos=(0, 0, 0)):  ## Initialization
        self.pos = pos  # position
        self.shape = SHAPES[shapeType]  # shape
        self.color = COLORS[shapeType]  # color

    def toVectors(self):  # converts to a position list of 4 vectors
        return [addVec(self.shape[i], self.pos) for i in range(len(self.shape))]

    def canOverlap(self,grid):  # Check if it overlaps with the pieces or the wall
        for x in self.toVectors():
            vec = getVecPos(x,grid)
            if (vec != (0,0,0)):  # returns false if a colored block is occupied or the position is not included
                return False
        return True

    def collisionDetect(self,grid):  # If collision is with the wall, it nudges the piece
        nudgeMin = (0,0,0)  # for variables being too low
        Xsize = len(grid)
        Ysize = len(grid[0])
        Zsize = len(grid[0][0])
        nudgeMax = (Xsize, Ysize, Zsize)  # for variables being too high
        for x in self.toVectors():
            nudgeMin=(min(nudgeMin[0],x[0]),min(nudgeMin[1],x[1]),min(nudgeMin[2],x[2]))
            nudgeMax=(max(nudgeMax[0],x[0]),max(nudgeMax[1],x[1]),max(nudgeMax[2],x[2]))
        return addVec(negVec(nudgeMin),addVec(nudgeMax,(-Xsize, -Ysize, -Zsize)))  # how much to nudge to offset collision with the side of the box


##Game object

class GAME(object):
    def __init__(self, level):  ## Initialization
        self.dim = (6,6,12)
        self.grid = [[[(0, 0, 0) for x in range(self.dim[0])] for x in range(self.dim[1])] for x in range(self.dim[2])]  # empty grid start
        self.level = level  # usually level 1
        self.score = 0
        self.mult = 0
        self.currentPiece = PIECE(random.randint(0, 7))  # current piece
        self.nextPieces = [PIECE(random.randint(0, 7)) for x in range(3)]  # next piece in sequence
    def checkIfLost(self):
        for x in range(self.dim[0]):
            for y in range(self.dim[1]):
                if not self.grid[x][y][self.dim[2]-1] == (0,0,0):
                    return True
        return False


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col):
    pass


def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pass


def main():
    pass


def main_menu():
    pass
