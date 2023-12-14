from flask import Flask
from .engine import Map, Engine
from .routes import setup_routes

app = Flask(__name__)

setup_routes(app)

@app.route('/play')
def play_game():
    return 'the game has begun'

if __name__ == "__main__":
    app.run(debug=True)
