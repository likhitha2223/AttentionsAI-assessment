import ollama

class ItineraryGenerationAgent:
    async def generate_itinerary(self, city: str, interests: str, budget: float):
        prompt = f"Generate a one-day itinerary for {city} based on the user's interest in {interests} with a budget of {budget}."
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
        itinerary = response['text']
        return itinerary
