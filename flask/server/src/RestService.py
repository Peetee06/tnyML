import time
import os
from flask import Flask, jsonify, render_template;
from flask_cors import CORS;
# from flask_restful import Resource, Api;


app = Flask(__name__)
# api=Api(app)
CORS(app)

weather = [
    {
        "day": "1/6/2019",
        "temperature": "23",
        "windspeed": "16",
        "event": "Sunny"
    },
    {
        "day": "2/6/2019",
        "temperature": "21",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "3/6/2019",
        "temperature": "31",
        "windspeed": "12",
        "event": "Sunny"
    },
    {
        "day": "4/6/2019",
        "temperature": "5",
        "windspeed": "28",
        "event": "Snow"
    }
]

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route("/", methods=['GET'])
def index():
    context = { 'server_time': format_server_time() }
    return render_template('index.html', context=context)

@app.route("/weatherReport/", methods = ['GET'])
def WeatherReport():
    global weather
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True,port=int(os.environ.get('PORT', 5000)))