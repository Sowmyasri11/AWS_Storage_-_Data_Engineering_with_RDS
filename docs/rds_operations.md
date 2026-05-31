# Part 5: AWS RDS Database Operations

## Objective

The objective of this phase was to design a relational schema, create tables in Amazon RDS PostgreSQL, and perform CRUD (Create, Read, Update, and Delete) operations using SQL.

---

## Database Setup

An Amazon RDS PostgreSQL instance was provisioned and connected through an Amazon EC2 instance.

Connection Status:

```text
psql (15.16, server 18.3)
SSL connection established successfully
```

Database Created:

```sql
CREATE DATABASE superstore_db;
```

Connected to Database:

```sql
\c superstore_db
```

Output:

```text
You are now connected to database "superstore_db" as user "postgres".
```

---

## Table Design

A relational table named `sales` was designed based on the Superstore dataset.

### Table Schema

```sql
CREATE TABLE sales (
    row_id INTEGER PRIMARY KEY,
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
    quantity INTEGER,
    discount NUMERIC(5,2),
    profit NUMERIC(10,2)
);
``"

Output:

```text
CREATE TABLE
```

---

## Table Validation

Command:

```sql
\d sales
```

Output:

```text
Table "public.sales"

row_id         integer                 NOT NULL
order_id       character varying(50)
order_date     date
ship_date      date
customer_id    character varying(50)
customer_name  character varying(100)
segment        character varying(50)
city           character varying(100)
state          character varying(100)
region         character varying(50)
category       character varying(50)
sub_category   character varying(50)
product_name   text
sales          numeric(10,2)
quantity       integer
discount       numeric(5,2)
profit         numeric(10,2)

Primary Key:
sales_pkey (row_id)
```

---

## CRUD Operations

### Create (Insert)

Two sample records were inserted successfully.

Output:

```text
INSERT 0 1
INSERT 0 1
```

### Read (Select)

Query:

```sql
SELECT * FROM sales;
```

Output:

```text
2 rows returned successfully
```

### Filter Records

Query:

```sql
SELECT *
FROM sales
WHERE region='South';
```

Output:

```text
1 row returned successfully
```

### Update

Query:

```sql
UPDATE sales
SET discount = 0.10
WHERE row_id = 1;
```

Output:

```text
UPDATE 1
```

Verification:

```text
discount changed from 0.00 to 0.10
```

### Delete

Query:

```sql
DELETE FROM sales
WHERE row_id = 2;
```

Output:

```text
DELETE 1
```

Verification:

```text
Only 1 record remains in the table.
```

---

## Summary of Operations

| Operation | Status |
|-----------|---------|
| Database Creation | Successful |
| Table Creation | Successful |
| Insert Records | Successful |
| Read Records | Successful |
| Filter Records | Successful |
| Update Records | Successful |
| Delete Records | Successful |
| Validation | Successful |

---

## Outcome

Successfully performed database operations on Amazon RDS PostgreSQL.

Completed activities:

- Created PostgreSQL database
- Designed relational schema
- Created table structure
- Inserted records
- Retrieved records using SQL queries
- Filtered records using conditions
- Updated existing records
- Deleted records based on conditions
- Validated table structure and data

The Amazon RDS database is now configured and ready for data loading, reporting, and analytics workloads.
