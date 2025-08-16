import library.sound as sound
import library.score as score
import library.player as player
import config

second_game_round = 1

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
