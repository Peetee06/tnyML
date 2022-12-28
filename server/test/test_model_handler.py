import pytest

from tnyml.model_handler import ModelHandler
from pathlib import Path


@pytest.fixture
def init_model():
    return ModelHandler("cats-vs-dogs")


def test_get_models_should_return_models():
    models = ModelHandler.get_models()
    assert models == ["cats-vs-dogs", "titanic"]


def test_predict(init_model):
    image_path = Path(__file__).parent / "data" / "testfile.jpg"
    prediction = init_model.predict(image_path)
    assert prediction.prediction == "cat"
    assert prediction.confidence == 0.705


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
