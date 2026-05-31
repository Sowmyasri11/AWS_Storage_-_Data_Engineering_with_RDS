import boto3
import pandas as pd
import os

BUCKET_NAME = "aws-data-lake-sowmya"

s3 = boto3.client("s3")

# Download file from S3
s3.download_file(
    BUCKET_NAME,
    "raw/Sample - Superstore.csv",
    "../Sample - Superstore.csv"
)

print("Dataset downloaded")

# Read CSV
df = pd.read_csv("../Sample - Superstore.csv")

print("\nDataset Shape:")
print(df.shape)

# --------------------
# Data Cleaning
# --------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("Data cleaning completed")

# --------------------
# Summary Metrics
# --------------------

print("\nSummary Metrics")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Orders:", df["Order ID"].nunique())

# --------------------
# Category Aggregation
# --------------------

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

# --------------------
# Region Aggregation
# --------------------

sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

# --------------------
# Monthly Analysis
# --------------------

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Month"] = monthly_sales["Month"].astype(str)

# Save outputs
os.makedirs("../output", exist_ok=True)

sales_by_category.to_csv(
    "../output/sales_by_category.csv",
    index=False
)

sales_by_region.to_csv(
    "../output/sales_by_region.csv",
    index=False
)

monthly_sales.to_csv(
    "../output/monthly_sales.csv",
    index=False
)

df.to_csv(
    "../output/cleaned_superstore.csv",
    index=False
)

print("\nProcessed datasets generated successfully")