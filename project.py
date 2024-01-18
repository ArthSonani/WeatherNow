import requests
import sys

api_key = "d444c0033abae566acd04368c72a512f"

def main():
    city = input("Enter Your City: ")
    coordinate = get_coordinates(city, api_key)
    weather = show_weather(coordinate[0], coordinate[1], api_key)

    print(f"\nWeather In Your Bueatiful City '{city.upper()}'")
    print("______________________________________________")
    print(f"Weather Condition is '{weather[0]}' 🌥️")
    print(f"Temperature is '{convert_tmp(weather[1])}°C' 🌡️")
    print(f"Wind speed is '{convert_speed(weather[2])}Km/hr' 🍃\n")


def get_coordinates(city, api_key):
    lat_lon = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}")

    if lat_lon.json() == []:
        sys.exit("No City Found ❎")
    else:
        lat = lat_lon.json()[0]["lat"]
        lon = lat_lon.json()[0]["lon"]
        return lat, lon

def show_weather(lat, lon, api_key):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
    main = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    wind = weather_data.json()['wind']['speed']
    return main, temp, wind

def convert_tmp(tmp):
    return round(tmp-273)

def convert_speed(speed):
    return round(speed*3.6)

if __name__ == "__main__":
    main()