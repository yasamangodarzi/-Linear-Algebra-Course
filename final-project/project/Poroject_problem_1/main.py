import pygame
import numpy
import math
import re
from sympy import *

The_pivot_information_of_Matrix = []


class Solve_Game:
    def __init__(self, number_of_cells, cell):
        self.number_cells = number_of_cells
        self.cell = cell

    def create_matrix(self):
        Matrix_orginal = numpy.zeros(
            (self.number_cells * self.number_cells, (self.number_cells * self.number_cells) + 1), dtype=numpy.int)
        for i in range(1, self.number_cells * self.number_cells + 1):
            right = i + 1
            left = i - 1
            down = i + self.number_cells
            up = i - self.number_cells
            if i % self.number_cells == 0:
                right = -1
            if i % self.number_cells == 1:
                left = -1
            Matrix_1 = numpy.zeros(self.number_cells * self.number_cells, dtype=numpy.int)
            if 0 < right < self.number_cells * self.number_cells + 1:
                Matrix_1[right - 1] = 1
            if 0 < left < self.number_cells * self.number_cells + 1:
                Matrix_1[left - 1] = 1
            if 0 < down < self.number_cells * self.number_cells + 1:
                Matrix_1[down - 1] = 1
            if 0 < up < self.number_cells * self.number_cells + 1:
                Matrix_1[up - 1] = 1
            Matrix_1[i - 1] = 1
            Matrix_orginal[:, i - 1] = Matrix_1
        key = 0
        for item in (self.cell):
            for part in (item):
                Matrix_orginal[:, self.number_cells * self.number_cells][key] = part
                key += 1
        return Matrix_orginal

    def Echelon_form_of_Matrix(self):
        Pivot = None
        Echelon_Matrix = self.create_matrix().astype(float)
        result = [[Echelon_Matrix[j][i] for j in range(len(Echelon_Matrix))] for i in range(len(Echelon_Matrix[0]))]
        pivot_index = -1
        Previous_pivot_index = -1
        i = 0
        while i < len(result):
            result = [[Echelon_Matrix[j][i] for j in range(len(Echelon_Matrix))] for i in range(len(Echelon_Matrix[0]))]
            item = result[i]
            i += 1
            for index in range(len(item)):
                if index == 0:
                    info = {"number_of_column": i, "number_of_row": pivot_index, "data": Pivot}
                    The_pivot_information_of_Matrix.append(info)
                    Pivot = None
                    Previous_pivot_index = pivot_index
                    pivot_index = -1
                if item[index] != 0 and Pivot is None and index > Previous_pivot_index:
                    Pivot = item[index]
                    pivot_index = index
                    if pivot_index != Previous_pivot_index + 1:
                        temp = numpy.array(Echelon_Matrix[Previous_pivot_index + 1])
                        Echelon_Matrix[Previous_pivot_index + 1] = Echelon_Matrix[pivot_index]
                        Echelon_Matrix[pivot_index] = temp
                        pivot_index = Previous_pivot_index + 1
                elif item[index] != 0 and Pivot is not None:
                    b = numpy.array([item[index], 0])
                    a = numpy.array([[Pivot, 0], [1, 1]])
                    Coefficient = numpy.linalg.solve(a, b)[0]
                    Echelon_Matrix[index] = [math.fabs(int(a - b) % 2) for a, b in
                                             zip(Echelon_Matrix[index], Echelon_Matrix[pivot_index] * Coefficient)]

        return Echelon_Matrix

    def correct_reducrd(self):
        Reduced_Echelon_Matrix= Matrix(self.Echelon_form_of_Matrix()).rref()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in Reduced_Echelon_Matrix]))
        return Reduced_Echelon_Matrix
        # Reduced_Echelon_Matrix = self.Echelon_form_of_Matrix()
        # for key,item in enumerate(Reduced_Echelon_Matrix):

    def Reduced_Echelon_Form_of_Matrix(self):
        Reduced_Echelon_Matrix = self.Echelon_form_of_Matrix().T
        # Reduced_Echelon_Matrix = Reduced_Echelon_Matrix.T
        pivot = None
        pivot_index = -1
        i = 1
        result = [[Reduced_Echelon_Matrix[j][i] for j in range(len(Reduced_Echelon_Matrix))] for i in
                  range(len(Reduced_Echelon_Matrix[0]))]
        ig = 0
        while ig < len(Reduced_Echelon_Matrix):
            Reduced_Echelon_Matrix = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
            item = Reduced_Echelon_Matrix[ig]
            try:
                info = The_pivot_information_of_Matrix[i]
            except:
                ig += 1
                continue

            pivot = info["data"]
            pivot_index = info["number_of_row"]
            i += 1
            ig += 1
            help_list = []
            for index in range(len(item)):
                if index == info["number_of_row"] and pivot is not None:
                    result[info["number_of_row"]] = result[info["number_of_row"]] / info["data"]
                elif item[index] != 0 and pivot is not None:
                    b = numpy.array([item[index], 0])
                    a = numpy.array([[pivot, 0], [1, 1]])
                    Coefficient = numpy.linalg.solve(a, b)[0]
                    for number in result[pivot_index]:
                        help_list.append(int(number * Coefficient))
                    result[index] = [float(a - b) for a, b in zip(result[index], help_list)]
                    help_list.clear()
        # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        #                  for row in Reduced_Echelon_Matrix]))
        # return Reduced_Echelon_Matrix
        return numpy.array(Reduced_Echelon_Matrix).T


import pygame
import numpy

### Globals ###

pygame.init()

adj = [[0, 0], [0, -1], [-1, 0], [0, 1], [1, 0]]

TILE_HEIGHT = 50
TILE_WIDTH = 50
MARGIN = 2


class Game:
    def __init__(self, cells):
        self.cells = cells
        self.clear()
        self.load_level()

    def clear(self):
        self.grid = [[0 for i in range(len(self.cells))] for j in range(len(self.cells))]

    def load_level(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                self.grid[x][y] = int(self.cells[y][x])

    def draw(self):
        for y in range(len(self.cells)):
            for x in range(len(self.cells)):
                i = x * TILE_WIDTH + MARGIN
                j = y * TILE_HEIGHT + MARGIN
                h = TILE_HEIGHT - (2 * MARGIN)
                w = TILE_WIDTH - (2 * MARGIN)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, (105, 210, 231), [i, j, w, h])
                else:
                    pygame.draw.rect(screen, (255, 255, 255), [i, j, w, h])

    def get_adjacent(self, x, y):
        adjs = []
        for i, j in adj:
            if (0 <= i + x < len(self.cells)) and (0 <= j + y < len(self.cells)):
                adjs += [[i + x, j + y]]
        return adjs

    def click(self, pos):
        x = int(pos[0] / TILE_WIDTH)
        y = int(pos[1] / TILE_HEIGHT)
        adjs = self.get_adjacent(x, y)
        for i, j in adjs:
            self.grid[j][i] = (self.grid[j][i] + 1) % 2


### Main ###

if __name__ == "__main__":

    cells = [[1, 0, 0, 0, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1],]
    # cells = [[1, 1, 0],
    #          [1, 0, 1],
    #          [0, 0, 0],
    #
    #          ]
    Solve_Game(5, cells).correct_reducrd()

    screen = pygame.display.set_mode((len(cells) * TILE_WIDTH, len(cells) * TILE_HEIGHT))
    screen.fill((167, 219, 216))
    pygame.display.set_caption("Game")

    game = Game(cells)
    game.draw()

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        game.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.click(pos)
        pygame.display.flip()
    pygame.quit()
