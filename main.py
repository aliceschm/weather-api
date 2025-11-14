from dotenv import load_dotenv
import os
from requests import post, get
import pprint

load_dotenv()
api_key = os.getenv("API_KEY")

def get_forecast(location):

    #api endpoint
    url = 'http://api.weatherapi.com/v1/forecast.json'

    params = {
        "key": api_key,
        "q": location,
        "days": 0,
        "lang": "en"
    }

    #get request
    response = get(url, params=params)

    #convert response to json only if status code is 200
    if response.status_code == 200:
        json_response = response.json()
        #pprint.pprint(json_response) #pprint lib for better visualization of response
        localtime = json_response["location"]["localtime"]
        temp = json_response["current"]["temp_c"]
        condition =json_response["current"]["condition"]["text"]
        max_temp = json_response["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        min_temp = json_response["forecast"]["forecastday"][0]["day"]["mintemp_c"]
        chance_of_rain = json_response["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
        moon_phase = json_response["forecast"]["forecastday"][0]["astro"]["moon_phase"]
        hours = json_response["forecast"]["forecastday"][0]["hour"]
        temps_by_hour = {h["time"]: h["temp_c"] for h in hours}
        
        #print forecast items
        print("\n=== WEATHER FORECAST ===")
        print(f"Local time: {localtime}")
        print(f"Condition: {condition}")
        print(f"Temperature now: {temp}°C")
        print(f"Max today: {max_temp}°C")
        print(f"Min today: {min_temp}°C")
        print(f"Chance of rain: {chance_of_rain}%")
        print(f"Moon phase: {moon_phase}")

        print("\n--- Temperature by hour ---")
        for time, t in temps_by_hour.items():
            hour = time.split(" ")[1]   #get only hour -remove date
            print(f"{hour}: {t}°C")

    else:
        print(f"Ocorreu um erro. Status code {response.status_code}")
        

get_forecast("Rio de Janeiro")
