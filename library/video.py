import subprocess
import config

def play_video():
   global proc
   subprocess.call(["cvlc", config.video_dir+"INTRO_HD.mp4",  "--fullscreen", "--play-and-exit"])
