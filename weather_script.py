import requests
import json

city = str(input('Enter the city: '))

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = weather_data['main']['temp']

if str(temperature)[-1] == '1':
    print(f'Сейчас в городе {city} {int(temperature)} градус')
elif str(temperature)[-1] in '056789':
    print(f'Сейчас в городе {city} {int(temperature)} градусов')
elif str(temperature)[-1] in '234':
    print(f'Сейчас в городе {city} {int(temperature)} градуса')
