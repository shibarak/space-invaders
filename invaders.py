from turtle import Turtle, register_shape
import simpleaudio as sa
from time import time
from pprint import pprint
# 11 guys per line 16 steps to go down


ufo_wav = sa.WaveObject.from_wave_file("audio/ufo_lowpitch.wav")
class Saucer(Turtle):
    """
    Class that defines the saucer.
    Creates a turtle class object with 3 sprites
    available as custom shapes:
    saucer.gif, saucer-points.gif and explodered.gif
    """
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        register_shape("sprites/saucer.gif")
        register_shape("sprites/saucer-points.gif")
        register_shape("sprites/explodered.gif")
        register_shape("sprites/explodered2.gif")
        self.shape_1 = "sprites/saucer.gif"
        self.shape_2 = "sprites/explodered.gif"
        self.shape_3 = "sprites/saucer-points.gif"
        self.shape_4 = "square"
        self.current_shape = self.shape_1
        self.penup()
        self.shape(self.current_shape)
        self.goto(-380, 330)
        self.points = 100
        self.showturtle()



class Invader1(Turtle):
    """
    Class that defines the top row invaders.
    Creates a turtle class object with 3 sprites
    available as custom shapes:
    invader1-1.gif, invader1-2.gif and explode.gif
    """
    def __init__(self):
        self.timer = 0
        super().__init__()
        self.speed(0)
        self.hideturtle()
        register_shape("sprites/invader1-1.gif")
        register_shape("sprites/invader1-2.gif")
        self.shape_1 = "sprites/invader1-1.gif"
        self.shape_2 = "sprites/invader1-2.gif"
        register_shape("sprites/explode.gif")
        self.shape_3 = "sprites/explode.gif"
        self.current_shape = self.shape_1
        self.penup()
        self.shape(self.current_shape)
        self.points = 30
        self.showturtle()

    def change_shape(self):
        """
        Changes the sprite for an Invader1 class object.
        Called everytime an invader moves
        :return:
        """
        if self.current_shape == self.shape_1:
            self.current_shape = self.shape_2
            self.shape(self.current_shape)
        else:
            self.current_shape = self.shape_1
            self.shape(self.current_shape)


class Invader2(Turtle):
    """
       Class that defines the middle 2 rows of invaders.
       Creates a turtle class object with 3 sprites
       available as custom shapes:
       invader2-1.gif, invader2-2.gif and explode.gif
       """
    def __init__(self):
        self.timer = 0
        super().__init__()
        self.speed(0)
        self.hideturtle()
        register_shape("sprites/invader2-1.gif")
        register_shape("sprites/invader2-2.gif")
        self.shape_1 = "sprites/invader2-1.gif"
        self.shape_2 = "sprites/invader2-2.gif"
        register_shape("sprites/explode.gif")
        self.shape_3 = "sprites/explode.gif"
        self.current_shape = self.shape_1
        self.penup()
        self.shape(self.current_shape)
        self.points = 20
        self.showturtle()

    def change_shape(self):
        """
        Changes the sprite for an Invader2 class object.
        Called everytime an invader moves
        :return:
        """
        if self.current_shape == self.shape_1:
            self.current_shape = self.shape_2
            self.shape(self.current_shape)
        else:
            self.current_shape = self.shape_1
            self.shape(self.current_shape)


class Invader3(Turtle):
    """
       Class that defines the bottom 2 rows of invaders.
       Creates a turtle class object with 3 sprites
       available as custom shapes:
       invader3-1.gif, invader3-2.gif and explode.gif
       """
    def __init__(self):
        self.timer = 0

        super().__init__()
        self.hideturtle()
        self.speed(0)
        register_shape("sprites/invader3-1.gif")
        register_shape("sprites/invader3-2.gif")
        self.shape_1 = "sprites/invader3-1.gif"
        self.shape_2 = "sprites/invader3-2.gif"
        register_shape("sprites/explode.gif")
        self.shape_3 = "sprites/explode.gif"
        self.current_shape = self.shape_1
        self.penup()
        self.shape(self.current_shape)
        self.points = 10
        self.showturtle()

    def change_shape(self):
        """
        Changes the sprite for an Invader2 class object.
        Called everytime an invader moves
        :return:
        """
        if self.current_shape == self.shape_1:
            self.current_shape = self.shape_2
            self.shape(self.current_shape)
        else:
            self.current_shape = self.shape_1
            self.shape(self.current_shape)


