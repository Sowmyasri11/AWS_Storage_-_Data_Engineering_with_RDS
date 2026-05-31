ype "help" for help.

superstore_db=> SELECT COUNT(\*) FROM sales;
count

---

     1

(1 row)

superstore_db=> INSERT INTO sales VALUES
(
2,
'CA-2016-152157',
'2016-12-01',
'2016-12-04',
'DV-13045',
'Darrin Van Huff',
'Corporate',
'Los Angeles',
'California',
'West',
'Office Supplies',
'Paper',
'Printer Paper',
120.50,
5,
0.05,
25.75
);

INSERT INTO sales VALUES
(
3,
'CA-2017-152158',
'2017-01-15',
'2017-01-18',
'AB-10001',
'John Smith',
'Consumer',
);.000,ss Mouse', VALUES
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
superstore_db=> SELECT COUNT(\*) FROM sales;
count

---

     5

(1 row)

superstore_db=> SELECT SUM(sales) AS total_sales
FROM sales;
total_sales

---

     1382.46

(1 row)

superstore_db=> SELECT COUNT(\*) FROM sales;
count

---

     5

(1 row)

superstore_db=> SELECT \* FROM sales LIMIT 10;
row_id | order_id | order_date | ship_date | customer_id | customer_name  
| segment | city | state | region | category | sub_category
| product_name | sales | quantity | discount | profit
--------+----------------+------------+------------+-------------+-----------------
+-------------+-------------+------------+---------+-----------------+-------------
-+-----------------------------------+--------+----------+----------+--------
1 | CA-2016-152156 | 2016-11-08 | 2016-11-11 | CG-12520 | Claire Gute  
| Consumer | Henderson | Kentucky | South | Furniture | Bookcases  
 | Bush Somerset Collection Bookcase | 261.96 | 2 | 0.10 | 41.91
2 | CA-2016-152157 | 2016-12-01 | 2016-12-04 | DV-13045 | Darrin Van Huff
| Corporate | Los Angeles | California | West | Office Supplies | Paper  
 | Printer Paper | 120.50 | 5 | 0.05 | 25.75
3 | CA-2017-152158 | 2017-01-15 | 2017-01-18 | AB-10001 | John Smith  
| Consumer | New York | New York | East | Technology | Phones  
 | iPhone Case | 350.00 | 3 | 0.00 | 75.00
4 | CA-2017-152159 | 2017-02-10 | 2017-02-13 | AB-10002 | Mary Jane  
| Home Office | Chicago | Illinois | Central | Furniture | Chairs  
 | Office Chair | 450.00 | 2 | 0.10 | 100.00
5 | CA-2017-152160 | 2017-03-20 | 2017-03-23 | AB-10003 | Robert King  
| Consumer | Dallas | Texas | South | Technology | Accessories
| Wireless Mouse | 200.00 | 4 | 0.05 | 50.00
(5 rows)

superstore_db=> SELECT \* FROM sales;
row_id | order_id | order_date | ship_date | customer_id | customer_name  
| segment | city | state | region | category | sub_category
| product_name | sales | quantity | discount | profit
--------+----------------+------------+------------+-------------+-----------------
+-------------+-------------+------------+---------+-----------------+-------------
-+-----------------------------------+--------+----------+----------+--------
1 | CA-2016-152156 | 2016-11-08 | 2016-11-11 | CG-12520 | Claire Gute  
| Consumer | Henderson | Kentucky | South | Furniture | Bookcases  
 | Bush Somerset Collection Bookcase | 261.96 | 2 | 0.10 | 41.91
2 | CA-2016-152157 | 2016-12-01 | 2016-12-04 | DV-13045 | Darrin Van Huff
| Corporate | Los Angeles | California | West | Office Supplies | Paper  
 | Printer Paper | 120.50 | 5 | 0.05 | 25.75
3 | CA-2017-152158 | 2017-01-15 | 2017-01-18 | AB-10001 | John Smith  
| Consumer | New York | New York | East | Technology | Phones  
 | iPhone Case | 350.00 | 3 | 0.00 | 75.00
4 | CA-2017-152159 | 2017-02-10 | 2017-02-13 | AB-10002 | Mary Jane  
| Home Office | Chicago | Illinois | Central | Furniture | Chairs  
 | Office Chair | 450.00 | 2 | 0.10 | 100.00
5 | CA-2017-152160 | 2017-03-20 | 2017-03-23 | AB-10003 | Robert King  
| Consumer | Dallas | Texas | South | Technology | Accessories
| Wireless Mouse | 200.00 | 4 | 0.05 | 50.00
(5 rows)

superstore_db=> \d sales
Table "public.sales"
Column | Type | Collation | Nullable | Default
---------------+------------------------+-----------+----------+---------
row_id | integer | | not null |
order_id | character varying(50) | | |
order_date | date | | |
ship_date | date | | |
customer_id | character varying(50) | | |
customer_name | character varying(100) | | |
segment | character varying(50) | | |
city | character varying(100) | | |
state | character varying(100) | | |
region | character varying(50) | | |
category | character varying(50) | | |
sub_category | character varying(50) | | |
product_name | text | | |
sales | numeric(10,2) | | |
quantity | integer | | |
discount | numeric(5,2) | | |
profit | numeric(10,2) | | |
Indexes:
"sales_pkey" PRIMARY KEY, btree (row_id)

superstore_db=> SELECT SUM(sales) AS total_sales
FROM sales;
total_sales

---

     1382.46

(1 row)

superstore_db=> SELECT SUM(profit) AS total_profit
FROM sales;
total_profit

---

       292.66

(1 row)

superstore_db=> SELECT AVG(discount) AS avg_discount
FROM sales;
avg_discount

---

0.06000000000000000000
(1 row)

superstore_db=> SELECT SUM(quantity) AS total_items_sold
FROM sales;
total_items_sold

---

               16

(1 row)

superstore_db=> SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region;
region | total_sales
---------+-------------
East | 350.00
South | 461.96
West | 120.50
Central | 450.00
(4 rows)

superstore_db=> SELECT category, SUM(profit) AS total_profit
FROM sales
GROUP BY category;
category | total_profit
-----------------+--------------
Furniture | 141.91
Office Supplies | 25.75
Technology | 125.00
(3 rows)

superstore_db=> SELECT state, SUM(sales)
FROM sales
GROUP BY state
ORDER BY SUM(sales) DESC;
state | sum  
------------+--------
Illinois | 450.00
New York | 350.00
Kentucky | 261.96
Texas | 200.00
California | 120.50
(5 rows)

superstore_db=> SELECT product_name, SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 1;
product_name | total_sales
--------------+-------------
Office Chair | 450.00
(1 row)

superstore_db=> SELECT product_name, SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 1;
product_name | total_profit
--------------+--------------
Office Chair | 100.00
(1 row)

superstore_db=> SELECT region, SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC;
region | total_profit
---------+--------------
Central | 100.00
South | 91.91
East | 75.00
West | 25.75
(4 rows)

superstore_db=>
