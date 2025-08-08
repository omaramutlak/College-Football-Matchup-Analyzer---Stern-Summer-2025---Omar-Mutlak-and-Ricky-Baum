import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("CFB_API_KEY")


def _get_api_key():
    """Gets the API key, prompting the user if not found."""
    global API_KEY
    if not API_KEY:
        API_KEY = input(
            "API key not found. Please enter your College Football Data API key (Obtain for free at Collegefootballdata.com): "
        )
        save_key = input("Save this key to a new .env file for future use? (y/n): ").lower()
        if save_key == 'y':
            with open(".env", "w") as f:
                f.write(f"CFB_API_KEY={API_KEY}")
            print("API key saved to .env file.")
    return API_KEY


def get_team_stats(team, year):
    api_key = _get_api_key()
    if not api_key:
        raise Exception("API key not provided. Cannot fetch data.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json",
    }
    url = f"https://api.collegefootballdata.com/stats/season?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch stats for {team}: {response.status_code} — {response.text}"
        )

    return response.json()


def get_team_roster(team, year):
    """Fetches the roster for a given team and year."""
    api_key = _get_api_key()
    if not api_key:
        raise Exception("API key not provided. Cannot fetch data.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json",
    }
    url = f"https://api.collegefootballdata.com/roster?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch roster for {team}: {response.status_code} — {response.text}"
        )

    return response.json()







