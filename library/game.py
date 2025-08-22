import library.sound as sound
import library.score as score
import library.player as player
import library.server as server
import library.secret as secret
import library.nfc as nfc
import library.display as display
import library.video as video
import config

second_game_round = 0
last_game_round = 0

def secret_collection():
    sound.beginning_background()
    server.startWebsite()
    while True:
       # wait until both teams are ready
       if secret.blue_team_is_ready and secret.yellow_team_is_ready:
           break

def stretching():
    sound.stretching_background()

    # wait for the start flag
    player.wait_for_start()
    sound.stop_background()

    # play intro video
    video.play_video()
    # after video finishes, start display
    display.start_display()

def first_game():
    sound.start_game_one()
    for i in range(config.first_game_repetitions):
      sound.first_game_background()
      player.wait_for_scan()

def second_game():
    global second_game_round
    sound.start_game_two()
    while score.second_game_condition():
       second_game_round = second_game_round + 1

       if second_game_round > config.second_game_limit:
           score.even_second_game()
           display.display_even_the_odds()
           sound.wait(2)
           display.stop_even_the_odds_display()
           break

       else:
           sound.second_game_background()
           player.wait_for_scan()

def half_time_show():

    # halftime show sound and image
    display.display_halftime()
    sound.half_time_music()
    display.stop_halftime_display()

    # wait for the start card again
    player.wait_for_start()

def third_game():
    sound.start_game_three()
    while score.third_game_condition():
       sound.third_game_background()
       player.wait_for_scan()

def last_game():
    global last_game_round

    while score.last_game_condition():

       last_game_round = last_game_round + 1
       player.wait_for_scan()

       if last_game_round > config.last_game_limit:
           score.even_last_game()
           display.display_even_the_odds()
           sound.wait(2)
           display.stop_even_the_odds_display()
           break
       else:
            sound.last_point_background()
            player.wait_for_scan()

    # if score has been evened we play a final round to determine the winner
    if score.get_score_blue() == score.get_score_yellow():
        sound.last_point_background()
        player.wait_for_last_scan()

def outro():
    if score.shiners_won():
        display.display_shiners()
        sound.play_outro_shiners()
        display.stop_shiners_display()
    else:
        display.display_surfers()
        sound.play_outro_surfers()
        display.stop_surfers_display()

def shutdown():
    nfc.close_nfc()

def performance():
    try:
        secret_collection()
        stretching()
        first_game()
        second_game()
        half_time_show()
        third_game()
        last_game()
        outro()
        shutdown()
    except:
        shutdown()
