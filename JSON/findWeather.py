import requests, json

# section 3 api_key
api_key = "bae2310f57414ae6008fb3738047ecdd"


# section 1 joining the key with the page (url)
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# section 2 which city?
city_name = input("Please enter your city: ")

# complete url address
complete_url = base_url + "q=" + city_name + "&units=metric" + "&appid=" + api_key

# response object
response = requests.get(complete_url)

# print(response.text)

x = json.loads(response.text)

if x["cod"] != '404':
    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print("Temperature in metric unit = " + str(current_temperature) + "\natmospheric pressure in metric = "
          + str(current_pressure) + "\nhumidity (in %) = " + str(current_humidity) +
          "\nweather description = " + str(weather_description))

else:
    print(" City not found")
