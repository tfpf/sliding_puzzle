#! /usr/local/bin/python3.8 -B

import sys
import tkinter as tk

import sliding_puzzle

###############################################################################

def main():

    try:
        image = sys.argv[1]
    except IndexError:
        image = 'crysis2.png'

    # setup
    sliding_puzzle.pad = 10
    sliding_puzzle.imsize = 150

    # create puzzle
    puzzle = sliding_puzzle.sliding_puzzle(tk.Tk(), 3, image)
    puzzle.mainloop()

###############################################################################

if __name__ == '__main__':
    main()

