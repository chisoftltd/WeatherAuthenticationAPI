import requests
import json

paraments = {
    "appid": "caa9d4d1a39c187d3935eb5ff0aeb72f",
    "lat": 55.864239,
    "lon": -4.251806,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=paraments)
response.raise_for_status()
data = response.json()
print(json.dumps(data, indent=4))
print(data['current'])