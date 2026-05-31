# Part 3: Data Ingestion and Storage using Python and Boto3

## Objective

The objective of this phase was to ingest data into Amazon S3 using Python and Boto3, organize the data using a folder structure, and perform file operations such as listing and downloading objects from S3.

---

## S3 Bucket Structure

The existing S3 bucket was used as a simple data lake.

Bucket Name:

aws-data-lake-sowmya

Folder structure created:

raw/
processed/
archive/

Purpose of each folder:

- raw/ : Stores original datasets without modification.
- processed/ : Stores transformed or cleaned datasets.
- archive/ : Reserved for long-term storage of old datasets.

---

## Creating Folder Structure in S3

A Python script named `create_s3_folders.py` was created using Boto3.

The script created the following prefixes in the bucket:

- raw/
- processed/
- archive/

This structure helps organize datasets according to their stage in the data pipeline.

---

## Uploading Dataset to S3

Dataset used:

Sample - Superstore.csv

The dataset was uploaded to:

raw/Sample - Superstore.csv

Python script used:

upload_to_s3.py

Boto3 method used:

upload_file()

The upload completed successfully and the file was stored in the raw zone of the data lake.

---

## Listing Files in S3

A Python script named `list_s3_files.py` was created to retrieve the contents of the bucket.

Boto3 method used:

list_objects_v2()

Output:

archive/
processed/
raw/
raw/Sample - Superstore.csv

This confirmed that the folder structure and uploaded dataset were available in the bucket.

---

## Downloading Files from S3

A Python script named `download_from_s3.py` was created to download objects from Amazon S3.

Source:

raw/Sample - Superstore.csv

Destination:

data/processed/downloaded_superstore.csv

Boto3 method used:

download_file()

The file was downloaded successfully and stored in the local project directory.

---

## Amazon Glacier for Data Archival

Amazon Glacier can be used to archive datasets that are rarely accessed but must be retained for compliance or historical analysis.

A common lifecycle strategy is:

1. Store incoming data in Amazon S3 Standard.
2. Move older data to S3 Glacier Instant Retrieval after a specified period.
3. Move long-term data to S3 Glacier Flexible Retrieval or Deep Archive.

Benefits:

- Lower storage costs.
- Automated archival using lifecycle policies.
- Long-term retention of historical datasets.

Example lifecycle:

- Days 0–90: S3 Standard
- Days 90–180: Glacier Instant Retrieval
- After 180 Days: Glacier Deep Archive

---

## Outcome

Successfully created a simple data lake structure in Amazon S3 and performed data ingestion operations using Python and Boto3.

Activities completed:

- Created S3 folder structure
- Uploaded dataset to S3
- Listed objects in S3
- Downloaded objects from S3
- Reviewed Amazon Glacier archival strategy

The environment is now ready for data processing and loading into downstream systems such as Amazon RDS.
