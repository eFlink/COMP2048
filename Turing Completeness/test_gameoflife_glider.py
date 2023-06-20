# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
N = 1750
# N = 300
# N = 64
# N = 3

# create the game of life object
life = conway.GameOfLife(N)
# life.insertBlinker((0,0))
# life.insertGlider((0, 0))
# life.insertGliderGun((0, 0))

# Part d
# life.insertFromPlainText("Vacuum.cells")
# life.insertFromPlainText("g4receiver.cells")

# Part e
# life.insertFromPlainText("3-engine_cordship_gun.cells")
# life.insertFromPlainText("Period-60_glider_gun.cells")

# Part f
# life.insertFromRLE("Glider.rle")
life.insertFromRLE("turingmachine.rle")


cells = life.getStates()  # initial state

# -------------------------------
# plot cells

# import this to allow animations

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life

    life.evolve()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,


interval = 100  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
