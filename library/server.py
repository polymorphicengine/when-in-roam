from flask import Flask, render_template, request, redirect
from threading import Thread
import logging
import library.secret as secret
import config

app = Flask(__name__, template_folder=config.html_dir, static_folder=config.static_dir)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blue_team')
def blue_team():
    return render_template('blue_team.html', secrets=secret.secret_count_blue)

@app.route('/yellow_team')
def yellow_team():
    return render_template('yellow_team.html', secrets=secret.secret_count_yellow)

@app.route('/submit_blue', methods=['POST'])
def submit_blue():

    user_input = request.form['user_input']
    done = secret.get_secret_blue(user_input)

    if done:
      return redirect('/blue_done')

    return redirect('/blue_team')

@app.route('/submit_yellow', methods=['POST'])
def submit_yellow():
    user_input = request.form['user_input']
    done = secret.get_secret_yellow(user_input)

    if done:
      return redirect('/yellow_done')

    return redirect('/yellow_team')

@app.route('/blue_done')
def blue_done():
   return render_template('blue_team_done.html')

@app.route('/yellow_done')
def yellow_done():
   return render_template('yellow_team_done.html')

@app.route('/blue_ready')
def blue_ready():
   secret.blue_team_ready()
   return render_template('blue_team_ready.html')

@app.route('/yellow_ready')
def yellow_ready():
   secret.yellow_team_ready()
   return render_template('yellow_team_ready.html')

@app.route('/undo_blue')
def undo_blue():
    secret.undo_blue()
    return redirect('/blue_team')

@app.route('/undo_yellow')
def undo_yellow():
    secret.undo_yellow()
    return redirect('/yellow_team')

def startWebsite():

    # disable flask logs
    log = logging.getLogger('werkzeug')
    log.disabled = True

    t = Thread(target =  lambda: app.run(host='0.0.0.0', debug=False, use_reloader=False))
    t.daemon = True
    t.start()

def startDebug():
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
