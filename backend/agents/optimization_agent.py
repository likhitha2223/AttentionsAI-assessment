from geopy.distance import geodesic

class OptimizationAgent:
    async def optimize_travel_path(self, start_point: str, end_point: str, budget: float):
        start_coords = (12.9716, 77.5946)  # Replace with actual coordinates
        end_coords = (12.9352, 77.6242)  # Replace with actual coordinates
        distance = geodesic(start_coords, end_coords).km
        if budget > 50:
            travel_mode = "taxi"
        else:
            travel_mode = "walking"
        return f"Travel from {start_point} to {end_point} by {travel_mode}, covering {distance} km."
