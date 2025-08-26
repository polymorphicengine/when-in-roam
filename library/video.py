import subprocess
import config
import os

def play_video():
   global proc
   os.environ['DISPLAY'] = ':0.0'
   subprocess.call(["cvlc", config.video_dir+"INTRO.mp4",  "--fullscreen", "--play-and-exit"])
