"""Main file to retrieve Garmin data and write it to Google Cloud Storage (GCS)"""
import datetime
import json
import os
import csv
# from dotenv import load_dotenv
from flatten_json import flatten
from garminconnect import Garmin
from test_write_gcs import (create_client_from_json,
                            upload_file)


#TODO use file-like object io.StringIO to upload to GCS without creating a file locally

username = os.environ["ID"]
password = os.environ["PASS"]

def init_api():
    """Initialize API for Garmin Connect."""
    _api = Garmin(username, password)
    _api.login()

    return _api


if __name__ == "__main__":

    SERVICE_KEY_PATH = r'atd2024-4c3b61c5ad99.json'
    BUCKET_NAME = "test-storage-abc"
    DATA_FILE_PATH = r'data.json'
    CSV_FILE_PATH = r'csv_data.csv'

    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2023, 12, 30)

    # retrieve data from Garmin Connect
    api = init_api()
    activities = api.get_activities_by_date(
                    start_date.isoformat(), end_date.isoformat())

    # dump Garmin data into a JSON file
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(activities, file, indent=4)

    # # read a list of nested JSON activities
    # with open(r'data.json', "r", encoding="utf-8") as json_file:
    #     activities = json.load(json_file)

    # iterate list and flatten JSONs

    flattened_activities = []
    for activity in activities:
        flattened_activity = flatten(activity)
        flattened_activities.append(flattened_activity)

    # dump flattened JSON into file
    # with open("flattened_data.json", "w", encoding='utf-8') as flat_json:
    #     json.dump(flattened_activities, flat_json, indent=4)

    # Extract column headers from the flattened activities list
    headers = list(set(key for activity in flattened_activities for key in activity.keys()))

    with open(CSV_FILE_PATH, "w", encoding="utf-8", newline='') as csv_output:
        writer = csv.DictWriter(csv_output, fieldnames=headers)

        # Write the headers to the CSV file
        writer.writeheader()

        # Write data to CSV file
        writer.writerows(flattened_activities)

    gcs_client = create_client_from_json(SERVICE_KEY_PATH)
    gcs_bucket = gcs_client.bucket(BUCKET_NAME)
    upload_file(gcs_bucket, DATA_FILE_PATH)
    upload_file(gcs_bucket, CSV_FILE_PATH)
