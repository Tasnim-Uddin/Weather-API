import logging
from urllib.parse import quote, urlencode
from Weather_API.core.utils import scrape

log = logging.getLogger(__name__)


class Weather:
    def __init__(self):
        self.base_url: str = "https://api.open-meteo.com/v1/forecast"
        log.info("Initialised weather")

    valid_options = [
        "temperature_2m",
        "relativehumidity_2m",
        "rain",
        "weathercode",
        "visibility",
    ]

    def get_weather(self, latitude: float, longitude: float, options: str):
        options = self.validate_options(options=options)
        if len(options) == 0:
            return "No options provided"
        data = {"latitude": latitude, "longitude": longitude}
        query = urlencode(data, True)
        query = quote(query, safe="=&")
        url = f"{self.base_url}?{query}&hourly={options}"
        data = scrape(url)
        return data

    def validate_options(self, options: str):
        options = options.split(",")
        options = [option for option in options if option in self.valid_options]
        return ",".join(options)
