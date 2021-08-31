from turtle import Turtle, register_shape


class Brick(Turtle):
    """
    Class that defines the bricks used in the barriers.
    Each brick is a turtle class object with 2 sprites
    available as custom shapes:
    brick.gif and damaged.gif
    """
    def __init__(self):
        super().__init__()
        register_shape("sprites/damage.gif")
        register_shape("sprites/brick.gif")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.shape_1 = "sprites/brick.gif"
        self.shape_2 = "sprites/damage.gif"
        self.current_shape = self.shape_1
        self.shape(self.current_shape)
        self.color((0, 1, 0))
        self.goto(0, 0)
        self.shapesize(.4, .4)
        self.showturtle()




class Barrier:
    """
    the Barrier class creates the three barriers from Brick class objects
    and contains the brick_list as an attribute.
    """
    def __init__(self):
        self.brick_list = []
        self.y_ref = -185
        self.create_barrier_1()
        self.create_barrier_2()
        self.create_barrier_3()


    def create_barrier_1(self):
        """
        Creates the left barrier.
        :return:
        """
        x = -240
        y = self.y_ref
        for brick in range(6):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -244.5
        y -= 9
        for brick in range(7):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -249
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -249
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -249
        y -= 9
        for brick in range(4):
            if brick == 2:
                x += 36
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9

    def create_barrier_2(self):
        """
        Creates the center barrier.
        :return:
        """
        x = -27
        y = self.y_ref
        for brick in range(6):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -31.5
        y -= 9
        for brick in range(7):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -36
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -36
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9
        x = -36
        y -= 9
        for brick in range(4):
            if brick == 2:
                x += 36
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x += 9

    def create_barrier_3(self):
        """
        Creates the right barrier.
        :return:
        """
        x = 240
        y = self.y_ref
        for brick in range(6):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x -= 9
        x = 244.5
        y -= 9
        for brick in range(7):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x -= 9
        x = 249
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x -= 9
        x = 249
        y -= 9
        for brick in range(8):
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x -= 9
        x = 249
        y -= 9
        for brick in range(4):
            if brick == 2:
                x -= 36
            new_brick = Brick()
            new_brick.goto(x, y)
            self.brick_list.append(new_brick)
            x -= 9

    def show(self):
        for brick in self.brick_list:
            brick.shape(brick.shape_1)
            brick.showturtle()


