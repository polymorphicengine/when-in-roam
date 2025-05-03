import config
import library.tts as tts
import library.sound as sound
from threading import Thread

max_secrets = config.max_secrets

secret_count_blue = 0
secret_count_yellow = 0

blue_team_is_ready = False
yellow_team_is_ready = False

wait_time = 1

def has_collected_all_blue():
    while not blue_team_is_ready:
       sound.wait(wait_time*60)
       if not blue_team_is_ready:
           sound.collected_all_sound_blue()

def has_collected_all_yellow():
    while not yellow_team_is_ready:
       sound.wait(wait_time*60)
       if not yellow_team_is_ready:
           sound.collected_all_sound_yellow()

def blue_team_ready():
   global blue_team_is_ready

   blue_team_is_ready = True

def yellow_team_ready():
   global yellow_team_is_ready

   yellow_team_is_ready = True

def get_secret_blue(text):
   global secret_count_blue
   global max_secrets

   tts.startTTS(text, 'B', secret_count_blue)
   secret_count_blue = secret_count_blue + 1

   Thread(target=sound.collect_secret_sound_blue, args=[secret_count_blue]).start()

   if secret_count_blue == max_secrets:
        Thread(target=has_collected_all_blue, args=[]).start()
        return True
   else:
        return False

def get_secret_yellow(text):
   global secret_count_yellow
   global max_secrets

   tts.startTTS(text, 'Y', secret_count_yellow)
   secret_count_yellow = secret_count_yellow + 1

   Thread(target=sound.collect_secret_sound_yellow, args=[secret_count_yellow]).start()

   if secret_count_yellow == max_secrets:
        Thread(target=has_collected_all_yellow, args=[]).start()
        return True
   else:
        return False

def undo_blue():
    global secret_count_blue
    if secret_count_blue > 0:
        secret_count_blue = secret_count_blue - 1
        Thread(target=sound.undo_secret_sound, args=[]).start()

def undo_yellow():
    global secret_count_yellow
    if secret_count_yellow > 0:
         secret_count_yellow = secret_count_yellow - 1
         Thread(target=sound.undo_secret_sound, args=[]).start()
