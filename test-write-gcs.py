from google.cloud import storage


#TODO: add some comments

def create_client_from_json(file_location):
    client = storage.Client.from_service_account_json(file_location)
    return client

def new_bucket(client, bucket_name):
    # creates a client for interacting with GCP Storage API,
    # using the ServiceAccount key file
    bucket = client.create_bucket(bucket_name, location='asia-southeast1')
    return bucket


def upload_file(bucket):
    file_name = 'my-file.txt'
    file_content = 'this is some example text.'
    blob_name = 'my-file-blob.txt'

    with open(file_name, "w") as file:
        file.write(file_content)

    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)

if __name__ == "__main__":
    json_location = r"atd2024-4c3b61c5ad99.json"
    bucket_name = "test-storage-abc"

    client = create_client_from_json(json_location)
    # bucket = new_bucket(client, bucket_name)
    bucket = client.bucket(bucket_name)
    upload_file(bucket)
