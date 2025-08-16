# game configuration
max_secrets = 8

first_game_repetitions = 3

second_game_score_condition = 8
second_game_limit = 6

third_game_score_condition = 13

# amount of points needed for win
last_game_score_condition = 16
last_game_limit = 2

# when true, tags can be triggered multiple times
rescan_possible = False

# after how many points to trigger ads
ads_repetition = 5

# turn ads on / off
play_ads = True

start_card_id = bytearray(b')N@\x05')

piper_dir = "/home/martin/git/when-in-roam/piper/"

# asset directories
sounds_dir = "/home/martin/git/when-in-roam/sounds/"
html_dir = "/home/martin/git/when-in-roam/html"
static_dir = "/home/martin/git/when-in-roam/html/static"

def is_rescan_possible():
    return rescan_possible

def set_rescan_possible(bool):
    global rescan_possible
    rescan_possible = bool

def should_play_ads():
    return play_ads

def toggle_ads():
    global play_ads
    play_ads = not play_ads
