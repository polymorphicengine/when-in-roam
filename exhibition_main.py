import library.player as player
import library.sound as sound
import library.led as led
import library.player as player
import random
import config

def beginning():
    sound.beginning_background()
    player.wait_for_scan_no_score()

def first_game():
    sound.start_game_one()
    sound.first_game_background()
    player.wait_for_scan_no_score()

def second_game():
    sound.start_game_two()
    sound.second_game_background()
    player.wait_for_scan_no_score()
  
def third_game():
    sound.start_game_three()
    sound.third_game_background()
    player.wait_for_scan_no_score()

def last_game():
    sound.start_match_point()
    sound.last_point_background()
    player.wait_for_scan_no_score()

def exhibition():
    beginning()
    first_game()
    second_game()
    third_game()
    last_game()


def gameLoop():
    while True:
        exhibition()

if __name__ == '__main__':
    try:
       config.rescan_possible = True
       gameLoop()
    finally:
       led.turn_off_red_light() 
       led.turn_off_green_light() 
