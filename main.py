"""Main file to retrieve Garmin data and write it to Google Cloud Storage (GCS)"""
import datetime
import json
import os
from dotenv import load_dotenv
from garminconnect import Garmin
from test_write_gcs import create_client_from_json

username = os.environ["ID"]
password = os.environ["PASS"]

def init_api():
    _api = Garmin(username, password)
    _api.login()

    return _api


if __name__ == "__main__":

    SERVICE_KEY_PATH = r'atd2024-4c3b61c5ad99.json'
    BUCKET_NAME = "test-storage-abc"

    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2023, 12, 30)

    api = init_api()

    activities = api.get_activities_by_date(
                    start_date.isoformat(), end_date.isoformat())

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(activities, file, indent=4)

    gcs_client = create_client_from_json(SERVICE_KEY_PATH)
    gcs_bucket = gcs_client.bucket(BUCKET_NAME)
