from dotenv import load_dotenv
import os
from requests import post, get
import json

load_dotenv()
api_key = os.getenv("API_KEY")



def get_forecast(location):

    #api endpoint
    url = 'http://api.weatherapi.com/v1/forecast.json'

    params = {
        "key": api_key,
        "q": location,
        "days": 7
    }

    #get request
    response = get(url, params=params)

    #convert response to json
    json_response = json.loads(response.content)
    print(json_response)

get_forecast("London")