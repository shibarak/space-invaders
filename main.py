import time
from turtle import Screen

import simpleaudio as sa

import pickle
from audio import Audio
from barrier import Barrier
from bullet import Bullet, Bullets
from invaders import Invaders
from tank import Tank
from zaps import Zaps
from screentext import Title, PressSpace, Hide, BottomLine, Lives, GameOver, Score, HiScore, Level, Paused

# ------------------- Sounds --------------------------------------------------- #

laser = sa.WaveObject.from_wave_file("audio/laser-2.wav")
shot = sa.WaveObject.from_wave_file("audio/shoot.wav")
inv_kill = sa.WaveObject.from_wave_file("audio/invaderkilled.wav")
splode = sa.WaveObject.from_wave_file("audio/explosion.wav")
ufo_wav = sa.WaveObject.from_wave_file("audio/ufo_lowpitch.wav")

move_sound_i = 0

# --------------------------------- functions ------------------------------------------ #


def done():
    """
    Quits the game and writes the audio.time and audio.list to a .txt and.pkl
    file respectively so they can be accessed by video-main.py to create a video
    of the gameplay (if video-main.py is running).
    :return:
    """
    audio.running = False

    str_time = str(audio.time)
    with open("audiolist.pkl", "wb") as file:
        pickle.dump(audio.list, file)
    with open("audiotime.txt", "w")  as file:
        file.write(str_time)
    screen.bye()


def move_sound():
    """
    Every time the invzders move this function plays  one of four
    move sounds and cycles to the next sound in the list. Once all four sounds have
    been played it resets to the first sound.
    :return: 
    """
    global move_sound_i
    move_sounds = [sa.WaveObject.from_wave_file("audio/1.wav"),
                   sa.WaveObject.from_wave_file("audio/2.wav"),
                   sa.WaveObject.from_wave_file("audio/3.wav"),
                   sa.WaveObject.from_wave_file("audio/4.wav"),
                   ]
    if invaders.moved:
        move_sounds[move_sound_i].play()
        ad = {"file": f"audio/{move_sound_i+1}.wav",
              "time": (time.time() - audio.time) }

        audio.list.append(ad)
        if move_sound_i == 3:
            move_sound_i = 0
        else:
            move_sound_i += 1


def move_handler(x):
    """
    allows the tank sprite to track the cursor using the Screen.onmove method
    I've added to the turtle library
    :param x: x axis value of the mouse cursor
    :return:
    """
    screen.onmove(None)  # avoid overlapping events
    tank.penup()
    if not invaders.pause:
        if 330 > x > -330:
            tank.setheading(tank.towards(x, -250))
            tank.goto(x, -275)
        screen.onmove(move_handler)
    else:
        pass


def shoot(x, y):
    """
    creates a Bullet object at time and position of click and plays the shot wav file.
    :param x:
    x axis position of cursor at time of click
    :param y:
    y axis position of cursor at time of click
    :return:
    """
    bullets.b_list.append(Bullet(x))
    shot.play()
    ad = {"file": f"audio/shoot.wav",
          "time": (time.time() - audio.time)}
    audio.list.append(ad)


def pause():
    """
    Tied to screen.onkey("p").
    Stops all inputs and motion and displays "PAUSED"  when the "p" key is pressed while
    preserving game state.  resumes when unpaused.
    :return:
    """
    if not invaders.pause:
        invaders.pause = True
        zaps.pause = True
        paused.showturtle()
        for z in zaps.z_list:
            z.pause = True
        for b in bullets.b_list:
            b.pause = True
        screen.onclick(None)
    else:
        invaders.pause = False
        zaps.pause = False
        paused.hideturtle()
        for z in zaps.z_list:
            z.pause = False
        for b in bullets.b_list:
            b.pause = False
        screen.onclick(shoot)


