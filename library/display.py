import pygame
import pygame.time
import pygame.camera
from threading import Thread
import library.score as score
import sys
import config

def display_loop():
    global yellow_scored
    global blue_scored
    global even_the_odds
    global score_amount
    global half_time
    global vid

    fullscreen = True
    pygame.init()
    pygame.camera.init()

    if fullscreen:
        resolution = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        display = pygame.display.set_mode(resolution, pygame.NOFRAME)
    else:
        display = pygame.display.set_mode((640,480))

    halftime_image = pygame.image.load(config.video_dir + 'HALFTIME_BACKGROUND.jpg')

    # text to render on webcam feed
    font = pygame.font.SysFont('Arial', 250, bold=True)

    width, height = pygame.display.get_surface().get_size()

    # start webcam
    # cam = pygame.camera.Camera('/dev/video0')
    # cam.start()

    def text_even_the_odds():
        return font.render("EVENING THE ODDS", False, (255, 0, 0))

    def text_shiners_won():
        return font.render("THE SHINERS WON THE ROAMING TOURNAMENT", False, (0, 255, 0))

    def text_surfers_won():
        return font.render("THE SURFERS WON THE ROAMING TOURNAMENT", False, (0, 0, 255))

    def text_blue_score(points):
        return font.render(f'The Surfers Scored {points} points!', False, (0, 0, 255))

    def text_yellow_score(points):
        return font.render(f'The Shiners Scored {points} points!', False, (255, 255, 0))

    # render the current score
    def display_score():
        yellow = score.get_score_yellow()
        blue = score.get_score_blue()

        sc_y = font.render(f'{yellow}', False, (255, 255, 0))
        sc_b = font.render(f'{blue}', False, (0, 0, 255))

        display.blit(sc_y, (sc_y.get_width(), height/2))
        display.blit(sc_b, (width - sc_b.get_width()*2, height/2))

    # display loop
    while True:

        display.fill((0,0,0))

        display_score()

        if yellow_scored:
            text = text_yellow_score(score_amount)
            display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))

        if blue_scored:
            text = text_blue_score(score_amount)
            display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))

        if even_the_odds:
            text = text_even_the_odds()
            display.blit(text, (width/2 - text.get_width()/2,height/3 - text.get_height()/2))

        if half_time:
            display.blit(halftime_image, (0,0))

        if shiners_won:
            text = text_shiners_won()
            display.blit(text, (width/2 - text.get_width()/2, height/3 - text.get_height()/2))

        if surfers_won:
            text = text_surfers_won()
            display.blit(text, (width/2 - text.get_width()/2, height/3 - text.get_height()/2))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def start_display():
    t = Thread(target=display_loop)
    t.daemon = True
    t.start()

# helper functions to toggle the display of text
# from other threads and conditions

yellow_scored = False
blue_scored = False
even_the_odds = False
half_time = False
shiners_won = False
surfers_won = False
score_amount = 1

def display_yellow_score(points):
    global yellow_scored
    global score_amount
    # set the score amount
    score_amount = points
    # set scored to True
    yellow_scored = True

def display_blue_score(points):
    global blue_scored
    global score_amount
    blue_scored = True
    score_amount = points

def stop_scored_display():
    global blue_scored
    global yellow_scored
    blue_scored = False
    yellow_scored = False

def stop_even_the_odds_display():
    global even_the_odds
    even_the_odds = False

def display_even_the_odds():
    global even_the_odds
    even_the_odds = True

def display_halftime():
    global half_time
    half_time = True

def stop_halftime_display():
    global half_time
    half_time = False

def display_shiners():
    global shiners_won
    shiners_won = True

def stop_shiners_display():
    global shiners_won
    shiners_won = False

def display_surfers():
    global surfers_won
    surfers_won = True

def stop_surfers_display():
    global surfers_won
    surfers_won = False
