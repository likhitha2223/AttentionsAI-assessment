import streamlit as st
import requests
from datetime import date

# API endpoint URL
base_url = "http://localhost:8000"

def get_preferences():
    city = st.text_input("Which city are you visiting?")
    date = st.date_input("What day are you planning to visit?")
    start_time = st.time_input("What time would you like to start your day?")
    end_time = st.time_input("What time would you like to finish your day?")
    budget = st.number_input("What is your budget for the day?", min_value=0)
    interests = st.text_input("What are your interests? (e.g., culture, adventure, food)")

    if st.button("Submit Preferences"):
        response = requests.post(f"{base_url}/collect_preferences/", json={
            "city": city,
            "date": date.isoformat(),  # No change here
            "start_time": start_time.strftime("%H:%M:%S"),  # Convert time to string
            "end_time": end_time.strftime("%H:%M:%S"),      # Convert time to string
            "budget": budget,
            "interests": interests
        })
        st.write(response.json())


def show_itinerary():
    city = st.text_input("Enter the city for itinerary:")
    interests = st.text_input("Enter your interests:")
    budget = st.number_input("Enter your budget:", min_value=0)

    if st.button("Generate Itinerary"):
        # Send request to backend to generate the itinerary
        response = requests.post(f"{base_url}/generate_itinerary/", json={
            "city": city,
            "interests": interests,
            "budget": budget
        })
        if response.status_code == 200:
            itinerary = response.json()
            st.write("Here is your itinerary:")
            st.write(itinerary)
        else:
            st.write("Error:", response.text)

def main():
    st.title("One-Day Tour Planning Assistant")
    
    # Get preferences from the user
    get_preferences()

    # Generate itinerary based on preferences
    show_itinerary()

if __name__ == "__main__":
    main()