def bullet_handler():
    """
    Handles the Bullet class objects in the Bullets object b_list.
    detects collisions with Invader objects and Brick objects in the barriers, as well
    as when the bullet reaches the upper bounds of the screen.
    :return:
    """
    if len(bullets.b_list) >= 1:  # limit number of bullets on screen
        screen.onclick(None)
    else:
        if not invaders.pause:
            screen.onclick(shoot)
    for b in bullets.b_list:
        b.move()
        if b.distance(invaders.saucer) < 30 and b.ycor() > (invaders.saucer.ycor() + 2):
            score.count += invaders.saucer.points
            score.draw()
            invaders.saucer.current_shape = invaders.saucer.shape_2
            invaders.saucer.shape(invaders.saucer.current_shape)
            inv_kill.play()
            ad = {"file": "audio/invaderkilled.wav",
                  "time": (time.time() - audio.time)}
            audio.list.append(ad)
            b.hideturtle()
            try:
                bullets.b_list.remove(b)
            except ValueError:
                pass

        for br in barrier.brick_list:
            if br.isvisible():
                if b.distance(br) < 11 and b.ycor() > (br.ycor() + .5):
                    print(len(barrier.brick_list))
                    b.hideturtle()
                    b.goto(5000, 5000)
                    if br.current_shape == br.shape_1:
                        br.current_shape = br.shape_2
                        br.shape(br.current_shape)
                    else:
                        br.hideturtle()
        for col in invaders.invader_list:
            for inv in col:
                if inv.isvisible():
                    if b.distance(inv) < 20 and b.ycor() < (inv.ycor() + 2):
                        score.count += inv.points
                        score.draw()
                        inv.current_shape = inv.shape_3
                        inv.shape(inv.current_shape)
                        inv_kill.play()
                        ad = {"file": "audio/invaderkilled.wav",
                              "time": (time.time() - audio.time)}
                        audio.list.append(ad)
                        b.hideturtle()
                        try:
                            b.hideturtle()
                            bullets.b_list.remove(b)
                            print(bullets.b_list)
                        except ValueError:
                            pass
        if b.ycor() > 330:  # delete offscreen bullets
            b.shape("sprites/bullet-splode.gif")
            bullets.dead_b_list.append(b)
            try:
                bullets.b_list.remove(b)
            except ValueError:
                pass
    for b in bullets.dead_b_list:
        if b.timer == 0:
            b.hideturtle()
            bullets.dead_b_list.remove(b)
        else:
            b.timer -= 1


def game_over():
    """
    Displays the game over text and returns the game to it's initial level-01 state.
    :return:
    """
    invaders.timer_abs = 35
    level.number = 1
    invaders.interval = 1.7
    invaders.init_y = 270
    invaders.saucer_count = 10
    zaps.limiter_abs = 20
    invaders.saucer.hideturtle()
    invaders.saucer.goto(-380, 330)
    invaders.saucer.showturtle()
    invaders.saucer_count = 0
    for b in bullets.b_list:
        b.hideturtle()
        b.goto(1000, 1000)
    for zap in zaps.z_list:
        zap.hideturtle()
        zap.goto(1000, 1000)
    zaps.z_list = []
    hide.showturtle()
    g_over.showturtle()
    hi_score.save_hi_score(score.count)
    hi_score.draw()
    screen.update()
    barrier.show()
    invaders.reset()
    screen.onkey(fun=game, key="space")
    hide.showturtle()
    g_over.showturtle()
    tank.shape("sprites/tank.gif")
    screen.update()
    score.count = 0
    lives.count = 3
    print(audio.list)



def next_level():
    """
    When every Invader object has been destroyed (i.e. made not visible with hideturtle())
    resets the invaders, barriers, bottom boundary line, and changes variables
    (invader move speed, invader starting position, invader shot speed, etc.)
    to increase the difficulty for the next level.
    :return:
    """

    hide.showturtle()
    screen.update()
    screen.onclick(None)
    level.number += 1
    invaders.interval -= .3
    invaders.timer_abs -= 6
    invaders.init_y -= 35
    invaders.saucer_count += 4
    zaps.limiter_abs -= 2
    for b in bullets.b_list:
        b.hideturtle()
        b.goto(1000, 1000)
    for zap in zaps.z_list:
        zap.hideturtle()
        zap.goto(1000, 1000)
    zaps.z_list = []
    hide.showturtle()
    level.draw()
    invaders.reset()
    barrier.show()
    time.sleep(2)


