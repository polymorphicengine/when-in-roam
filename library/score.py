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

def even_second_game():
    global blue_score, yellow_score
    blue_score = config.third_game_score_condition
    yellow_score = config.third_game_score_condition

def even_last_game():
    global blue_score, yellow_score
    blue_score = config.last_game_score_condition - 1
    yellow_score = config.last_game_score_condition - 1

def get_score_blue():
    return blue_score

def get_score_yellow():
    return yellow_score
