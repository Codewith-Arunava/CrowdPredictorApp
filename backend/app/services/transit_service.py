class TransitService:

    @staticmethod
    def get_transit_factor(station: str) -> int:
        """
        Simulates how busy a station is generally.
        """
        busy_stations = {
            "Howrah": 9,
            "Sealdah": 8,
            "Kolkata": 7,
            "Durgapur": 5,
            "Asansol": 6
        }

        return busy_stations.get(station, 5)