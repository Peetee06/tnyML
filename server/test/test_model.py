from pathlib import Path

from tnyml import model
from prediction import Prediction

# TODO get model instance


def test_make_prediction():
    """
    Test for make_prediction
    """

    image_path = (
        Path(__file__).parent.parent
        / "public"
        / "user"
        / "uploads"
        / "Uploads_cat_dog"
        / "image_to_predict.jpg"
    )
    model_name = "cat_dog_model"
    actual_prediction = model.make_prediction(model_name, image_path)
    expected_prediction = Prediction("cat", 0.998)

    assert actual_prediction == expected_prediction
