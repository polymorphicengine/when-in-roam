import library.sound as sound
import library.score as score
import library.player as player
import library.server as server
import library.secret as secret
import library.nfc as nfc
import config

second_game_round = 1
last_game_round = 1

def secret_collection():
    sound.beginning_background()
    server.startWebsite()
    while True:
       # wait until both teams are ready
       if secret.blue_team_is_ready and secret.yellow_team_is_ready:
           break

def stretching():
    sound.stretching_background()
    player.wait_for_start()
    sound.stop_background()
    sound.play_intro()

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
           break

       else:
           sound.second_game_background()
           player.wait_for_scan()

def half_time_show():
    return

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
           break
       else:
            sound.last_point_background()
            player.wait_for_scan()

    # if score has been evened we play a final round to determine the winner
    # TODO: what if a team then only scores 0 points?
    if score.get_score_blue() == score.get_score_yellow():
        sound.last_point_background()
        player.wait_for_scan()

def outro():
    if score.shiners_won():
        sound.play_outro_shiners()
    else:
        sound.play_outro_surfers()

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
