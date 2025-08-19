import pygame
import pygame.time
import pygame.camera
import pygamevideo as video
from threading import Thread
import library.score as score
import sys
import config

def display_loop():
    global yellow_scored
    global blue_scored
    global even_the_odds
    global score_amount

    fullscreen = True
    pygame.init()
    pygame.camera.init()

    if fullscreen:
        display = pygame.display.set_mode((640,480), pygame.FULLSCREEN)
    else:
        display = pygame.display.set_mode((640,480))

    # pip install pygamevideo
    # define video file
    vid = video.Video(config.video_dir + "lain.mp4")

    # text to render on webcam feed
    font = pygame.font.SysFont('Arial', 50, bold=True)

    width, height = pygame.display.get_surface().get_size()

    # start webcam
    # cam = pygame.camera.Camera('/dev/video0')
    # cam.start()

    def text_even_the_odds():
        return font.render("EVENING THE ODDS", False, (0, 0, 0))

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

    # play the video
    vid.play()

    # display loop
    while True:

        display.fill((0,0,0))

        if vid.is_playing:

            vid.draw_to(display, (0, 0))

        else:
            vid.release()
            # img = cam.get_image()
            # display.blit(img,(0,0))

            display_score()

            if yellow_scored:
                text = text_yellow_score(score_amount)
                display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
                increase_timer()
                if timer > 3:
                        yellow_scored = False
                        reset_timer()

            if blue_scored:
                text = text_blue_score(score_amount)
                display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
                if timer > 3:
                        blue_scored = False
                        reset_timer()

            if even_the_odds:
                display.blit(text_even_the_odds(), (width/2,height/2))
                increase_timer()
                if timer > 3:
                        even_the_odds = False
                        reset_timer()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def display_loop_thread():
    t = Thread(target=display_loop)
    t.daemon = True
    t.start()

# helper functions for timing the display of which team scored

yellow_scored = False
blue_scored = False
even_the_odds = False
score_amount = 1

timer_start = 0
timer = 0

def start_timer():
   global timer_start
   timer_start = pygame.time.get_ticks()

def increase_timer():
    global timer
    global timer_start
    timer = (pygame.time.get_ticks() - timer_start) / 1000

def reset_timer():
    global timer
    global timer_start
    timer = 0
    timer_start = 0

def display_yellow_score(points):
    global yellow_scored
    global score_amount
    # set the score amount
    score_amount = points
    # set scored to True
    yellow_scored = True
    # start the timer
    start_timer()

def display_blue_score(points):
    global blue_scored
    global score_amount
    blue_scored = True
    score_amount = points
    start_timer()

def display_even_the_odds():
    global even_the_odds
    even_the_odds = True
    start_timer()
