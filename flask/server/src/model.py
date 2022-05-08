from typing import Any, Tuple


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
