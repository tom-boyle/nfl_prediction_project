import requests
import json
import pandas as pd

def fetch_nfl_data(api_key):
    base_url = "https://api.sportsdata.io/v3/nfl/scores/json/Scores/2022?key=0d40b8d4e9264152ac92346d701a23dc"
    headers = {
        "0d40b8d4e9264152ac92346d701a23dc" : api_key
    }

    response = requests.get(base_url, headers=headers)
    response.raise_for_status() # This will raise an exception for HTTP errors

    return response.json()

def save_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(f"../data/{filename}.csv", index=False)

if __name__ == "__main__":
    API_KEY = "0d40b8d4e9264152ac92346d701a23dc"
    data = fetch_nfl_data(API_KEY)
    save_data_to_csv(data, "nfl_data")