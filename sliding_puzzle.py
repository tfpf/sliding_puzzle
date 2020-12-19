#! /usr/local/bin/python3.8 -B

import cv2
import itertools
import numpy as np
import os
import tkinter as tk

###############################################################################

pad = 10
imsize = 150

###############################################################################

class sliding_puzzle(tk.Frame):
    '''\
Display a sliding puzzle using a square image. Said square image is divided
into smaller square sub-images, according to the argument provided to the
constructor. All sub-images are then resized to `imsize' and saved to the disk,
so that they can be used the next time this program is run. The input image
must be square in shape for this to work as expected.

Each sub-image is a button, which, when clicked, will move to the empty
slot if possible. The spacing between the sub-images can be controlled by
changing `pad'.

Attributes:
    size: int (maximum number of sub-images per row or column)
    images: list (list of sub-images)
    vacant: tuple (indicates which location is currently vacant)

Methods:
    __init__
    __repr__
    move: move the indicated sub-image to the vacant slot if possible
'''

    def __init__(self, parent, size = 3, image = 'crysis2.png'):
        tk.Frame.__init__(self, parent)
        self.grid(padx = pad, pady = pad)
        self.size = size
        self.images = []
        parent.title('Sliding Puzzle')
        parent.resizable(False, False)

        # check if images are already available
        # if not, create the images and save them for future use
        try:
            for i in range(self.size ** 2):
                with open(f'img{i}.png'):
                    pass
        except FileNotFoundError:
            img = cv2.imread(image)
            for i, (r, c) in enumerate(itertools.product(range(self.size), range(self.size))):
                h_step = img.shape[0] // self.size
                v_step = img.shape[1] // self.size
                img_crop = img[r * h_step : (r + 1) * h_step, c * v_step : (c + 1) * v_step]
                img_crop = cv2.resize(img_crop, (imsize, imsize))
                cv2.imwrite(f'img{i}.png', img_crop)
        finally:
            for i, (r, c) in enumerate(itertools.product(range(self.size), range(self.size))):
                self.images.append(tk.PhotoImage(file = f'img{i}.png')) 
                button = tk.Button(self, image = self.images[i])
                button['command'] = lambda _button = button: self.move(_button)
                button.grid(row = r, column = c)
            button.destroy()

        self.vacant = (self.size - 1, self.size - 1)

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

