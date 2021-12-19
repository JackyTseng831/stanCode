"""
File: bouncing_ball.py
Name: Jacky
-------------------------
This program is to simulate a ball with horizontal speed VX falling to ground, and bounce again with REDUCE times of
vertical speed.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 5
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
time = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    start_bounce()
    onmouseclicked(again)


def again(mouse):
    global time
    if time <= 2:  # The ball would only beyond the screen for 3 times.
        if mouse.x <= window.width and mouse.y <= window.height:  # The click should be in screen to restart the ball
            start_bounce()
            time += 1


def start_bounce():
    n = 0
    gravity = GRAVITY
    bounce = 0
    while True:
        if ball.x + SIZE <= window.width:
            if n == 0:  # n=0 means the ball fall down
                ball.move(VX, gravity)
                gravity += GRAVITY  # Vertical speed would increase GRAVITY each loop
                if ball.y+SIZE >= window.height:
                    n = 1  # n=1 means the ball bounce up
                    bounce = -gravity*REDUCE  # Vertical speed decrease to REDUCE times of last vertical speed reversely
            if n == 1:  # bounce
                ball.move(VX, bounce)
                if bounce < 0:  # The ball still go up
                    bounce += GRAVITY
                else:  # The ball start to fall down
                    n = 0
                    gravity = GRAVITY
            pause(DELAY)  # animation
        else:  # The ball beyond screen
            window.remove(ball)
            window.add(ball, x=START_X, y=START_Y)
            break


if __name__ == "__main__":
    main()
