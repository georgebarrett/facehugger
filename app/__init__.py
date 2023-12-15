from flask import Flask, redirect, url_for
from .engine import Map, Engine
from .routes import setup_routes

app = Flask(__name__)

setup_routes(app)

app.secret_key = 'password'

@app.route('/')
def play_game():
    return redirect(url_for('central_corridor'))

if __name__ == "__main__":
    app.run(debug=True)
