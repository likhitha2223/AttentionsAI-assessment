from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.interaction_agent import UserInteractionAgent
from agents.itinerary_agent import ItineraryGenerationAgent
from agents.optimization_agent import OptimizationAgent
from agents.weather_agent import WeatherAgent
from agents.news_agent import NewsAgent
from agents.memory_agent import MemoryAgent

# Initialize FastAPI app
app = FastAPI()

# Initialize agents
user_interaction_agent = UserInteractionAgent()
itinerary_generation_agent = ItineraryGenerationAgent()
optimization_agent = OptimizationAgent()
weather_agent = WeatherAgent()
news_agent = NewsAgent()
memory_agent = MemoryAgent()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Travel Itinerary API! Visit /docs for the full API documentation."}

# Pydantic model for user input
class Preferences(BaseModel):
    city: str
    date: str
    start_time: str
    end_time: str
    budget: float
    interests: str

class ItineraryRequest(BaseModel):
    city: str
    interests: str
    budget: float

class OptimizeRequest(BaseModel):
    start_point: str
    end_point: str
    budget: float

class WeatherRequest(BaseModel):
    city: str
    date: str

class NewsRequest(BaseModel):
    city: str

@app.post("/collect_preferences/")
async def collect_preferences(preferences: Preferences):
    """
    Collect and store user preferences using the UserInteractionAgent.
    """
    # Collect user preferences
    collected_preferences = await user_interaction_agent.collect_preferences(
        city=preferences.city,
        date=preferences.date,
        start_time=preferences.start_time,
        end_time=preferences.end_time,
        budget=preferences.budget,
        interests=preferences.interests
    )
    
    # Save preferences to the memory agent
    memory_agent.save_preferences(user_id="user1", preferences=collected_preferences)

    return {"message": "Preferences collected successfully", "preferences": collected_preferences}

@app.post("/generate_itinerary/")
async def generate_itinerary(request: ItineraryRequest):
    """
    Generate an itinerary using the ItineraryGenerationAgent based on user preferences.
    """
    # Generate itinerary using agent
    itinerary = await itinerary_generation_agent.generate_itinerary(
        city=request.city, 
        interests=request.interests, 
        budget=request.budget
    )
    
    return {"itinerary": itinerary}

@app.post("/optimize_itinerary/")
async def optimize_itinerary(request: OptimizeRequest):
    """
    Optimize the itinerary using the OptimizationAgent based on budget and travel paths.
    """
    optimized_path = await optimization_agent.optimize_travel_path(
        start_point=request.start_point,
        end_point=request.end_point,
        budget=request.budget
    )
    
    return {"optimized_path": optimized_path}

@app.post("/get_weather/")
async def get_weather(request: WeatherRequest):
    """
    Fetch weather information using the WeatherAgent for a specific city and date.
    """
    weather = await weather_agent.get_weather(
        city=request.city, 
        date=request.date
    )
    
    return {"weather": weather}

@app.post("/get_news/")
async def get_news(request: NewsRequest):
    """
    Fetch news related to the specified city using the NewsAgent.
    """
    news = await news_agent.get_news(city=request.city)
    
    return {"news": news}

