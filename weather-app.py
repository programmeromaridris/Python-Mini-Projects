import requests

api_key = "227667bae300b4eb8e4fc08afea76bbf"
user_input = input("Enter the city name:")
print("Getting weather details for " + user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found. Please check the city name and try again.")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    print(f"The weather in {user_input} is {weather}. Temperature: {temp}°C")

