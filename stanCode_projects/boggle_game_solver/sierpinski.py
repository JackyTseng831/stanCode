"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 7                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program is to draw sierpinski triangle with its order
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The order of the triangle
	:param length: The length of the triangle
	:param upper_left_x: The upper left x site of the triangle
	:param upper_left_y: The upper left y site of the triangle
	:return: The result of the sierpinski triangle with its order
	"""
	if order == 0:  # Base case!
		return
	else:
		# upper left triangle of next order
		sierpinski_triangle(order - 1, length * 1 / 2, upper_left_x, upper_left_y)
		# upper right triangle of next order
		sierpinski_triangle(order - 1, length * 1 / 2, upper_left_x + 0.5 * length, upper_left_y)
		# bottom triangle of next order
		sierpinski_triangle(order - 1, length * 1 / 2, upper_left_x + 0.25 * length, upper_left_y + 0.866 / 2 * length)
		# upper edge of the triangle
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# left edge of the triangle
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + 0.866 * length)
		# right edge of the triangle
		line_3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + 0.866 * length)
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)


if __name__ == '__main__':
	main()