# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import math

import numpy as np
import scipy.signal
from scipy import signal
import rle


class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''

    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N, N), np.int)
        self.neighborhood = np.ones((3, 3), np.int)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0

    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        # get weighted sum of neighbors
        # PART A & E CODE HERE

        N = self.grid.shape[0]

        # Part E
        # grid = np.zeros((N, N), np.int)
        #
        # convolved = scipy.signal.convolve(self.grid, self.neighborhood, mode='same')
        # grid = (((self.grid == 1) & (convolved > 1) & (convolved < 4)) | (
        #         (self.grid == 0) & (convolved == 3)))

        # PART A
        # neighbour_pos of the 8 or less cells around centre.

        neighbour_pos = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0],
                        [-1, 1], [0, 1], [1, 1]]
        cell_neighbour_count = np.zeros(self.grid.size, np.int)

        # cell number
        cell_number = 0
        # row and column index of the cell to be checks
        rowIdx = 0
        while rowIdx < N:
            colIdx = 0
            while colIdx < N:
                for neighbour in neighbour_pos:
                    rowPos = rowIdx + neighbour[0]
                    colPos = colIdx + neighbour[1]
                    # check if neighbour position is out of index
                    if rowPos < 0 or rowPos >= N or colPos < 0 or colPos >= N:
                        continue
                    # if alive, increase cell number count for the specified cell
                    cell_neighbour_count[cell_number] += self.grid[rowPos][colPos]
                cell_number += 1
                colIdx += 1
            rowIdx += 1

        # implement the GoL rules by thresholding the weights
        # PART A CODE HERE
        grid = np.zeros((N, N), np.int)

        # reset cell number to iterate through again
        cell_number = 0

        # row and column index of the cell to be checks
        rowIdx = 0
        while rowIdx < N:
            colIdx = 0
            while colIdx < N:
                # if cell is alive
                # print(cell_neighbour_count[cell_number], " ", self.grid[rowIdx][colIdx])

                if self.grid[rowIdx][colIdx] == 1:
                    if cell_neighbour_count[cell_number] < 2 or cell_neighbour_count[cell_number] > 3:
                        grid[rowIdx][colIdx] = 0
                    else:
                        grid[rowIdx][colIdx] = 1
                else:
                    if cell_neighbour_count[cell_number] == 3:
                        grid[rowIdx][colIdx] = 1
                cell_number += 1
                colIdx += 1
            rowIdx += 1

        # update the grid
        self.grid = grid  # UNCOMMENT THIS WITH YOUR UPDATED GRID

    def insertBlinker(self, index=(0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0] + 1, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 35] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 35] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue

        self.grid[index[0] + 5, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue

        # add index for part I c)
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue

        self.grid[index[0] + 6, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 7, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 16] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue

    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        N = self.grid.shape[0]
        grid = np.zeros((N, N), np.int)
        with open(txtString) as plaintext:
            row = 0
            for line in plaintext:
                i = 0
                # skip line if there is a comment
                if line[0] == '!':
                    # skip line and row for inserting cell states
                    if line[0] == '\n':
                        row += 1
                    continue
                for char in line:
                    if char == '.':
                        grid[row][i] = 0
                    elif char == 'O':
                        grid[row][i] = 1
                    i += 1
                row += 1
        self.grid = grid

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''

        N = self.grid.shape[0]
        grid = np.zeros((N, N), np.int)

        with open(rleString) as rle_file:
            parser = rle.RunLengthEncodedParser(rle_file.read())
            row = 0
            col = 0
            for char in parser.human_friendly_pattern:
                if char == '\n':
                    col = 0
                    row += 1
                    continue
                elif char == '.':
                    grid[row][col] = 0
                else:
                    grid[row][col] = 1
                col += 1
        self.grid = grid
