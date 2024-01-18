from dotenv import load_dotenv
import os
from garminconnect import Garmin
import datetime
import json

username = os.environ["ID"]
password = os.environ["PASS"]

def init_api():
    api = Garmin(username, password)
    api.login()

    return api

api = init_api()

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2023, 12, 30)

activities = api.get_activities_by_date(
                start_date.isoformat(), end_date.isoformat())

with open("data.json", "w") as file:
    json.dump(activities, file, indent=4)
