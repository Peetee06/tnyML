class Prediction(object):
    def __init__(self, prediction, confidence):
        self.prediction = prediction
        self.confidence = confidence

    def __eq__(self, other):
        return (
            self.prediction == other.prediction
            and self.confidence == other.confidence
        )
