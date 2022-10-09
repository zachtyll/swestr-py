from urllib import response
from urllib.error import HTTPError
from matplotlib.rcsetup import validate_sketch
import requests
import json

# Intervals that are accepted by
# the SWESTR server.
acceptedIntervals = [
    "1W",
    "1M",
    "2M",
    "3M",
    "6M"
]


def latest_rate():
    """
    Get the latest published interest rate for the SEK.
    Returns
    """
    try:
        response = requests.get("https://api.riksbank.se/swestr/v1/latest/SWESTR")
        content = json.loads(response.content)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Unexpected error occured: {err}")
    else:
        return content["rate"]


def compounded_average(interval):
    """Get the latest published average entry for the given id.
    """

    # Error on faulty inserted intervals.
    if interval not in acceptedIntervals:
        raise ValueError("Interval is not supported by the server.")

    compoundedAverageId = f"SWESTRAVG{interval}"

    url = f"https://api.riksbank.se/swestr/v1/avg/latest/{compoundedAverageId}"
    try:
        response = requests.get(url)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
    else:
        return response.content