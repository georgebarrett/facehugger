from flask import Flask
from .engine import Map, Engine

app = Flask(__name__)

@app.route('/play')
def play_game():
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    game_output = a_game.play()

    return 'the game has begun'