from pathlib import Path
import flask
from werkzeug.utils import secure_filename

from model_handler import ModelHandler
from config.config import get_upload_folder


def get_models():
    models = ModelHandler.get_models()
    return models


def predict(model_name):
    models = ModelHandler.get_models()
    if model_name not in models:
        flask.abort(
            404,
            description=(
                f"Model with name {model_name} not found. "
                f"Please use one of the following models: {models}"
            ),
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
    model_handler = ModelHandler(model_name)
    prediction = model_handler.predict(image_path)

    return prediction.to_json()
