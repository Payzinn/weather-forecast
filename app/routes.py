from flask import Blueprint, render_template, request, redirect, url_for, current_app, jsonify
from dadata import Dadata
import sqlite3

main = Blueprint('main', __name__)

def add_city_to_database(city):
    conn = sqlite3.connect('weather_requests.db')
    c = conn.cursor()
    c.execute('SELECT * FROM weather_requests WHERE city=?', (city,))
    result = c.fetchone()
    if result:
        c.execute('UPDATE weather_requests SET count = count + 1 WHERE city=?', (city,))
    else:
        c.execute('INSERT INTO weather_requests (city, count) VALUES (?, ?)', (city, 1))
    conn.commit()
    conn.close()

@main.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    previous_cities = []

    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = current_app.weather_api.get_weather(city)
        # print(f"Weather data: {weather_data}")
        if 'error' not in weather_data:
            add_city_to_database(city)
            return redirect(url_for('main.index', city=city))

    city = request.args.get('city')  
    if city:
        weather_data = current_app.weather_api.get_weather(city)
       
    conn = sqlite3.connect('weather_requests.db')
    c = conn.cursor()
    c.execute('SELECT city, count FROM weather_requests ORDER BY count DESC')
    rows = c.fetchall()
    previous_cities = {city: count for city, count in rows}
    conn.close()

    return render_template('index.html', weather_data=weather_data, previous_cities=previous_cities)

dadata_token = "5f96d915308a5c61ce2699cb014ea08ecb8530ba"

@main.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '')
    if query:
        dadata = Dadata(dadata_token)
        result = dadata.suggest("address", query, from_bound={"value": "city"}, to_bound={"value": "city"})      
        suggestions = [item['value'] for item in result if item['data'].get('city')]
        return jsonify(suggestions)
    return jsonify([])
