from flask import Flask, render_template, redirect
from threading import Thread
import logging
import library.sound as sound
import library.player as player
import config

app = Flask(__name__, template_folder=config.html_dir, static_folder=config.static_dir)

@app.route('/')
def home():
    return render_template('index_practice.html')

@app.route('/stop')
def stop():
    sound.stop_background()
    return redirect('/')

@app.route('/toggle_ads')
def toggle_ads():
    config.toggle_ads()
    return redirect('/')

@app.route('/stretching')
def stretching():
    sound.stretching_background()
    return redirect('/')

@app.route('/intro')
def intro():
    sound.play_intro_background()
    return redirect('/')

@app.route('/game_one')
def game_one():
    sound.first_game_background()
    return redirect('/')

@app.route('/game_two')
def game_two():
    sound.second_game_background()
    return redirect('/')

@app.route('/game_three')
def game_three():
    sound.third_game_background()
    return redirect('/')

@app.route('/match_point')
def match_point():
    sound.last_point_background()
    return redirect('/')

def start_practice():

    # disable flask logs
    log = logging.getLogger('werkzeug')
    log.disabled = True

    t = Thread(target =  lambda: app.run(host='0.0.0.0', debug=False, use_reloader=False, port=5001))
    t.daemon = True
    t.start()

    config.set_rescan_possible(True)

    while True:
        player.wait_for_scan()
