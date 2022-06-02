from typing import Any, Tuple

# TODO: create model class
# TODO: has attribute modeldata


def make_prediction(input_data: Any) -> Tuple[float, float]:
    # TODO create ludwig handler
    # TODO make prediction on input_data using ludwig
    prediction = 0.3
    confidence = 0.9

    if input_data == 1:
        test = "abc"
    else:
        test2 = "bcd"

    return (prediction, confidence)


def preprocess_data(input_data: Any) -> Any:
    return input_data

def get_models():
    # TODO: search flask/server/models
    # TODO: return list of models
    return "models"
