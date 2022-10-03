import pytest

from tnyml.ludwig_handler import LudwigHandler
from pathlib import Path


@pytest.fixture
def init_model():
    return LudwigHandler("cat_dog_model")


def test_get_models_should_return_models():
    models = LudwigHandler.get_models()
    assert models == ["cat_dog_model", "car_truck_model"]


def test_predict(init_model):
    image_path = (
        Path(__file__).parent.parent
        / "public"
        / "user"
        / "uploads"
        / "Uploads_cat_dog"
        / "image_to_predict.jpg"
    )
    prediction = init_model.predict(image_path)
    assert prediction.prediction == "cat"
    assert prediction.confidence == 0.998


# TODO: write tests to handle missing image, wrong model, etc.

# TODO move this test to flask testing
# def test_rest_service_predict():
#    prediction = predict("cat_dog_model")
#
#    expected_prediction = { "prediction" : "cat",
#                            "confidence" : 0.53
#    }
#
#    assert(prediction != expected_prediction)
