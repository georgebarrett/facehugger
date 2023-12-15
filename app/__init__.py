from flask import Flask, redirect, url_for, render_template
from .engine import Map, Engine
from .routes import setup_routes

app = Flask(__name__)

setup_routes(app)

app.secret_key = 'password'

if __name__ == "__main__":
    app.run(debug=True)