class Invaders:
    """
    The invaders class creates the invasion from Invader class objects.
    it contains methods to handle the motion of the invaders and reset them
    after level up or gameover.
    """
    def __init__(self):
        self.saucer = Saucer()
        self.invader_list = [[], [], [], [], [], [], [], [], [], [], []]
        self.saucer_count = 0
        self.saucer_timer = 4
        self.saucer_mov = 4
        self.init_x = -273
        self.init_y = 270
        self.mov_x = 4
        self.mov_y = -20
        self.start_time = None
        self.timer = 35
        self.timer_abs = 35
        self.interval = 1.7
        self.moved = False
        self.step_down = False
        self.completed = False
        self.game = False
        self.pause = False
        self.invade()

    def invade(self):
        '''
        Creates the invasion by filling the self.invader_list with invader class objects
        at the appropriate intervals.
        :return:
        '''
        x = self.init_x
        y = self.init_y
        for col in self.invader_list:
            for i in range(0, 5):
                if i == 0:
                    inv = Invader1()
                    inv.goto(x=x, y=y)
                    col.append(inv)
                    print(x, y)
                    y -= 54

                elif i <= 2:
                    inv = Invader2()
                    inv.goto(x=x, y=y)
                    col.append(inv)
                    print(x, y)
                    y -= 54
                else:
                    inv = Invader3()
                    inv.goto(x=x, y=y)
                    col.append(inv)
                    print(x, y)
                    y -= 54
            x += 52
            y = self.init_y

        pprint(self.invader_list)
        print(self.invader_list)

    def reset(self):
        """
        restes the invader list after gameover or level up.
        :return:
        """
        self.timer_abs = 35
        self.timer = 35
        x = self.init_x
        y = self.init_y
        for col in self.invader_list:
            for inv in col:
                inv.goto(x, y)
                inv.current_shape = inv.shape_1
                inv.shape(inv.current_shape)
                inv.showturtle()
                y -= 54
            x += 52
            y = self.init_y
        pprint(self.invader_list)
        print(self.invader_list)

    def move(self):
        """
        Controls the movement of the saucer and invader class objects on screen.
        :return:
        """
        if not self.pause:
            if self.step_down:
                self.mov_x *= -1
                self.step_down = False
            if self.saucer_count > 10:
                if self.saucer_timer == 0:
                    if self.saucer.current_shape == self.saucer.shape_2:
                        self.saucer.current_shape = self.saucer.shape_3
                        self.saucer_timer = 10
                        pass
                    elif self.saucer.current_shape == self.saucer.shape_3:
                        self.saucer.shape(self.saucer.current_shape)
                        self.saucer.current_shape = self.saucer.shape_4
                        self.saucer_timer = 10
                        pass
                    elif self.saucer.current_shape == self.saucer.shape_4:
                        self.saucer.hideturtle()
                        self.saucer.current_shape = self.saucer.shape_1
                        self.saucer.shape(self.saucer.current_shape)
                        self.saucer.goto(-380, 330)
                        self.saucer.showturtle()
                        self.saucer_count = 0
                    else:
                        new_x = self.saucer.xcor() + self.saucer_mov
                        self.saucer.goto(new_x, 330)
                        self.saucer_timer = 1
                        if new_x > 380:
                            self.saucer.hideturtle()
                            self.saucer.goto(-380, 330)
                            self.saucer.showturtle()
                            self.saucer_count = 0
                else:
                    self.saucer_timer -= 1
            if self.timer != 0:
                self.timer -= 1
                self.moved = False
            else:
                self.moved = True
                for column in self.invader_list:
                    for inv in column:
                        if inv.current_shape == inv.shape_3:
                            inv.hideturtle()
                        else:
                            new_x = (inv.xcor() + self.mov_x)
                            inv.goto(new_x, inv.ycor())
                            inv.change_shape()
                            if inv.isvisible() and not self.step_down:
                                if -305 > new_x or 305 < new_x:
                                    self.step_down = True
                                    for col in self.invader_list:
                                        for vader in col:
                                            new_y = (vader.ycor() + self.mov_y)
                                            vader.goto(vader.xcor(), new_y)
                                            vader.change_shape()
                if time() - self.start_time > 1.7:
                    self.saucer_count += 1
                    print(self.saucer_count)
                    if self.timer_abs > 1:
                        self.timer_abs -= 1
                    self.start_time = time()

                self.timer = self.timer_abs


