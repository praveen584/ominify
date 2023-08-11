import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,  # Corrected the API key variable
        "units": "metric"  # You can change this to "imperial" if you prefer Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        return data
    else:
        print("Error:", data['message'])
        return None

def main():
    api_key = "ca394e8a960bf09af5cc0b1970083cf4"  # Replace with your actual API key
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    
    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")

if __name__ == "__main__":
    main()
