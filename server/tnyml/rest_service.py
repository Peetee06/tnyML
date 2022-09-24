from http.client import NO_CONTENT
import time
import os
from tkinter.messagebox import RETRY
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    send_file,
    send_from_directory,
    url_for,
    flash,
)
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from pathlib import Path

import model

UPLOAD_FOLDER = Path(__file__).parent.parent / "public" / "user" / "uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}

app = Flask(__name__)

# allow origin 4200 to access everything inside /api/
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# all around data upload
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/api/uploadfile", methods=["POST"])
@cross_origin(supports_credentials=True)
def uploadFile():
    # TODO: return url to uploaded file
    # TODO make sure there are no conflicts in saved files
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
        image_path = app.config["UPLOAD_FOLDER"] / filename
        file.save(image_path)
        resp = jsonify({"image_url": f"/api/getfile/{filename}"})
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
    image_path = app.config["UPLOAD_FOLDER"] / filename
    return send_file(image_path)


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.route("/", methods=["GET"])
def index():
    context = {"server_time": format_server_time()}
    return render_template("index.html", context=context)


@app.route("/api/models", methods=["GET"])
def getData():
    models = model.get_models()
    return jsonify(models)


@app.route("/api/models/<model_name>", methods=["POST"])
def predict(model_name):
    image_url = dict(request.json)["url"]  # type: ignore
    # extract filename
    image_filename = image_url.split("/getfile/")[-1]

    image_path = app.config["UPLOAD_FOLDER"] / image_filename

    prediction = model.make_prediction(model_name, image_path)    

    response = jsonify(prediction.__dict__)
    return response
    # TODO: if wanted model_name does not exist return 404 not found or sth

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
