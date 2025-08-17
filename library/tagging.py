import library.nfc as nfc
from flask import Flask, render_template, redirect, request
import logging
import config

app = Flask(__name__, template_folder=config.html_dir, static_folder=config.static_dir)

output = ""
last_team = "B"
last_player = "A"
last_number = 1

@app.route('/')
def home():
    return render_template('index_tagging.html', output = output, last_team = last_team, last_player = last_player, last_number = last_number)

@app.route('/', methods=['POST'])
def form():
    global output
    global last_team
    global last_player
    global last_number

    team = request.form['team']
    player = request.form['player']
    number = request.form['number']

    if check_valid(team, player, number):
        nfc.write_once(team, player, int(number))
        output = "Wrote to chip!"
        last_team = team

        if int(number) == 6:
            last_number = 1
            last_player = increase_player(player)
        else:
            last_number = int(number) + 1
            last_player = player
    else:
        output = "Incorrect input!"

    return redirect('/')

@app.route('/scan')
def scan():
    global output
    output = "Current TAG: " + str(nfc.scan())
    return redirect('/')

def start_tagging():
    # disable flask logs
    log = logging.getLogger('werkzeug')
    log.disabled = True

    app.run(host='0.0.0.0', debug=False, use_reloader=False, port=5001)

def check_valid(team, player, number):
    t = team in ['B', 'Y']
    p = player in ['A', 'B', 'C']
    n = number.isdigit()
    return (t and p and n)

def increase_player(player):
    match player:
        case 'A': return 'B'
        case 'B': return 'C'
        case _: return 'A'
