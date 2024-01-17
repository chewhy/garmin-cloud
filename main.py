<<<<<<< HEAD
from flask import escape

import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "name" in request_json:
        name = request_json["name"]
    elif request_args and "name" in request_args:
        name = request_args["name"]
    else:
        name = "World"
    return f"Hello {escape(name)}!"
=======
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
>>>>>>> 18dce1d (main.py retrieves data from Garmin)
