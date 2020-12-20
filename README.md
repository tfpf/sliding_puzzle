# Sliding Puzzle
A sliding puzzle implementation using Python Tkinter. To play, first install
the following Python packages.
* Tkinter (for GUI processing)
* OpenCV (to read the puzzle image)
* NumPy (required by OpenCV)

Then download/clone this repository. Finally, open a terminal to the
download/clone location and run
<br>
`python3 main.py 3 crysis2.png`
<br>
and enjoy! This will create a 3-by-3 sliding puzzle (i.e. an 8-puzzle) using
the image file 'crysis2.png'.

If you want to use a different image (say, 'myimage.jpg'), delete the cached
image files (`rm img*.png`) and specify your new image on the command line
<br>
`python3 main.py 3 myimage.jpg`
<br>
and it should work. Just make sure that 'myimage.jpg' is a square image.
Otherwise, it may get visibly distorted.

To play at higher difficulty levels, just change the number on the command
line. For instance,
<br>
`python3 main.py 4 myimage.jpg`
<br>
will create a 4-by-4 sliding puzzle (i.e. a 15-puzzle), whereas
<br>
`python3 main.py 6 myimage.jpg`
<br>
will create a 6-by-6 sliding puzzle (i.e. a 35-puzzle).

