import json
import requests

url = "https://api.openweathermap.org/data/3.0/onecall?lat=12.904023445195131&lon=77.62415139509889&appid=4a82a7ce7a2a2fcd0fa0ae278b8fb560"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Response Body:", response.json())

try:
    file_name = "weather_data.json"
    with open(file_name, 'w') as file:
        json.dump(response.json(), file)
except Exception as e:
    print("An error occurred while writing to json file:", e)