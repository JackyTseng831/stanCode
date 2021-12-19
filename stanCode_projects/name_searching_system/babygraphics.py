"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    length = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)  # same length of each year
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*length
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       fill='black')  # upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill='black')  # bottom line
    for i in range(len(YEARS)):  # create the line and the year text of each year
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill='black')
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           font="times 15")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    place = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK  # height per ranking
    for i in range (len(lookup_names)):  # each name in lookup_names list
        name = lookup_names[i]
        information = name_data[name]  # the ranking of name in each year
        color = COLORS[i]  # order of color
        for j in range(len(YEARS)):
            if j+1 < len(YEARS):  # not last year
                x1 = get_x_coordinate(CANVAS_WIDTH, j)  # x of left line
                x2 = get_x_coordinate(CANVAS_WIDTH, j + 1)  # x of right line
                if str(YEARS[j]) in information and str(YEARS[j+1]) in information:  # left and right both have ranking
                    # data
                    rank = information[str(YEARS[j])]
                    rank1 = float(rank)
                    rank2 = information[str(YEARS[j+1])]
                    rank2 = float(rank2)
                    y1 = GRAPH_MARGIN_SIZE+rank1*place
                    y2 = GRAPH_MARGIN_SIZE+rank2*place
                    canvas.create_text(x1 + TEXT_DX, y1, text=name+rank, anchor=tkinter.SW,
                                       font="times 12", fill=color)
                elif str(YEARS[j]) not in information:
                    if str(YEARS[j+1]) in information:  # left have no ranking and right have
                        rank2 = information[str(YEARS[j + 1])]
                        rank2 = float(rank2)
                        y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE  # left at bottom line
                        y2 = GRAPH_MARGIN_SIZE+rank2*place
                    else:  # both left and right have no ranking ( both at bottom line)
                        y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x1 + TEXT_DX, y1, text=name+'*', anchor=tkinter.SW,
                                       font="times 12", fill=color)
                else:  # left have ranking and right have no ranking
                    rank = information[str(YEARS[j])]
                    rank1 = float(rank)
                    y1 = GRAPH_MARGIN_SIZE + rank1 * place
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x1 + TEXT_DX, y1, text=name + rank, anchor=tkinter.SW,
                                       font="times 12", fill=COLORS[i])
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            else:  # last year
                if str(YEARS[j]) in information:
                    rank = information[str(YEARS[j])]
                    rank1 = float(rank)
                    x1 = get_x_coordinate(CANVAS_WIDTH, j)
                    y1 = GRAPH_MARGIN_SIZE + rank1 * place
                    canvas.create_text(x1 + TEXT_DX, y1, text=name + rank, anchor=tkinter.SW,
                                       font="times 12", fill=color)
                else:
                    x1 = get_x_coordinate(CANVAS_WIDTH, j)
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x1 + TEXT_DX, y1, text=name+'*', anchor=tkinter.SW,
                                       font="times 12", fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
