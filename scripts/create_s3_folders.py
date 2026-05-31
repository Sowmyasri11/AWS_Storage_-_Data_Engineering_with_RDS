import boto3
BUCKET_NAME = "aws-data-lake-sowmya"

s3 = boto3.client("s3")

folders =[
        "raw/",
        "processed/",
        "archive/"]
for folder in folders:
        s3.put_object(
                Bucket=BUCKET_NAME,
                Key=folder
        )
        print(f"Created: {folder}")
print("Folder strcture created successfully")