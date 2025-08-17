import library.sound as sound
import library.player as player

def stop():
    sound.stop_background()

def stretching():
    sound.stretching_background()
    player.wait_for_start()
    sound.stop_background()
    sound.play_intro()
   
def first_game():
    sound.first_game_background()
    player.wait_for_scan_no_score()

def second_game():
    sound.second_game_background()
    player.wait_for_scan_no_score()

def third_game():
    sound.third_game_background()
    player.wait_for_scan_no_score()

def last_game():
    sound.last_point_background()
    player.wait_for_scan_no_score()
