from http.client import NO_CONTENT
import time
import os
from tkinter.messagebox import RETRY
from flask import (Flask, jsonify, render_template, 
                   request, redirect, send_file, 
                   send_from_directory, url_for, flash)
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from ludwig_handler import LudwigHandler

# FIXME: remove numpy when image retrieval is implemented
import numpy as np

UPLOAD_FOLDER = "flask/server/public/user/uploads/"
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}

app = Flask(__name__)

# allow origin 4200 to access everything inside /api/
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


modeldata = [
    {"model_id": 1, "description": "Cats and Dogs"},
    {"model_id": 2, "description": "Cars and Trucks"},
]

# all around data upload
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/api/uploadfile", methods=["POST"])
@cross_origin(supports_credentials=True)
def uploadFile():
    if "file" not in request.files:
        resp = jsonify({"message": "No file part in the request"})
        resp.status_code = 400
        return resp
    file = request.files["file"]
    if file.filename == "":
        resp = jsonify({"message": "No file selected for uploading"})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # type: ignore
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        resp = jsonify({"message": "File successfully uploaded"})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({"message": "Allowed file types are jpg, jpeg"})
        resp.status_code = 400
        return resp


# end upload section


@app.route("/api/getfile/<filename>", methods=["GET"])
@cross_origin(supports_credentials=True)
def getFile(filename):
    #  return 'welcome %s' % mytext
    path = "public\\user\\uploads\\" + filename
    return send_file(path)


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.route("/", methods=["GET"])
def index():
    context = {"server_time": format_server_time()}
    return render_template("index.html", context=context)


@app.route("/api/models", methods=["GET"])
def getData():
    # TODO: models = tnymlModel.get_data()
    global modeldata
    return jsonify(modeldata)


@app.route("/api/models/{model_id}", methods=["POST"])
def predict(model_id):
    # TODO: get image from POST body
    image = np.array((3,3))
    # TODO: get modeldata
    global modeldata
    # TODO: get model from modeldata
    for model in modeldata:
        if model["model_id"] == model_id:
            model_name = model["description"]
            current_model = LudwigHandler(model_name)
            prediction = current_model.predict(image)
            # TODO: create prediction resource
            # /api/models/{model_id}/{prediction_id}
            # TODO: return prediction URL
            return jsonify(prediction)

    # TODO: if wanted model_id does not exist return 404 not found or sth

@app.route("/api/models/{model_id}/{prediction_id}", methods=["GET"])
def predictions(model_id, prediction_id):
    # TODO: access model_id and prediction_id and return the prediction
    return "TODO"


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))

