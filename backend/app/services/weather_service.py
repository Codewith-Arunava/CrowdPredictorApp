import random

class WeatherService:

    @staticmethod
    def get_weather_factor() -> int:
        """
        Simulates weather impact:
        - Rain → less crowd
        - Good weather → more crowd
        """

        weather = random.choice(["sunny", "rainy", "cloudy"])

        if weather == "rainy":
            return -2
        elif weather == "sunny":
            return 2
        else:
            return 0