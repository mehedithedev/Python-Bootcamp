import requests
api = "091407001ef812a094e745e66dde647b"
def fetch(location, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api}"

    res = requests.get(url)
    status_code = res.raise_for_status()
    data = res.json()

    list_data = data['list']

    number_of_data = 8 * days

    final_data = list_data[:number_of_data]
    return final_data
    #
    # for forecast in list_data[:number_of_data]:
    #     print(forecast['dt_txt'])
if __name__ == "__main__":
    print(fetch("dhaka", 3))

