"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.n = 0  # off (ball no move)
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2,
                        y=self.window_height-(paddle_offset+paddle_height))
        self.paddle.filled = True
        self.paddle_thick = PADDLE_HEIGHT
        self.paddle_length = PADDLE_WIDTH
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2, x=self.window_width / 2 - self.ball_radius,
                          y=self.window_height / 2 - self.ball_radius)
        self.window.add(self.ball)
        self.ball.filled = True
        # Detect parameters
        self.find_1 = 0
        self.find_2 = 0
        self.find_3 = 0
        self.find_4 = 0
        # Default initial velocity for the ball
        self._dy = INITIAL_Y_SPEED
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=brick_offset + i * (brick_height + brick_spacing))
        # Initialize our mouse listeners
        self.moved = onmousemoved(self.second)
        self.start()

    def set_a_ball(self):
        self.ball.x = self.window_width / 2 - self.ball_radius
        self.ball.y = self.window_height / 2 - self.ball_radius

    def create_a_ball(self):
        self.window.add(self.ball)

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def start(self):  # for ball moving
        onmouseclicked(self.first)

    def first(self, mouse):
        self.n = 1  # on

    def bottom(self):  # ball reach bottom of the screen
        beyond = self.ball.y+2*BALL_RADIUS >= self.window.height
        return beyond

    def find_vertex(self):  # detect touchable
        self.find_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.find_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        self.find_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        self.find_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                                self.ball.y + 2 * self.ball_radius)

    def second(self, mouse):  # for paddle moving
        if 0 <= mouse.x <= self.window.width-self.paddle.width:
            self.paddle.x = mouse.x

    def touch_paddle_1(self):  # ball touch paddle
        paddle_1 = self.paddle.y <= self.ball.y+self.ball_radius*2
        return paddle_1

    def touch_paddle_2(self):  # ball touch paddle
        paddle_2 = self.ball.y < self.paddle.y+self.paddle_thick/2
        return paddle_2

    def remove_brick(self):
        remove = self.window.remove(self.find_1)
        self.window.remove(self.find_2)
        self.window.remove(self.find_3)
        self.window.remove(self.find_4)
        return remove

    def top(self):  # ball reach top of screen
        top = self.ball.y <= 0
        return top

    def side(self):  # ball reach side of screen
        side = self.ball.x+2*BALL_RADIUS >= self.window.width or self.ball.x <= 0
        return side

    def touch(self):  # ball touch other objects
        touch = self.find_1 or self.find_2 or self.find_3 or self.find_4 is not None
        return touch
