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
    Uploads a test text file to Google Cloud Storage bucket.
    Creates a new file containing some sample text.
    """

    # Create a blob (binary large object) in bucket.
    blob = bucket.blob(file)

    # write blob into GCS bucket.
    blob.upload_from_filename(file)

# if __name__ == "__main__":
    # JSON_Location = r"atd2024-4c3b61c5ad99.json"
    # Bucket_Name = "test-storage-abc"

    # client = create_client_from_json(JSON_Location)
    # # bucket = new_bucket(client, bucket_name)
    # bucket = client.bucket(Bucket_Name)
    # upload_file(bucket)
    