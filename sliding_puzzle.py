#! /usr/local/bin/python3.8 -B

import cv2
import itertools
import numpy as np
import os
import random
import tkinter as tk
import tkinter.messagebox as mb

###############################################################################

pad = 10
imsize = 600

###############################################################################

class sliding_puzzle(tk.Frame):
    '''\
Display a sliding puzzle using a square image. Said square image is divided
into smaller square sub-images, according to the argument provided to the
constructor. All sub-images are then resized so that the final puzzle is
`imsize' wide and `imsize' high. They are then saved to the disk, so that they
can be used the next time this program is run. The input image must be square
in shape for this to work as expected.

Each sub-image is put on a button, which, when clicked, will move to the empty
slot if possible. The spacing between the sub-images can be controlled by
changing `pad'.

All sub-images must be bound to a class member variable (`images') before
putting them on the buttons. Otherwise, the garbage collector deletes them
before they can be used.

Attributes:
    N: int (maximum number of sub-images per row or column)
    images: list (list of sub-images)
    buttons: list (list of buttons the sub-images are drawn on)
    vacant: tuple (indicates which location is currently vacant)
    monitor_status: bool (whether or not to show success message on completion)
    moves: int (how many moves the user has made)

Methods:
    __init__
    __repr__
    move: move the indicated sub-image to the vacant slot if possible
    randomise: randomly call `move' a large number of times
'''

    def __init__(self, parent, N = 3, image = 'crysis2.png'):
        tk.Frame.__init__(self, parent)
        self.grid(padx = pad, pady = pad)
        self.N = N
        self.images = []
        self.buttons = []
        self.vacant = (self.N - 1, self.N - 1)
        self.monitor_status = False
        self.moves = 0

        parent.title('Sliding Puzzle')
        parent.resizable(False, False)

        # check if images are already available
        # if not, create the images and save them for future use
        try:
            for i in range(self.N ** 2 - 1):
                with open(f'img{i:03d}.png'):
                    pass
        except FileNotFoundError:
            img = cv2.imread(image)
            for i, (r, c) in enumerate(list(itertools.product(range(self.N), range(self.N)))[: -1]):
                h_step = img.shape[0] // self.N
                v_step = img.shape[1] // self.N
                img_crop = img[r * h_step : (r + 1) * h_step, c * v_step : (c + 1) * v_step]
                img_crop = cv2.resize(img_crop, (imsize // self.N, imsize // self.N))
                cv2.imwrite(f'img{i:03d}.png', img_crop)
        finally:
            for i, (r, c) in enumerate(list(itertools.product(range(self.N), range(self.N)))[: -1]):
                self.images.append(tk.PhotoImage(file = f'img{i:03d}.png'))
                button = tk.Button(self, image = self.images[i])
                button['command'] = lambda _button = button: self.move(_button)
                button.grid(row = r, column = c)
                self.buttons.append(button)

        randomise_button = tk.Button(self, text = 'Randomise', command = self.randomise)
        randomise_button.grid(row = self.N, columnspan = self.N, pady = (4 * pad, pad))

    ########################################

    def __repr__(self):
        return f'sliding_puzzle(object)'

    ########################################

    def move(self, _button):
        '''\
Compare the position of the sub-image to be moved with the position of the
vacant slot. If they are adjacent to each other, interchange their positions.

Args:
    _button: tkinter.Button (the sub-image to be moved)
'''

        vacant_row, vacant_column = self.vacant
        button_row, button_column = tuple(map(_button.grid_info().get, ('row', 'column')))
        if set((abs(vacant_row - button_row), abs(vacant_column - button_column))) == {0, 1}:
            _button.grid(row = vacant_row, column = vacant_column)
            self.vacant = (button_row, button_column)

        # increment counter only if the game is being monitored
        if self.monitor_status:
            self.moves += 1

            # upon completion, stop monitoring
            if all(i == button.grid_info().get('row') * self.N + button.grid_info().get('column') for i, button in enumerate(self.buttons)):
                self.monitor_status = False
                mb.showinfo(title = 'Puzzle Solved!', message = f'You have solved the puzzle in {self.moves} moves!')

    ########################################

    def randomise(self):
        '''\
Move the sub-images randomly.
'''

        # start monitoring the game only after this function is called
        # i.e. after the user clicks the button to randomise the sub-images
        self.monitor_status = False
        for button in random.choices(self.buttons, k = 1000 * self.N):
            self.move(button)
        self.monitor_status = False
        self.moves = 0

