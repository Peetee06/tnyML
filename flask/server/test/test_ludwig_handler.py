from cgi import test
import pytest

from src.tnyml.ludwig_handler import LudwigHandler
import numpy as np

# TODO get model instance

@pytest.fixture
def init_model():
    return LudwigHandler("testmodel")

def test_predict(init_model):
    image = np.zeros((3,3))
    prediction = init_model.predict(image)
    assert (prediction.prediction == "CAT"
            and prediction.confidence == 0.9)
