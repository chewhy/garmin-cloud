from google.cloud import storage


#TODO: add some comments

def create_client_from_json(file_location):
    """
    Use a JSON file that contains a service key for the service account
    and returns a Client object.
    """
    client = storage.Client.from_service_account_json(file_location)
    return client

def new_bucket(client, bucket_name):
    """
    Creates bucket object. This function should only be called once.
    """
    # creates a client for interacting with GCP Storage API,
    # using the ServiceAccount key file
    bucket = client.create_bucket(bucket_name, location='asia-southeast1')
    return bucket


def upload_file(bucket, file):
    """
    Uploads a file to the provided bucket.
    """

    # Create a blob (binary large object) in bucket.
    blob = bucket.blob(file)

    # write blob into GCS bucket.
    blob.upload_from_filename(file)
