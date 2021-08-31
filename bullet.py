from turtle import Turtle, register_shape


class Bullet(Turtle):
    def __init__(self, paddle_x: float):
        super().__init__()
        register_shape("sprites/bullet-splode.gif")
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=0.1)
        self.x = paddle_x
        self.goto(self.x, -250)
        self.y_move = 10
        self.showturtle()
        self.timer = 15
        self.pause = False
        self.move()

    def move(self):
        if not self.pause:
            new_y = self.ycor() + self.y_move
            self.goto(self.x, new_y)







class Bullets:
    def __init__(self):
        self.b_list = []
        self.dead_b_list = []
        self.on = None