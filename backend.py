import requests

API_KEY = "7329f98aa244bb955dfa8daaf52197b3"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # Checked from python console
    filtered_data = data["list"]
    number_of_values = 8*forecast_days
    filtered_data = filtered_data[:number_of_values]

    return filtered_data
