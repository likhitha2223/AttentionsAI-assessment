class UserInteractionAgent:
    async def collect_preferences(self, city: str, date: str, start_time: str, end_time: str, budget: float, interests: str):
        preferences = {
            "city": city,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "budget": budget,
            "interests": interests
        }
        return preferences
