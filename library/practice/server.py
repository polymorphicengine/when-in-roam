from flask import Flask, render_template, request
from threading import Thread
import logging
import config
import library.practice.games as games


app = Flask(__name__, template_folder=config.html_dir, static_folder=config.static_dir)


@app.route('/')
def home():
    return render_template('index_practice.html')

@app.route('/stretching')
def stretching():
   games.stretching()
   return render_template('index_practice.html')

@app.route('/game_one')
def game_one():
   games.first_game()
   return render_template('index_practice.html')

@app.route('/game_two')
def game_two():
   games.second_game()
   return render_template('index_practice.html')
  
@app.route('/game_three')
def game_three():
   games.third_game()
   return render_template('index_practice.html')

@app.route('/match_point')
def match_point():
   games.last_game()
   return render_template('index_practice.html')

@app.route('/stop')
def stop():
   games.stop()
   return render_template('index_practice.html')


def startWebsite():
    Thread(target =  lambda: app.run(host='0.0.0.0', debug=False, use_reloader=False)).start()

def startDebug():
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

