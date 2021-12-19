"""
File: draw_line.py
Name: Jacky
-------------------------
This program is to draw lines. We will click two points to draw a line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant is to decide the width of lines
SIZE = 10

# Global variables
window = GWindow()
circle = GOval(SIZE, SIZE)
n = 0
start_x = 0
start_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(function)


def function(mouse):
    global n, start_x, start_y
    if n == 0:  # n=0, Starting point of a line (first click)
        start_x = mouse.x
        start_y = mouse.y
        window.add(circle, start_x, start_y)
        n = 1
    else:  # n=1, Ending point of a line (second click)
        end_x = mouse.x
        end_y = mouse.y
        window.remove(circle)
        draw = GLine(start_x, start_y, end_x, end_y)
        window.add(draw)
        n = 0


if __name__ == "__main__":
    main()
