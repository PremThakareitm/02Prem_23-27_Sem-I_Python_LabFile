# 7.1 Write a program to use ‘whether API’ and print temperature of any city, also
# print the sunrise and sunset times for the same humidity of that area.

import requests

api_key = "65a84ed61a806ba4e196b8be0ef37f89"
url = "http://api.openweathermap.org/data/2.5/weather"

city = str(input("Enter city to search: "))

params = {'q': city, 'appid': api_key}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data['main']['temp'] - 273.15 
    humidity = data['main']['humidity']
    sunrise_time = data['sys']['sunrise']
    sunset_time = data['sys']['sunset']

    print(f"Temperature in {city}: {temperature:.2f}°C")
    print(f"Humidity in {city}: {humidity}%")
    print(f"Sunrise in {city}: {sunrise_time}")
    print(f"Sunset in {city}: {sunset_time}")
else:
    print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
