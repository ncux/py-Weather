import requests as Weather

city = input('Enter city name: ')
API_KEY = 'enter API_KEY here'

url = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(API_KEY, city)

response = Weather.get(url).json()

temperature = response['main']['temp']
conditions = response['weather'][0]['description']
windSpeed = response['wind']['speed']

print(response)
print(temperature)
print(conditions)
print(windSpeed)








