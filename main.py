#! /usr/local/bin/python3.8 -B

import sys
import tkinter as tk

import sliding_puzzle

###############################################################################

def main():

    try:
        N = int(sys.argv[1])
        assert N > 2
    except (AssertionError, IndexError, ValueError):
        N = 3

    try:
        image = sys.argv[2]
    except IndexError:
        image = 'crysis2.png'

    sliding_puzzle.pad = 10
    sliding_puzzle.imsize = 600

    puzzle = sliding_puzzle.sliding_puzzle(tk.Tk(), N, image)
    puzzle.mainloop()

###############################################################################

if __name__ == '__main__':
    main()

