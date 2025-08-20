import pygame
import library.score as score
import config

# setup sound
pygame.mixer.init(buffer=4096)

sounds_dir = config.sounds_dir

# wait in seconds
def wait(s):
    pygame.time.wait(int(s * 1000))

# play sound and wait until it is finished
def play_seq(s):
    s.play()
    wait(s.get_length())

def stop_background():
    pygame.mixer.music.stop()

def play_content(path):
    play_seq(pygame.mixer.Sound(path))

# char should be A, B or C
def play_ad(char, team):
    play_seq(pygame.mixer.Sound(sounds_dir + f'ads/{team}_ADVERT_{char}5.wav'))

def play_intro():
    play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/INTRO.wav'))

def play_intro_background():
    pygame.mixer.music.load(sounds_dir + 'commentator/INTRO.wav')
    pygame.mixer.music.play(loops=-1)

def play_outro_shiners():
    play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/OUTRO_SHINERS.wav'))

def play_outro_surfers():
    play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/OUTRO_SURFERS.wav'))

def play_outro_shiners_background():
    pygame.mixer.music.load(sounds_dir + 'commentator/OUTRO_SHINERS.wav')
    pygame.mixer.music.play(loops=-1)

def play_outro_surfers_background():
    pygame.mixer.music.load(sounds_dir + 'commentator/OUTRO_SURFERS.wav')
    pygame.mixer.music.play(loops=-1)

####################################################
################### SOUND EFFECTS ##################
####################################################

def scan_tag_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'fx/scan/scan_chip.wav'))

def before_secret_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/SECRET_REVEALED.wav'))

def after_secret_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'fx/AFTER_SECRET.wav'))

def undo_secret_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'fx/UNDO_SECRET.wav'))

####################################################
################# BACKGROUND SOUNDS ################
####################################################

def beginning_background():
    pygame.mixer.music.load(sounds_dir + 'background/1_Beginning.wav')
    pygame.mixer.music.play(loops=-1)

def stretching_background():
    pygame.mixer.music.load(sounds_dir + 'background/2_Stretching.wav')
    pygame.mixer.music.play(loops=-1)

def first_game_background():
    pygame.mixer.music.load(sounds_dir + 'background/3_First_Game.wav')
    pygame.mixer.music.play(loops=-1)

def second_game_background():
    pygame.mixer.music.load(sounds_dir + 'background/4_Second_Game.wav')
    pygame.mixer.music.play(loops=-1)

def third_game_background():
    pygame.mixer.music.load(sounds_dir + 'background/5_Third_Game.wav')
    pygame.mixer.music.play(loops=-1)

def last_point_background():
    pygame.mixer.music.load(sounds_dir + 'background/6_Last_Point.wav')
    pygame.mixer.music.play(loops=-1)

def half_time_music():
    play_seq(pygame.mixer.Sound(sounds_dir + 'halftime/HALFTIME_MUSIC.wav'))

###########################################################
################# SECRET COLLECTION SOUNDS ################
###########################################################

def collected_all_sound_blue():
    pygame.mixer.Sound(sounds_dir + "commentator/secret/TAG_B_s9.wav").play()

def collected_all_sound_yellow():
    pygame.mixer.Sound(sounds_dir + "commentator/secret/TAG_Y_s9.wav").play()

def collect_secret_sound_blue(num):
    # collect_secret_fx()
    play_seq(pygame.mixer.Sound(sounds_dir + f"commentator/secret/TAG_B_s{num}.wav"))

def collect_secret_sound_yellow(num):
    # collect_secret_fx()
    play_seq(pygame.mixer.Sound(sounds_dir + f"commentator/secret/TAG_Y_s{num}.wav"))

def collect_secret_fx():
    play_seq(pygame.mixer.Sound(sounds_dir + 'fx/scan/collect_secret.wav'))

################################################
################# POINTS SOUNDS ################
################################################

# played when blue scored points
def points_sound_blue(points):
    points_message_blue(points)
    # points_fx(points)

# played when yellow scored points
def points_sound_yellow(points):
    points_message_yellow(points)
    # points_fx(points)

def points_fx(points):
    play_seq(pygame.mixer.Sound(sounds_dir + f"fx/points/{points}_points.wav"))

def points_message_blue(points):
    match points:
        case -2:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_B_6.wav'))
        case 0:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_B_5.wav'))
        case 1:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_B_4.wav'))
        case 2:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_B_3.wav'))
        case 3:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_B_1-2.wav'))
        case _:
            print("Error in points_message_blue")

def points_message_yellow(points):
    match points:
        case -2:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_Y_6.wav'))
        case 0:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_Y_5.wav'))
        case 1:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_Y_4.wav'))
        case 2:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_Y_3.wav'))
        case 3:
            play_seq(pygame.mixer.Sound(sounds_dir + 'commentator/points/TAG_Y_1-2.wav'))
        case _:
            print("Error in points_message_yellow")

################################################
################# SYSTEM SOUNDS ################
################################################

def start_game_one():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/GAME_INTROS/GAME_ONE_INTRO.wav'))

def start_game_two():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/GAME_INTROS/GAME_TWO_INTRO.wav'))

def start_game_three():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/GAME_INTROS/GAME_THREE_INTRO.wav'))

def start_match_point():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/GAME_INTROS/MATCH_POINT_INTRO.wav'))

def score_sound():
 if score.blue_score >= score.yellow_score:
     team_blue_sound()
     score_number_sound(score.blue_score)
     team_yellow_sound()
     score_number_sound(score.yellow_score)
 else:
      team_yellow_sound()
      score_number_sound(score.yellow_score)
      team_blue_sound()
      score_number_sound(score.blue_score)

def score_number_sound(points):
    play_seq(pygame.mixer.Sound(sounds_dir + f"system/SCORE_{points}.wav"))

def team_blue_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/TEAM_B.wav'))

def team_yellow_sound():
    play_seq(pygame.mixer.Sound(sounds_dir + 'system/TEAM_Y.wav'))
