from typing import List

class AnalyticsService:

    @staticmethod
    def calculate_average(crowd_levels: List[int]) -> float:
        if not crowd_levels:
            return 0.0
        return sum(crowd_levels) / len(crowd_levels)

    @staticmethod
    def get_peak_station(data: List[dict]) -> str:
        """
        data format: [{"station": "A", "crowd": 7}, ...]
        """
        if not data:
            return "N/A"

        return max(data, key=lambda x: x["crowd"])["station"]