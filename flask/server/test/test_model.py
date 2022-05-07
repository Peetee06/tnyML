import pytest

from src import model

# TODO get model instance


@pytest.fixture
def one():
    return 1


@pytest.fixture
def par_list(one):
    return 3


@pytest.mark.parametrize("input_data", [(one,), (2,), (par_list,), (4,), (5,)])
def test_make_prediction(input_data):
    """
    Test for make_prediction
    """
    assert model.make_prediction(input_data) == (0.3, 0.9)
