from cgi import test
import pytest

from tnyml import model

# TODO get model instance


def test_make_prediction():
    """
    Test for make_prediction
    """

    image_url = "https://tnyml.app/resources/server/public/user/uploads/Uploads_cat_dog/image_to_predict.jpg"
    model_name = "cat_dog_model"
    prediction = model.make_prediction(model_name, image_url)
    assert prediction.prediction == "cat"
    assert prediction.confidence == 0.998
