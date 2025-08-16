import config
import library.score as score

repetition = config.ads_repetition

ad_state_blue = 1
ad_state_yellow = 1

def to_char(num, team):
    match num:
       case 1: return ('A', team)
       case 2: return ('B', team)
       case _: return ('C', team)

def check_ad_blue():
         global ad_state_blue


         # if ads are turned off return None
         if not config.should_play_ads():
             return None

         sc = score.get_score_blue()

         # otherwise, check the score to see if ad should be played
         # if it should, return the a tuple to identify which ad
         if ad_state_blue * repetition <= sc:
                 ad_state_blue = ad_state_blue + 1
                 return to_char(ad_state_blue, 'B')

def check_ad_yellow():
         global ad_state_yellow

         if not config.should_play_ads():
             return None

         sc = score.get_score_yellow()

         if ad_state_yellow * repetition <= sc:
                 ad_state_yellow = ad_state_yellow + 1
                 return to_char(ad_state_yellow, 'Y')
