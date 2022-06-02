from ludwig.api import LudwigModel
import pathlib
import numpy as np
from src.tnyml.prediction import Prediction

class LudwigHandler(object):
    MODEL_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent / "models"

    def __init__(self, model_name: str):
        model_dir: str = str(self.MODEL_DIR / model_name)
        # model = LudwigModel.load(model_dir)  # type: ignore
        # TODO: add data dict

    def predict(self, image: np.ndarray) -> Prediction:
        # TODO: if we use other models as well, we have to decide here
        # on how to handle each one

        # TODO: insert image to data dict
        # self.data["image"] = image
        # TODO: predict
        # model.predict(self.data, data_format="dict")
        # TODO: clean results folder as we don't need it
        prediction = Prediction("CAT", 0.9)
        return prediction