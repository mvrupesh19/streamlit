import streamlit as st
import python_weather
import asyncio

# Setup the page title and icon
st.set_page_config(page_title="Weather App", page_icon="🌤️")

async def get_weather(city_name):
    # We use 'METRIC' for Celsius
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        return await client.get(city_name)

# --- UI DESIGN ---
st.title("🌤️ Real-Time Weather App")
st.write("Enter a city name below to get the current weather conditions.")

# Create an input box for the user
city = st.text_input("City Name", placeholder="e.g. New York, London, Tokyo")

if city:
    try:
        # Run the async function to get weather data
        weather = asyncio.run(get_weather(city))
        
        # Display the results in nice columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Temperature", value=f"{weather.temperature}°C")
            st.write(f"**Condition:** {weather.description}")
            
        with col2:
            st.write(f"**Kind:** {weather.kind}")
            # The library often provides basic icons/descriptions
            if "sun" in weather.description.lower():
                st.write("☀️")
            elif "rain" in weather.description.lower():
                st.write("🌧️")
            else:
                st.write("☁️")
                
        # Optional: Show a small divider
        st.divider()
        st.info(f"Showing results for: {city.capitalize()}")

    except Exception as e:
        st.error(f"Could not find weather for '{city}'. Please check the spelling.")