def game():
    '''
    starts and runs the standard game mode.  loops while the invaders.game
    attribute is true.
    :return:
    invaders.game = False
    '''
    press_space.title_screen = False
    invaders.game = True
    BottomLine()
    screen.onkey(fun=None, key="space")
    score.draw()
    lives.draw()
    level.clear()
    g_over.hideturtle()
    title.hideturtle()
    press_space.hideturtle()
    hide.hideturtle()
    invaders.start_time = time.time()
    screen.onkey(fun=done, key="q")
    screen.onkey(fun=pause, key="p")
    screen.onclick(shoot)
    screen.listen()
    screen.update()
    while invaders.game:
        invaders.completed = True
        screen.onmove(move_handler)
        screen.tracer(0)
        invaders.move()
        bullet_handler()
        move_sound()
        zaps.timer()
        # play sound when UFO comes on screen
        if invaders.saucer.xcor() == -372:
            ufo_wav.play()
            ad = {"file": f"audio/ufo_lowpitch.wav",
                  "time": (time.time() - audio.time)}
            audio.list.append(ad)
        # Handles the Invader objects in invaders.invader_list:
        #  - Checks if they are currently visible
        #  - Has them fire if the ank is underneath (and moving... a bug i haven't been able to fix)
        #  - Checks for collision with the barriers and (if you've really messed up) the tank.
        for col in invaders.invader_list:
            for i in range(0, 5):
                inv = col[i]
                if inv.isvisible():
                    invaders.completed = False
                    if abs(tank.xcor() - inv.xcor()) < 5:
                        try:
                            if not col[i+1].isvisible():
                                zaps.zap_em(x=inv.xcor(), y=inv.ycor())
                        except IndexError:
                            zaps.zap_em(x=inv.xcor(), y=inv.ycor())
                    for br in barrier.brick_list:
                        if br.isvisible():
                            if inv.distance(br) < 17 and inv.ycor() > (br.ycor() - 2):
                                br.hideturtle()

                    if inv.distance(tank) < 17 and inv.ycor() > (tank.ycor() - 2):
                        lives.count = 0
                        lives.draw()
                        screen.update()
                        game_over()
                        invaders.game = False
                        return


        # Handles the Zap (what i called the Invaders shots) objects in zaps.zap_list:
        #  - Checks for collision with the barriers and the tank.
        #  - if the tank is hit destroys the tank, plays the explosion sound, lowers lives, etc
        #  - triggers game ver if lives reach 0
        #  - lastly check if the zap has hit the bottom line, changes zap into bottom line damage sprite.
        for z in zaps.z_list:
            z.move()
            if z.current_shape == z.shape_1:
                z.current_shape = z.shape_2
                z.shape(z.current_shape)
            else:
                z.current_shape = z.shape_1
                z.shape(z.current_shape)
            if z.distance(tank) < 20 and z.ycor() > (tank.ycor() - 2):
                screen.onmove(None)
                lives.count -= 1
                lives.draw()
                screen.update()
                splode.play()
                ad = {"file": f"audio/explosion.wav",
                      "time": (time.time() - audio.time)}
                audio.list.append(ad)
                z.hideturtle()
                z.goto(5000, 5000)
                try:
                    zaps.z_list.remove(z)
                except ValueError:
                    pass
                for i in range(5):
                    tank.shape("sprites/tank-splode.gif")
                    screen.update()
                    time.sleep(.1)
                    tank.shape("sprites/tank-splode2.gif")
                    screen.update()
                    time.sleep(.1)
                if lives.count <= 0:
                    game_over()
                    invaders.game = False
                    return
                screen.onmove(move_handler)
                tank.shape("sprites/tank.gif")
            for br in barrier.brick_list:
                if br.isvisible():
                    if z.distance(br) < 12 and z.ycor() > (br.ycor() - 2):
                        print(len(barrier.brick_list))
                        z.hideturtle()
                        z.goto(5000, 5000)
                        try:
                            zaps.z_list.remove(z)
                        except ValueError:
                            pass
                        if br.current_shape == br.shape_1:
                            br.current_shape = br.shape_2
                            br.shape(br.current_shape)
                        else:
                            br.hideturtle()
            if z.ycor() <= -310:
                z.goto(z.xcor(), -320)
                z.shape("sprites/ishot-dead.gif")
                try:
                    zaps.z_list.remove(z)
                except ValueError:
                    pass
        if invaders.completed:
            next_level()
            game()
        screen.update()
        time.sleep(0.0)


# ----------------------- Create Objects, setup --------------------#

screen = Screen()
screen.title("Space Invaders")
screen.setup(680, 820)
screen.bgcolor("black")


lives = Lives()
tank = Tank()
bullets = Bullets()
zaps = Zaps()
invaders = Invaders()
barrier = Barrier()
score = Score()
hi_score = HiScore()
hide = Hide()
g_over = GameOver()
paused = Paused()
level = Level()

screen.listen()
screen.onkey(fun=game, key="space")
audio = Audio()
title = Title()
press_space = PressSpace(screen)
press_space.flash()

screen.mainloop()