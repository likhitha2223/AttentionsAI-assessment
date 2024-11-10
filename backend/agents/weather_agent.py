import requests

class WeatherAgent:
    async def get_weather(self, city: str, date: str):
        api_key = "YOUR_API_KEY" 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url).json()
        weather = response.get("weather")[0].get("description")
        return weather
