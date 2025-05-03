import library.server as server
import library.player as player
import library.sound as sound
import library.secret as secret
import library.score as score
import library.led as led
import config

def beginning():
    led.turn_off_red_light()
    sound.beginning_background()
    server.startWebsite()
    while True:
       if secret.blue_team_is_ready and secret.yellow_team_is_ready:
           break

def stretching():
    led.turn_on_red_light()
    sound.stretching_background()
    player.wait_for_start()
    sound.stop_background()
    sound.play_intro()

def first_game():
    sound.start_game_one()
    for i in range(config.first_game_repetitions):
      sound.first_game_background()
      led.turn_on_red_light()
      player.wait_for_scan()

def second_game():
    sound.start_game_two()
    while score.second_game_condition():
       sound.second_game_background()
       led.turn_on_red_light()
       player.wait_for_scan()

def third_game():
    sound.start_game_three()
    while score.third_game_condition():
       sound.third_game_background()
       led.turn_on_red_light()
       player.wait_for_scan()

def last_game():
    while score.last_game_condition():
       sound.last_point_background()
       led.turn_on_red_light()
       player.wait_for_scan()

def performance():
    # beginning()
    # stretching()
    first_game()
    second_game()
    third_game()
    last_game()

if __name__ == '__main__':
    try:
      performance()
    finally:
      led.turn_off_red_light() 
      led.turn_off_green_light() 
    # first_game()
    # server.startDebug()
