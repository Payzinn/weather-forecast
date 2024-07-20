from flask import Flask
from .weather_api import WeatherAPI
from .routes import main
import sqlite3

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('APP_SETTINGS', silent=True)

    app.weather_api = WeatherAPI()

    with app.app_context():
        conn = sqlite3.connect('weather_requests.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS weather_requests (
                id INTEGER PRIMARY KEY,
                city TEXT NOT NULL,
                count INTEGER DEFAULT 1
            )
        ''')
        conn.commit()
        conn.close()

    app.register_blueprint(main)

    return app
