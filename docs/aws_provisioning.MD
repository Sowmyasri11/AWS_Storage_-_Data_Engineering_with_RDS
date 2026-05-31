# Part 2: AWS Provisioning

## Objective

The objective of this phase was to provision the AWS resources required for the project. This included creating an S3 bucket for storing raw data, provisioning a PostgreSQL database using Amazon RDS, configuring security groups, and validating database connectivity through an EC2 instance.

---

## Creating an S3 Bucket

An Amazon S3 bucket was created to act as the raw data lake for the project.

Steps performed:

- Opened the AWS S3 Console.
- Created a new bucket.
- Selected the same AWS region used for other resources.
- Kept public access blocked.
- Successfully created the bucket.

The bucket will be used to store raw CSV files before processing.

---

## Creating an Amazon RDS PostgreSQL Instance

A PostgreSQL database was provisioned using Amazon RDS.

Configuration used:

- Engine: PostgreSQL
- Instance class: db.t3.micro
- Storage: 20 GB
- Public access: Enabled

Steps performed:

- Opened the Amazon RDS Console.
- Selected "Create Database".
- Chose PostgreSQL as the database engine.
- Configured database credentials.
- Created the database instance.

After a few minutes, the database status changed to "Available".

---

## Configuring Security Groups

To allow database connectivity, inbound rules were configured for the RDS security group.

Rule added:

- Type: PostgreSQL
- Port: 5432

This allows PostgreSQL clients to connect to the database instance.

---

## Launching an EC2 Instance

An EC2 instance was launched to validate connectivity with the RDS database.

Steps performed:

- Created an Amazon Linux EC2 instance.
- Connected using EC2 Instance Connect.
- Verified successful access to the instance terminal.

---

## Installing PostgreSQL Client

After connecting to the EC2 instance, PostgreSQL client tools were installed.

Command used:

```bash
sudo dnf install postgresql15 -y
```

Verification:

```bash
psql --version
```

Output:

```text
psql (PostgreSQL) 15.16
```

---

## Connecting to Amazon RDS

Using the RDS endpoint, a connection was established from the EC2 instance.

Command used:

```bash
psql -h <RDS-ENDPOINT> -U postgres -d postgres
```

Connection output:

```text
psql (15.16, server 18.3)

SSL connection established

postgres=>
```

This confirmed that the EC2 instance could successfully communicate with the PostgreSQL database hosted on Amazon RDS.

---

## Database Validation

After establishing the connection, basic SQL commands were executed to verify database functionality.

Commands executed:

```sql
SELECT version();
```

```sql
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

```sql
INSERT INTO customers VALUES (1, 'Sowmya');
```

```sql
SELECT * FROM customers;
```

The commands executed successfully, confirming that read and write operations were working correctly.

---

## Outcome

In this phase, the required AWS infrastructure was successfully provisioned.

Resources created:

- Amazon S3 bucket for raw data storage
- Amazon RDS PostgreSQL database
- Amazon EC2 instance for connectivity testing

Connectivity between EC2 and RDS was validated successfully, and database operations were performed without issues.

The environment is now ready for data ingestion and storage using Python and Boto3.
