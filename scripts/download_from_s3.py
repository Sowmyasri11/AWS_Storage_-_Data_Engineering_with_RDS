import boto3

BUCKET_NAME = "aws-data-lake-sowmya"

s3 = boto3.client("s3")

s3.download_file(
    BUCKET_NAME,
    "raw/Sample - Superstore.csv",
    "../data/processed/downloaded_superstore.csv"
)

print("File downloaded successfully")