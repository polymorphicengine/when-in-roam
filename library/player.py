import library.nfc as nfc
import config
import library.score as score
import library.sound as sound
import library.ads as ads

def wait_for_scan():
  nfc.scan_and_play_once(on_scan)

def wait_for_scan_no_score():
  nfc.scan_and_play_once(lambda x, y, z: on_scan(x,y,z,False))

def wait_for_start():
    nfc.scan_for(config.start_card_id)

# given a tag id, select what should be played
def on_scan(team, player, num, score_enabled = True):

    content_file = decode_tag(team, player, num)
    points = number_score(num)
    is_secret = (num == 1) or (num == 2)

    # stop background
    sound.stop_background()

    # 1. scan sound effect
    sound.scan_tag_sound()

    # 1.5 if a secret is reveald play the special fx before
    if is_secret:
        sound.before_secret_sound()

    # 2. content sound
    sound.play_content(content_file)

    # 2.5 if a secret is reveald play the special fx after
    if is_secret:
        sound.after_secret_sound()

    madnum = None

    # 3. + 4. points message and soundeffect
    if team == 'Y':
        score.add_points_blue(points)
        madnum = ads.check_ad_blue()
        sound.points_sound_blue(points)

    if team == 'B':
        score.add_points_yellow(points)
        madnum = ads.check_ad_yellow()
        sound.points_sound_yellow(points)


    # 5. final score after round
    if score_enabled:
        sound.score_sound()

    # 6. maybe play an ad

    if madnum != None:
        sound.play_ad(*madnum)

    # print(f"Tag: {team}_{player}_{num}")


# there are two teams (Y and B) -> no need to decode
# there are 3 players per team (A, B, C) -> no need to decode
# there are 6 tags on each player, each tag stands for a different category and is associated with a fixed score
# 1, 2 & 3 for secret, 4 for media, 5 for money and 6 for fake


def decode_tag(team, player, num):
    if num != 1 and num != 2 and num != 3:
       return config.sounds_dir + f"game/{num}_{number_category(num)}/{team}_{number_category(num).upper()}_{player}{num}.wav"
    else:
       secret_number = compute_secret_number(player, num)
       return config.sounds_dir + f"game/1-2-3_SECRET/{team}_SECRET_{secret_number}.wav"

def number_category(num) -> str:
    match num:
        case 1:
            return "SECRET"
        case 2:
            return "SECRET"
        case 3:
            return "SECRET"
        case 4:
            return "MEDIA"
        case 5:
            return "MONEY"
        case 6:
            return "FAKE_SECRET"
        case _:
            raise Exception("Error in number_category")

def number_score(num):
    match num:
        case 1:
            return 2
        case 2:
            return 2
        case 3:
            return 2
        case 4:
            return 1
        case 5:
            return 1
        case 6:
            return 0
        case _:
            raise Exception("Error in number_score")

# player A ->  1, 4 and 7
# player B ->  2, 5 and 8
# player C ->  3, 6 and 9
def compute_secret_number(player, num):
    # returns 1 for A, 2 for B etc.
    player_num = ord(player.lower()) - 96

    return player_num + (num - 1)*3
