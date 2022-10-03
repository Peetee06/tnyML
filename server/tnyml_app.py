import time
import connexion
from flask import render_template
from flask_cors import CORS

app = connexion.FlaskApp(__name__, specification_dir="openapi/")
app.add_api(
    "api_specification.yaml", strict_validation=True, validate_responses=True
)

flask_app = app.app

# allow origin 4200 to access everything inside /api/
CORS(flask_app)
# cors = CORS(
#     flask_app, resources={r"/api/*": {"origins": "http://localhost:4200"}}
# )


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.route("/", methods=["GET"])
def index():
    context = {"server_time": format_server_time()}
    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
