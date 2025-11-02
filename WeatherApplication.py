import json
import requests
import os

def fetch_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

def save_json(data, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {file_name}")
    except (IOError, TypeError) as e:
        print(f"Failed to write JSON: {e}")

if __name__ == "__main__":
    # Read API key from environment variable for security
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY is not set in environment variables.")
    else:
        lat = 12.904023445195131
        lon = 77.62415139509889
        weather_data = fetch_weather(lat, lon, api_key)
        if weather_data is not None:
            print("Weather Data:", weather_data)
            save_json(weather_data, "weather_data.json")