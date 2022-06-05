from typing import Any, Tuple
import pathlib
from ludwig_handler import LudwigHandler
from prediction import Prediction

# TODO: create model class


def make_prediction(model_name: str, image_url: str) -> Prediction:

    current_model = LudwigHandler(model_name)

    prediction = current_model.predict(image_url)

    return prediction


def get_models():
    # path to directory that contains the trained models
    models_path = pathlib.Path(__file__).parent.parent / "models"
    # list containing names of trained models
    models = [dir.stem for dir in models_path.iterdir() if dir.is_dir()]
    return models
