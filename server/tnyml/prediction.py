class Prediction:
    """A class to represent a prediction.

    Attributes:
        prediction (str): the predicted class.
        confidence (float): the confidence of the prediction.

    """

    def __init__(self, prediction: str, confidence: float):
        """Constructs all necessary attributes for the Prediction object.

        Args:
            prediction (str): the predicted class.
            confidence (float): the confidence of the prediction.

        """
        self.prediction: str = prediction
        self.confidence: float = confidence

    def __eq__(self, other) -> bool:
        """Compares two Prediction objects.

        Args:
            other (Prediction): The other Prediction object.

        Returns:
            bool: Returns True if the two Prediction objects have the same
            prediction label and confidence (i.e. are equal), False otherwise.
        """
        return (
            self.prediction == other.prediction
            and self.confidence == other.confidence
        )

    def to_json(self) -> dict:
        """Converts the Prediction object to a dictionary.

        Returns:
            dict: A dictionary representation of the Prediction object.
        """
        return {"prediction": self.prediction, "confidence": self.confidence}
