import time
import os
from flask import Flask, jsonify, render_template;
from flask_cors import CORS;

app = Flask(__name__)
CORS(app)

data = [
    {
        "day": "1/6/2019",
    },
    {
        "day": "2/6/2019",
    }
]

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route("/", methods=['GET'])
def index():
    context = { 'server_time': format_server_time() }
    return render_template('index.html', context=context)

@app.route("/getData/", methods = ['GET'])
def getData():
    global data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=int(os.environ.get('PORT', 5000)))