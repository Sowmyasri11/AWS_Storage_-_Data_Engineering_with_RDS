import boto3

BUCKET_NAME = "aws-data-lake-sowmya"

s3 = boto3.client("s3")

files = [
    "cleaned_superstore.csv",
    "sales_by_category.csv",
    "sales_by_region.csv",
    "monthly_sales.csv"
]

for file in files:
    s3.upload_file(
        f"../output/{file}",
        BUCKET_NAME,
        f"processed/{file}"
    )

    print(f"Uploaded: {file}")

print("All processed files uploaded successfully")