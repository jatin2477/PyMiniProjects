import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"

api_key = "450701699b48c52cac3890400b5aa36a"


def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metrics"
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    if data["cod"] == 200:
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"Could not retrieve weather data for {city}.")

city_name = input("Enter city name : ")
get_weather(city_name)