"""
File: my_drawing.py
Name: Jacky
----------------------
A cute koala
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow

window = GWindow(500, 500)


def main():
    """
    Just a cute koala
    """
    sky()
    window.add(sky())
    ground()
    window.add(ground())
    tree()
    window.add(tree())
    leaf()
    window.add(leaf())
    koala()
    window.add(koala())


def ground():
    grass = GPolygon()
    grass.add_vertex((0, 375))
    grass.add_vertex((0, 500))
    grass.add_vertex((500, 500))
    grass.add_vertex((500, 375))
    grass.add_vertex((180, 300))
    grass.filled = True
    grass.fill_color = 'seagreen'
    grass.color = 'green'
    return grass


def sky():
    blue_sky = GRect(500, 500, x=0, y=0)
    blue_sky.filled = True
    blue_sky.fill_color = 'skyblue'
    blue_sky.color = 'skyblue'
    return blue_sky


def tree():
    trunk = GPolygon()
    trunk.add_vertex((100, 0))
    trunk.add_vertex((185, 0))
    trunk.add_vertex((210, 250))
    trunk.add_vertex((240, 500))
    trunk.add_vertex((140, 500))
    trunk.add_vertex((120, 260))
    trunk.filled = True
    trunk.fill_color = 'saddlebrown'
    return trunk


def leaf():
    leave = GPolygon()
    leave.add_vertex((120, 260))
    leave.add_vertex((100, 270))
    leave.add_vertex((80, 273))
    leave.add_vertex((60, 260))
    leave.add_vertex((50, 245))
    leave.add_vertex((70, 237))
    leave.add_vertex((90, 235))
    leave.add_vertex((110, 245))
    leave.filled = True
    leave.fill_color = 'darkgreen'
    leave.color = 'black'
    return leave


def koala():
    front_leg = GOval(80, 40, x=175, y=300)
    front_leg.filled = True
    front_leg.fill_color = 'gray'
    window.add(front_leg)
    leg = GOval(90, 50, x=180, y=400)
    leg.filled = True
    leg.fill_color = 'gray'
    window.add(leg)
    body = GOval(165, 190, x=215, y=275)
    body.filled = True
    body.fill_color = 'gray'
    window.add(body)
    left_ear = GOval(95, 95, x=155, y=100)
    left_ear.filled = True
    left_ear.fill_color = 'gray'
    window.add(left_ear)
    left_ear_in = GOval(60, 60, x=180, y=130)
    left_ear_in.filled = True
    left_ear_in.fill_color = 'dimgrey'
    window.add(left_ear_in)
    right_ear = GOval(95, 95, x=340, y=98)
    right_ear.filled = True
    right_ear.fill_color = 'gray'
    window.add(right_ear)
    right_ear_in = GOval(60, 60, x=350, y=128)
    right_ear_in.filled = True
    right_ear_in.fill_color = 'dimgrey'
    window.add(right_ear_in)
    head = GOval(180, 150, x=210, y=140)
    head.filled = True
    head.fill_color = 'gray'
    window.add(head)
    left_eye = GOval(15, 15, x=250, y=200)
    left_eye.filled = True
    window.add(left_eye)
    right_eye = GOval(15, 15, x=330, y=200)
    right_eye.filled = True
    window.add(right_eye)
    nose = GOval(40, 50, x=277, y=220)
    nose.filled = True
    nose.fill_color = 'dimgrey'
    window.add(nose)
    mouse = GArc(45, 50, 180, 180)
    window.add(mouse, x=275, y=255)


if __name__ == '__main__':
    main()
