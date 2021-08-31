
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import cv2
import numpy as np
from time import time, sleep
import mss
from pynput import keyboard
import pickle

# To capture video and audio from space invaders run this script when the title screen appears.
# press the "q" key to exit the game and build the video.


screenshot = True

# Set video resolution/size
SCREEN_SIZE = (1360, 1610)
# codec for initial (audioless) screen capture
fourcc = cv2.VideoWriter_fourcc(*'mp4v')



def q_break(key):
    """
    function for the listener. When "q" key is pressed breaks the screencapture loop.
    :param key: a pynput "Key" object of the key captured by the listener.
    :return:
    """
    global screenshot
    try:
        print(key.char)
        if key.char == "q":
             screenshot = False
    except AttributeError:
        pass

# listen to keyboard
listener = keyboard.Listener(on_press=q_break)
listener.start()


screen_list = []
start_time = time()

# continually take screenshots of the game window and save them to a list. Takes ~20 fps.
while screenshot:
    sleep(.022)
    with mss.mss() as sct:
        monitor = {"top": 25, "left": 380, "width": 680, "height": 805}
        screen = sct.grab(monitor=monitor)
        print(screen)
        screen_list.append(screen)



frames = len(screen_list)
print(frames)
total_time = time() - start_time
print(total_time)

# sleep for 5 seconds to allow time for "audiolist.pkl" and audiotime.txt" to be created in main.py
sleep(5)

# open "audiolist.pkl" and audiotime.txt" in  this script
with open("audiolist.pkl", "rb") as file:
    audio_list = pickle.load(file)
with open("audiotime.txt", "r") as file:
    audio_time = float(file.read())

# find the optimal framerate for the video. So the video runs in real time.
native_frame_rate = round((frames / total_time), 2)

# set parameters for open cv VideoWriter
out = cv2.VideoWriter("SIcapture.mp4", fourcc, native_frame_rate, (SCREEN_SIZE))
# some stuff I printed just to give me a sense of what's going on.
print(f"native frame rate is {native_frame_rate}fps.")
print(f"start time is {start_time}")
print(f"audio start time is {audio_time}")
print(f"audio_list type is {type(audio_list)}")
# Figure out the time difference between when audio and video capture started to attempt to synch.
# This is always off by ~ 1 second either way.  Have to fix afterward.
time_dif = start_time - (audio_time - 0.5)
print(f"time difference is {time_dif}")

# create the silent video from the screenshots with open cv
for screen in screen_list:
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    out.write(frame)


cv2.destroyAllWindows()
out.release()

# use the audio_list from main.py to generate AudioFileClip objects using the original .wav files and put them in a list
clip_list = []
for item in audio_list:
    clip = AudioFileClip(filename=item["file"]).set_start(item["time"]-time_dif)
    clip_list.append(clip)

duration = (audio_list[-1]["time"] - time_dif)

# put all the audio files together into one composite and set the duration as the duration of the video
track = CompositeAudioClip(clips=clip_list).set_duration(t=duration)
# write the CompositeAudioClip object to an mp3 file
track.write_audiofile("track.mp3", fps=44100)

# make a moviepy VideoFileclip object from the silent screencap video we made earlier
clip = VideoFileClip("SIcapture.mp4")

# put together the audio and video and output a video playable on mac/ iOS
clip.write_videofile("SIwithaudio.mov",
                     codec="h264",
                     audio="track.mp3",
                     audio_codec="aac-lc",
                     temp_audiofile="temp-audio.m4a",
                     remove_temp=True)