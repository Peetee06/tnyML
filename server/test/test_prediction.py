import prediction


def test___eq__():
    prediction1 = prediction.Prediction("cat", 0.998)
    prediction2 = prediction.Prediction("cat", 0.998)
    assert prediction1 == prediction2


def test____eq___should_be_unequal_prediction():
    prediction1 = prediction.Prediction("cat", 0.998)
    prediction2 = prediction.Prediction("dog", 0.998)
    assert prediction1 != prediction2


def test____eq___should_be_unequal_confidence():
    prediction1 = prediction.Prediction("cat", 0.998)
    prediction2 = prediction.Prediction("cat", 0.991)
    assert prediction1 != prediction2


def test_to_json_should_be_equal():
    prediction1 = prediction.Prediction("cat", 0.998)
    assert prediction1.to_json() == {"prediction": "cat", "confidence": 0.998}


def test_to_json_should_be_unequal_prediction():
    prediction1 = prediction.Prediction("dog", 0.998)
    assert prediction1.to_json() != {"prediction": "cat", "confidence": 0.998}


def test_to_json_should_be_unequal_confidence():
    prediction1 = prediction.Prediction("cat", 0.991)
    assert prediction1.to_json() != {"prediction": "cat", "confidence": 0.998}
