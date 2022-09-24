from typing import Tuple
from ludwig.api import LudwigModel
from pathlib import Path
import numpy as np
from pandas import DataFrame
from prediction import Prediction


class LudwigHandler(object):
    MODEL_DIR: Path = Path(__file__).parent.parent / "models"

    def __init__(self, model_name: str):
        self.model_dir: Path = self.MODEL_DIR / model_name
        self.model = LudwigModel.load(str(self.model_dir))

    def predict(self, image_path) -> Prediction:
        """makes a prediction for the given image

        Args:
            image_path(Path): full path of image to predict

        Returns:
            Prediction: A Prediction object containing the prediction and
                        confidence for given image
        """

        # path to image to predict
        images_to_predict = {"image_path": [str(image_path)]}

        all_predictions, _ = self.model.predict(dataset=images_to_predict)

        predicted_class = all_predictions.at[  # type: ignore
            0, "label_predictions"
        ]

        prediction_confidence = round(
            float(all_predictions.at[0, "label_probability"]), 3  # type: ignore
        )

        prediction = Prediction(predicted_class, prediction_confidence)
        return prediction
