import requests

api_key = "091407001ef812a094e745e66dde647b"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
if __name__ == "__main__":
    print(get_data(place="dhaka", forecast_days=3, kind="Temparature"))