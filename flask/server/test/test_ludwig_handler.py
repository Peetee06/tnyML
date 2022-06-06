from cgi import test
import pytest

from tnyml.ludwig_handler import LudwigHandler
import numpy as np
from pathlib import Path


@pytest.fixture
def init_model():
    return LudwigHandler("cat_dog_model")


def test_predict(init_model):
    image_path = Path(__file__).parent.parent / "public" / "user" / "uploads" / "Uploads_cat_dog" / "image_to_predict.jpg"
    prediction = init_model.predict(image_path)
    assert prediction.prediction == "cat"
    assert (abs(prediction.confidence - 0.998) <= 0.01)


# TODO move this test to flask testing
# def test_rest_service_predict():
#    prediction = predict("cat_dog_model")
#
#    expected_prediction = { "prediction" : "cat",
#                            "confidence" : 0.53
#    }
#
#    assert(prediction != expected_prediction)
