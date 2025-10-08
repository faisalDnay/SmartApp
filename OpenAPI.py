import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
def weerapi():
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 52.0908,
            "longitude": 5.1222,

            "current": ["temperature_2m", "apparent_temperature", "rain"],
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]

        # Process current data. The order of variables needs to be the same as requested.
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()

        print(f"De huidige temratuur in Utrecht is: {current_temperature_2m:.1f} C")

        # Process hourly data. The order of variables needs to be the same as requested.

    except Exception as e:
        print(f"Kon de tempratuur niet ophalen:", e)
if __name__ == '__main__':
    weerapi()