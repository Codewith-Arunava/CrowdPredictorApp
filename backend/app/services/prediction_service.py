import random

class PredictionService:

    @staticmethod
    def predict_crowd(station: str, time: str) -> int:
        """
        Dummy ML prediction logic.
        Replace with trained ML model later.
        """

        # Example logic (can be replaced with real model)
        base = random.randint(3, 7)

        # peak hours logic
        if "08" in time or "09" in time or "18" in time:
            base += 2

        return min(base, 10)