import requests

class NewsAgent:
    async def get_news(self, city: str):
        api_key = "YOUR_NEWS_API_KEY"  # Replace with your actual news API key
        url = f"https://newsapi.org/v2/everything?q={city}&apiKey={api_key}"
        response = requests.get(url).json()
        articles = response.get("articles", [])
        news_titles = [article['title'] for article in articles]
        return news_titles
