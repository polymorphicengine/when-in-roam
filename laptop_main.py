import library.sound as sound
import library.secret as secret
import library.server as server
import library.score as score
import library.nfc as nfc
import library.player as player
import library.ads as ads

# maximum amount of rounds
second_game_limit = 6

# tracks the rounds of game two
second_game_repetition = 0

def beginning():
    sound.beginning_background()
    server.startWebsite()
    while True:
       if secret.blue_team_is_ready and secret.yellow_team_is_ready:
           break

def second_game():
    global second_game_repetition
    sound.start_game_two()
    while score.second_game_condition():
       second_game_repetition = second_game_repetition + 1

       if second_game_repetition > second_game_limit:
           print("Moving on and evening the odds!")
           score.even_second_game()
           break

       else:
           sound.second_game_background()
           print(f'Round number:{second_game_repetition}')
           player.wait_for_scan()

try:
  second_game()
  # print(ads.to_char(1))
except Exception as e:
  print(e)
  nfc.close_nfc()
  print("Exiting...")
