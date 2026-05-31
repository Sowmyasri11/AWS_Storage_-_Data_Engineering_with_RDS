# Part 7: CSV Import & Export with AWS RDS

## 1. Objective

The goal of this part is to demonstrate a complete data workflow using
AWS RDS (PostgreSQL), EC2, and CSV files: - Import CSV data into AWS
RDS - Perform verification using SQL queries - Export query results back
to CSV - Understand bulk import/export methods in AWS

------------------------------------------------------------------------

## 2. Prerequisites

Before starting, ensure: - AWS EC2 instance is running - AWS RDS
PostgreSQL instance is active - Security group allows port 5432 access -
superstore.csv dataset is available on EC2

------------------------------------------------------------------------

## 3. Step 1: Connect to AWS RDS from EC2

Command used:

``` bash
psql -h <rds-endpoint> -U postgres -d superstore_db
```

After successful login:

    superstore_db=>

------------------------------------------------------------------------

## 4. Step 2: Create Table in RDS

``` sql
CREATE TABLE sales (
    row_id INT PRIMARY KEY,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    region VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name TEXT,
    sales NUMERIC(10,2),
    quantity INT,
    discount NUMERIC(5,2),
    profit NUMERIC(10,2)
);
```

------------------------------------------------------------------------

## 5. Step 3: Import CSV into AWS RDS

### Method Used: `\copy `{=tex}(Client-side import)

``` bash
psql -h <rds-endpoint> -U postgres -d superstore_db \
-c "\copy sales FROM 'superstore.csv' CSV HEADER"
```

### Output:

-   Data successfully inserted into sales table
-   Verified using COUNT(\*)

``` sql
SELECT COUNT(*) FROM sales;
```

------------------------------------------------------------------------

## 6. Step 4: Verify Imported Data

``` sql
SELECT * FROM sales LIMIT 5;
```

Expected: - 5 or more records depending on dataset

------------------------------------------------------------------------

## 7. Step 5: Export Data from RDS to CSV

### Method Used: `\copy `{=tex}export query

``` bash
psql -h <rds-endpoint> -U postgres -d superstore_db \
-c "\copy (SELECT * FROM sales) TO 'export_sales.csv' CSV HEADER"
```

### Output:

-   File created on EC2: export_sales.csv

------------------------------------------------------------------------

## 8. Step 6: Validate Export

``` bash
ls -l export_sales.csv
cat export_sales.csv
```

------------------------------------------------------------------------

## 9. Bulk Import/Export Methods

  Method            Description                         Use Case
  ----------------- ----------------------------------- ---------------------
  COPY              Server-side fast loading            Local PostgreSQL
  `\copy`{=tex}     Client-side (AWS RDS recommended)   Cloud databases
  pgAdmin           GUI-based import/export             Beginners
  Python (Pandas)   Automated ETL pipelines             Data engineering
  AWS S3 + Glue     Enterprise data pipelines           Large-scale systems

------------------------------------------------------------------------

## 10. AWS Workflow Summary

CSV File → EC2 → AWS RDS → SQL Processing → CSV Export → GitHub/BI Tools

------------------------------------------------------------------------

## 11. Key Learnings

-   How to import CSV into AWS RDS using `\copy`{=tex}
-   How to export query results into CSV
-   Difference between COPY and `\copy`{=tex}
-   Role of EC2 as a data processing layer
-   Real-world ETL pipeline understanding

------------------------------------------------------------------------

## 12. Conclusion

This task demonstrates a complete cloud-based data pipeline using AWS
services, enabling: - Data ingestion - Data processing - Data
extraction - Cloud database integration
