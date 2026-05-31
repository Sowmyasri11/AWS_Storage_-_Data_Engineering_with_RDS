import boto3

BUCKET_NAME = "aws-data-lake-sowmya"

LOCAL_FILE = "../data/raw/Sample - Superstore.csv"

S3_KEY = "raw/Sample - Superstore.csv"

s3 = boto3.client("s3")

s3.upload_file(
        LOCAL_FILE,
        BUCKET_NAME,
        S3_KEY
)
print("File uploaded succesfully")