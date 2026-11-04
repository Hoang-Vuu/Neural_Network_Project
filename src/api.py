"""Open-Meteo daily forecast helper for future trip planning."""
from datetime import datetime, timezone
import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_forecast(latitude, longitude, days=7):
    """Return compact daily forecasts for a location."""

    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        raise ValueError("Invalid latitude or longitude")

    if not 1 <= days <= 7:
        raise ValueError("days must be from 1 to 7")

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "precipitation_probability_max,wind_speed_10m_max",
        "forecast_days": days,
        "timezone": "auto",
        "wind_speed_unit": "kmh"
    }

    response = requests.get(
        FORECAST_URL,
        params=params,
        timeout=20
    )
    response.raise_for_status()

    data = response.json()
    daily = data["daily"]

    observations = []

    for index, date_string in enumerate(daily["time"]):
        observations.append({
            "date": date_string,
            "rain_probability_max_pct":
                daily["precipitation_probability_max"][index],
            "wind_speed_max_kmh":
                daily["wind_speed_10m_max"][index]
        })

    return {
        "timezone": data.get("timezone"),
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "Open-Meteo Forecast API",
        "days": observations
    }


if __name__ == "__main__":
    sample = get_forecast(52.515, 13.351, days=3)
    print(sample)
