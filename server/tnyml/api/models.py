from genericpath import isfile
from pathlib import Path
import flask
from werkzeug.utils import secure_filename

from ludwig_handler import LudwigHandler
from config.config import get_upload_folder


def get_models():
    models = LudwigHandler.get_models()
    return models


def predict(model_name):
    models = LudwigHandler.get_models()
    if model_name not in models:
        flask.abort(
            404,
            description=f"Model with name {model_name} not found. Please use one of the following models: {models}",
        )

    request_body: dict = dict(flask.request.json)  # type: ignore
    image_url: str = request_body.get("url")  # type: ignore
    # extract filename
    image_filename: str = image_url.split("/files/")[-1]
    image_filename = secure_filename(image_filename)
    if image_filename == "":
        flask.abort(400, "Invalid filename")
    image_path: Path = get_upload_folder() / image_filename

    if not image_path.is_file():
        flask.abort(400, "File not found")
    ludwig_handler = LudwigHandler(model_name)
    prediction = ludwig_handler.predict(image_path)

    return prediction.to_json()
