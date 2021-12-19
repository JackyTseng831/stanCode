"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 50 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics(10, 75, 15, 50, 8 , 8 , 40, 15, 50, 5)

    # Add animation loop here!
    bottom_times = NUM_LIVES
    remain_bricks = graphics.brick_cols*graphics.brick_rows
    dx = graphics.get_dx()  # get x speed
    dy = graphics.get_dy()  # get y speed

    while True:
        pause(FRAME_RATE)
        if bottom_times >= 0 or remain_bricks > 0:  # still have lives or no brick on screen
            if graphics.n == 1:  # if on
                graphics.find_vertex()
                if graphics.bottom():
                    bottom_times -= 1  # dead once
                    if bottom_times <= 0:
                        break  # totally dead
                    graphics.n = 0  # turn off
                    graphics.set_a_ball()
                    graphics.create_a_ball()
                elif graphics.top():
                    dx *= -1
                    dy *= -1
                elif graphics.side():
                    dx *= -1
                elif graphics.touch():
                    if graphics.touch_paddle_1():  # ball touch top of the paddle
                        if graphics.ball.x + graphics.ball_radius*2 > graphics.paddle.x or graphics.paddle.x + graphics.paddle_length > graphics.ball.x:  # ball not touch side of paddle
                            if graphics.touch_paddle_2():  # ball not touch bottom of the paddle
                                dy *= -1
                    else:
                        graphics.remove_brick()
                        remain_bricks -= 1
                        if remain_bricks == 0:
                            break  # complete
                        dy *= -1
                graphics.ball.move(dx, dy)


if __name__ == '__main__':
    main()
