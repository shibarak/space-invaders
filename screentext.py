from turtle import Turtle, register_shape, Screen

class Hide(Turtle):
    """
    A large black sprite almost the size of the screen.
    Used to hide tank, barrier and invader sprites when game is not
    in play.
    """
    def __init__(self):
        super(Hide, self).__init__()
        self.speed(0)
        register_shape("sprites/stars-static.gif")
        self.shape("sprites/stars-static.gif")
        self.hideturtle()
        self.goto(0, 38)
        self.penup()
        self.hideturtle()



    # test where to put the wall
    # def flash(self):
    #     if self.isvisible():
    #         self.hideturtle()
    #
    #     else:
    #         self.showturtle()


class Title(Turtle):
    """
    Turtle class object of the title screen logo
    """
    def __init__(self):
        super(Title, self).__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        register_shape("sprites/Space_Invaders_new.gif")
        self.shape("sprites/Space_Invaders_new.gif")
        self.goto(0, 38)
        self.showturtle()

class PressSpace(Turtle):
    """
    Turtle class object. Displays '<PRESS SPACEBAR>'
    """
    def __init__(self, screen: Screen):
        super(PressSpace, self).__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        register_shape("sprites/pressspace.gif")
        self.shape("sprites/pressspace.gif")
        self.goto(0, -150)
        self.showturtle()
        self.title_screen = True
        self.screen = screen

    def flash(self ):
        """
        flashes the PressSpace turtle.
        :return:
        """
        while self.title_screen:
            self.screen.delay(500)
            if self.isvisible():
                self.hideturtle()

            else:
                self.showturtle()


class BottomLine(Turtle):
    """
    Creates Turtle class object for the bottom green line
    """
    def __init__(self):
        super(BottomLine, self).__init__()
        self.speed(0)
        self.hideturtle()
        register_shape("sprites/b-line.gif")
        self.penup()
        self.shape("sprites/b-line.gif")
        self.goto(0, -303)
        self.showturtle()


class LivesText(Turtle):
    """
    Creates Turtle class object for the text displaying lives remaining
    """
    def __init__(self):
        super(LivesText, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.goto(-310, -377)

class Tank(Turtle):
    """
    creates a tank Turtle class object to display alongside lives text.
    Shows how many tanks in reserve.
    """
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        register_shape("sprites/tank.gif")
        self.shape("sprites/tank.gif")
        self.showturtle()


class Lives:
    """
    Handles the drawing of the lives text and display of the tanks
    """
    def __init__(self):
        self.text = LivesText()
        self.count = 3
        self.tank_1 = Tank()
        self.tank_1.goto(-260, -350)
        self.tank_2 = Tank()
        self.tank_2.goto(-190, -350)

    def draw(self):
        self.text.clear()
        self.text.write(arg=f"{self.count}", align="center",
                        font=("VP Pixel", 40, "normal"))
        if self.count == 3:
            self.tank_1.showturtle()
            self.tank_2.showturtle()
        elif self.count == 2:
            self.tank_2.hideturtle()
        elif self.count == 1:
            self.tank_1.hideturtle()


class GameOver(Turtle):
    def __init__(self):
        super(GameOver, self).__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        register_shape("sprites/gameover.gif")
        self.shape("sprites/gameover.gif")

class Paused(Turtle):
    def __init__(self):
        super(Paused, self).__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        register_shape("sprites/paused.gif")
        self.shape("sprites/paused.gif")


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-220, 342)
        self.count = 0
        self.draw()

    def draw(self):
        string_count = f"{self.count:05}"
        string_count = " ".join(string_count)
        self.clear()
        self.write(arg=f" S C O R E - {string_count}", align="center",
                   font=("VP Pixel", 25, "normal"))


class HiScore(Turtle):
    def __init__(self):
        super(HiScore, self).__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(180, 342)
        self.count = 0
        self.get_hi_score()
        self.draw()

    def draw(self):
        string_count = f"{self.count:05}"
        string_count = " ".join(string_count)
        self.clear()
        self.write(arg=f"H I - S C O R E - {string_count} ", align="center",
                   font=("VP Pixel", 25, "normal"))

    def get_hi_score(self):
        with open(file="hiscore.txt", mode="r") as data:
            self.count = int(data.read())

    def save_hi_score(self, score: int):
        if score > self.count:
            self.count = score
            with open(file="hiscore.txt", mode="w") as file:
                file.write(str(score))



class Level(Turtle):
    def __init__(self):
        super(Level, self).__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.number = 1

    def draw(self):
        string_number = f"{self.number:02}"
        string_number = " ".join(string_number)
        self.clear()
        self.write(arg=f"L E V E L - {string_number}", align="center",
                   font=("VP Pixel", 40, "normal"))









