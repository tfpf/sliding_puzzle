#! /usr/local/bin/python3.8 -B

import sliding_puzzle
import tkinter as tk

###############################################################################

def main():

    # setup
    sliding_puzzle.pad = 10
    sliding_puzzle.imsize = 150

    # create puzzle
    puzzle = sliding_puzzle.sliding_puzzle(tk.Tk(), size = 4)
    puzzle.mainloop()

###############################################################################

if __name__ == '__main__':
    main()

