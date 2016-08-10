#!/usr/bin/python3

import subprocess
from time import time, sleep
import curses

WORK = "WORK"
PAUSE = "PAUSE"
LONGER_PAUSE = "LONGER_PAUSE"
WORK_TIMEOUT = 25*60
PAUSE_TIMEOUT = 5*60
LONGER_PAUSE_TIMEOUT = 15*60

def play_sound(status, timeout, stdscr):
    """
    Plays the sound with totem.
    """
    start_time = time()
    while(time() - start_time < timeout):
        time_delta = (timeout - (time() - start_time))/60
        minutes = int(time_delta)
        seconds = int((time_delta - minutes)*60)
        stdscr.addstr(0, 0, "[*] {}: {}:{}".format(status, minutes, seconds),
                      curses.A_REVERSE)
        stdscr.refresh()
    subprocess.Popen(["totem", "/home/svieg/Downloads/dingdong.mp3"])
    sleep(3)
    subprocess.Popen(["pkill", "totem"])

def main(stdscr):
    """
    ALL OF THE LOGIC.
    """
    while True:
        for i in range(3):
            # Work
            play_sound(WORK, WORK_TIMEOUT, stdscr)
            # Pause
            play_sound(PAUSE, PAUSE_TIMEOUT, stdscr)

        play_sound(WORK, WORK_TIMEOUT, stdscr)
        play_sound(LONGER_PAUSE, LONGER_PAUSE_TIMEOUT, stdscr)

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    main(stdscr)
