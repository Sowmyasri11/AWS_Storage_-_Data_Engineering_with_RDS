# Part 4: Data Processing and Transformation

## Objective

The objective of this phase was to process raw data stored in Amazon S3, perform data cleaning and transformation using Python and Pandas, generate analytical datasets, and store the processed outputs for further use.

---

## Dataset

Dataset Used:

Sample - Superstore.csv

Source Location:

s3://aws-data-lake-sowmya/raw/

The dataset was downloaded and processed using Python on an Amazon EC2 instance.

---

## Reading Data

The dataset was loaded into a Pandas DataFrame using the `read_csv()` function.

Activities performed:

- Loaded CSV dataset into memory
- Verified row and column counts
- Inspected column names and data types

Dataset Statistics:

- Rows: 9,994
- Columns: 21

---

## Data Cleaning

Basic data cleaning operations were performed to improve data quality.

### Handling Missing Values

Missing values were replaced using:

```python
df.fillna("Unknown")
```

### Removing Duplicates

Duplicate records were removed using:

```python
df.drop_duplicates()
```

### Correcting Data Types

The following columns were converted to datetime format:

- Order Date
- Ship Date

This enabled time-based analysis on sales data.

---

## Summary Metrics

The following business metrics were calculated:

- Total Sales: 2,297,200.86
- Total Profit: 286,397.02
- Total Unique Orders: 5,009

These metrics provide a high-level overview of business performance.

---

## Group-wise Aggregations

### Sales by Category

Sales were aggregated by product category using the Pandas `groupby()` function.

Output File:

sales_by_category.csv

### Sales by Region

Sales were aggregated by region to identify geographical performance trends.

Output File:

sales_by_region.csv

---

## Date-Based Analysis

Monthly sales trends were generated using the Order Date column.

Steps performed:

1. Converted Order Date to datetime format.
2. Extracted month and year.
3. Aggregated sales by month.

Output File:

monthly_sales.csv

This dataset can be used for trend analysis and reporting.

---

## Processed Outputs

The following processed datasets were generated:

- cleaned_superstore.csv
- sales_by_category.csv
- sales_by_region.csv
- monthly_sales.csv

These files were stored locally in the output directory.

---

## Uploading Processed Data to S3

Processed datasets were uploaded to:

s3://aws-data-lake-sowmya/processed/

Python Script:

upload_processed_to_s3.py

Boto3 Method Used:

upload_file()

This ensures transformed datasets are available in the processed layer of the data lake.

---

## Outcome

Successfully completed data processing and transformation using Python and Pandas.

Activities completed:

- Read dataset from storage
- Performed data cleaning
- Handled missing values
- Corrected date data types
- Generated summary metrics
- Created category-wise aggregations
- Created region-wise aggregations
- Performed date-based analysis
- Generated processed datasets
- Uploaded transformed data to Amazon S3

The processed datasets are now available for reporting, analytics, and loading into downstream systems such as Amazon RDS.
