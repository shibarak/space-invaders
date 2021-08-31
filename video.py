import cv2
import numpy as np
from time import time
from time import time, sleep
import mss


class Video:
    def __init__(self):
        self.idle = True
        self.time = time()
        self.screen_size = (1360, 1610)
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter("output3.mp4", self.fourcc, 20.0, (self.screen_size))
        self.screen_list = []
        self.monitor = {"top": 25, "left": 380, "width": 680, "height": 805}


    def get_screen(self):
        with mss.mss() as sct:
            scts = sct.grab(monitor=self.monitor)
            print(scts)
            self.screen_list.append(scts)

    def create_mp4(self):
        for screen in self.screen_list:
            frame = np.array(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            self.out.write(frame)

        cv2.destroyAllWindows()
        self.out.release()










s_time = time()





print(time() - s_time)

