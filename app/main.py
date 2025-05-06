import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING,
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("The weather in Paris: ")
        print(f"Temperature: {data["current"]["temp_c"]}°C")
        print(f"Condition: {data["current"]["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
