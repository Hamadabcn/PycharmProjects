import json

stringOfJsonData = '{"name": "Hamada", "IsMarried": true, "nice": 0, "feeling": null}'

# read
jsonDataAsPythonValue = json.loads(stringOfJsonData)  # .loads reads from a json file
print(jsonDataAsPythonValue)
print(type(jsonDataAsPythonValue))

# write
pythonValue = {'isHuman': True, 'nice': 0, 'name': 'Hamada', 'feeling': None}
stringOfJsonData = json.dumps(pythonValue)  # .dumps writes on a json file
print(stringOfJsonData)

# temperature in london today from weathermap using API
# https://api.openweathermap.org/data/2.5/weather?q=london&appid=bae2310f57414ae6008fb3738047ecdd