# game configuration
max_secrets = 2

# set period of announcing that team is ready to start (in minutes)
ready_to_start_period = 3

first_game_repetitions = 3

second_game_score_condition = 9
second_game_limit = 6

third_game_score_condition = 14

# amount of points needed for win
last_game_score_condition = 16
last_game_limit = 2

# when true, tags can be triggered multiple times
rescan_possible = True

# after how many points to trigger ads
ads_repetition = 6

# turn ads on / off
play_ads = True

start_card_id = bytearray(b'\xaaSn\x05')
              # actual flag: bytearray(b'\x04X\xfb:@Y\x80')

piper_dir = "/home/martin/git/when-in-roam/piper/"

# asset directories
sounds_dir = "/home/martin/git/when-in-roam/sounds/"
video_dir = "/home/martin/git/when-in-roam/video/"
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
