from typing import List
from ludwig.api import LudwigModel
from pathlib import Path
import pandas as pd
from prediction import Prediction


class LudwigHandler:
    """Class that handles all Ludwig model related tasks.

    Attributes:
        model_dir (:obj:`Path`): The path to the model's directory.
        model (:obj:`LudwigModel`): The LudwigModel object.

    """

    MODEL_DIR: Path = Path(__file__).parent.parent / "models"
    """The path to the pre-trained Ludwig models

        :meta hide-value:
    """

    @classmethod
    def get_models(cls):
        """Get all available models."""
        # list containing names of trained models
        models = [dir.stem for dir in cls.MODEL_DIR.iterdir() if dir.is_dir()]
        return models

    def __init__(self, model_name: str):
        """The constructor for the LudwigHandler class.

        Args:
            model_name (str): The name of the model to use.

        """
        self.model_dir: Path = self.MODEL_DIR / model_name
        self.model: LudwigModel = LudwigModel.load(str(self.model_dir))

    def predict(self, image_path: Path) -> Prediction:
        """Makes a prediction for the given image.

        Args:
            image_path (Path): Full path of image to predict.

        Returns:
            Prediction: A Prediction object containing the prediction
            and confidence for given image.
        """

        # path to the image to predict
        images_to_predict: dict[str, List[str]] = {
            "image_path": [str(image_path)]
        }

        # predictions returned by the model
        # make sure they are converted to DataFrame to enable typing checks
        all_predictions: pd.DataFrame = pd.DataFrame(
            self.model.predict(dataset=images_to_predict)[0]
        )

        # extract the predicted class
        predicted_class: str = all_predictions.at[0, "label_predictions"]

        # extract the predicted confidence
        prediction_confidence: float = round(
            float(all_predictions.at[0, "label_probability"]), 3
        )

        # create a Prediction object
        prediction: Prediction = Prediction(
            predicted_class, prediction_confidence
        )
        return prediction
