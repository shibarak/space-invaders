from turtle import Turtle, register_shape, getshapes


class Tank(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        register_shape("sprites/tank.gif")
        register_shape("sprites/tank-splode.gif")
        register_shape("sprites/tank-splode2.gif")
        self.shape("sprites/tank.gif")
        self.speed('fastest')
        self.goto(0, -275)
        self.showturtle()
        self.shapesize(stretch_wid=3, stretch_len=0.5)


