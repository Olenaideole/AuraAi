import requests
import json

API_URL = "https://api.example.com/tokens"
API_KEY = "your_api_key_here"

def fetch_token_data():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        with open("trading_data.json", "w") as f:
            json.dump(data, f, indent=4)
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_token_data()
