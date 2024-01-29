from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'your_secret_key'

    from app.routes import setup_routes
    setup_routes(app)

    return app