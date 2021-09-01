from turtle import Turtle, register_shape

class Zap(Turtle):
    def __init__(self, inv_x: float, inv_y: float):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        register_shape("sprites/ishot1.gif")
        register_shape("sprites/ishot2.gif")
        register_shape("sprites/ishot-dead.gif")
        self.shape_1 = "sprites/ishot1.gif"
        self.shape_2 = "sprites/ishot2.gif"
        self.current_shape = "sprites/ishot1.gif"
        self.shape(self.current_shape)
        self.color("white")
        self.shapesize(stretch_wid=0.3, stretch_len=0.1)
        self.x = inv_x
        self.y = inv_y
        self.goto(self.x, self.y)
        self.y_move = -8
        self.showturtle()
        self.pause = False
        self.move()

    def move(self):
        if not self.pause:
            new_y = self.ycor() + self.y_move
            self.goto(self.x, new_y)


class Zaps:
    def __init__(self):
        self.z_list = []
        self.limiter_abs = 18
        self.limiter = self.limiter_abs
        self.pause = False

    def zap_em(self, x, y):
        if not self.pause:
            if self.limiter < 0:
                self.z_list.append(Zap(inv_x=x, inv_y=y))
                self.limiter = self.limiter_abs

    def timer(self):
        self.limiter -= 1
