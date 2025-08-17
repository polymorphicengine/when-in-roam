import config

blue_score = 0
yellow_score = 0


def add_points_blue(points):
    global blue_score
    blue_score = max(blue_score + points, 0)

def add_points_yellow(points):
    global yellow_score
    yellow_score = max(yellow_score + points, 0)

def second_game_condition():
    return max(blue_score, yellow_score) < config.second_game_score_condition

def third_game_condition():
    return max(blue_score, yellow_score) < config.third_game_score_condition

def last_game_condition():
    return max(blue_score, yellow_score) < config.last_game_score_condition

def shiners_won():
    if yellow_score >= config.last_game_score_condition:
         return True
    else:
         return False

def set_score_blue(num):
    global blue_score
    blue_score = num

def set_score_yellow(num):
    global yellow_score
    yellow_score = num

def get_score_blue():
    global blue_score
    return blue_score

def get_score_yellow():
    global yellow_score
    return yellow_score
