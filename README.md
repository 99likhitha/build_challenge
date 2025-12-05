# Build Challenge – Assignments 1 and 2

This repository contains two independent assignments demonstrating competencies in concurrent programming, functional programming, stream-style data operations, and analytical computation using Python. Both assignments include complete implementations and automated test suites using `pytest`.

---

## Assignment 1: Producer–Consumer Pattern

### Overview
This assignment implements a classic producer–consumer concurrency model using Python threads, a custom blocking buffer, and condition variables. The goal is to demonstrate synchronized communication between producer and consumer threads.

---

### Objectives
- Thread synchronization  
- Concurrent producer and consumer execution  
- Blocking queue behavior  
- Wait/notify coordination  
- Multi-producer and multi-consumer handling  

---

### Implementation Details

#### BlockingBuffer
A custom FIFO blocking buffer built using `threading.Condition`.

Features:
- Producers block when the buffer is full  
- Consumers block when the buffer is empty  
- Condition variable ensures correct wait/notify behavior  
- Mutual exclusion for all operations  
- Strict FIFO ordering  

#### Producer
- Reads items from a source container  
- Inserts items into the buffer  
- Supports any number of concurrent producers  

#### Consumer
- Continuously consumes from the buffer  
- Stops only when a sentinel value (`None`) is received  
- Supports multiple concurrent consumers  

---

#### File Structure
assignment1/
    producer_consumer.py
    test_producer_consumer.py


### Test Coverage
The test suite verifies:
- Basic producer–consumer flow  
- Blocking behavior (full and empty buffer)  
- Correct FIFO ordering  
- Multiple producers generating concurrently  
- Multiple consumers consuming concurrently  
- Sentinel-based controlled shutdown  
- Handling of empty input sources  

---

### Running Tests
```bash
pytest assignment1 -vv
```



# Assignment 2 – Sales Data Analysis Using Functional Programming

This assignment demonstrates functional programming principles, stream-style transformations, data aggregation, and analytical computation using a realistic dataset of 1,000 retail sales records. The implementation leverages pandas to emulate Java Streams–style data processing using declarative and vectorized operations.

---

## 1. Overview

The goal of this assignment is to process a structured CSV dataset using:

- Functional pipelines  
- Lambda expressions  
- Grouping and aggregation  
- Stream-style operations  
- Declarative transformations  

The analysis simulates real-world use cases such as revenue reporting, customer behavior modeling, profitability tracking, and category-level analytics.

---

## 2. Dataset Description

A synthetic dataset with **1,000 retail transactions** was generated using `generate_csv.py`. Each record includes:

- `order_id`  
- `customer_id`  
- `product`  
- `category`  
- `price`  
- `cost`  
- `quantity`  
- `discount`  
- `region`  
- `payment_method`  
- `date` (range: 2023–2024)  

These fields support a wide range of analytical operations including profit analysis, contribution modeling, customer segmentation, and time-series trend evaluations.

### Dataset Files
- `sales_data_large.csv` – main dataset (1,000 rows)  
- `generate_csv.py` – reproducible generator script  

---

## 3. Functional Programming Techniques Used

This assignment heavily relies on functional programming patterns within pandas.

### 3.1 Lambda Expressions
Used inside transformation pipelines:
- `revenue = price * quantity * (1 - discount)`  
- `cost_total = cost * quantity`  
- `profit = revenue - cost_total`  
- Extraction of time-based fields (month, year, weekday)

### 3.2 Chained Transformations
Example pipeline:
```python
self.df.assign(
    revenue=lambda x: x.price * x.quantity * (1 - x.discount),
    cost_total=lambda x: x.cost * x.quantity,
    profit=lambda x: x.revenue - x.cost_total,
    month=lambda x: x.date.dt.to_period("M").astype(str)
)
```

### 3.3 Stream-Style Operations

Functional patterns mirroring Java Streams:

- `groupby → agg → sort_values`
- `value_counts(normalize=True)`
- Transformation → filtering → aggregation → collection

---

### 3.4 Vectorized Operations

All heavy computation is vectorized:

- No loops  
- No manual iteration  
- No mutable intermediate state  

---

## 4. Analytical Features Implemented

The `SalesAnalysis` class supports comprehensive analytics:

### 4.1 Total Revenue
```python
total_revenue()
```

### 4.2 Revenue by Category
```python
revenue_by_category()
```

### 4.3 Revenue by Region
```python
revenue_by_region()
```
### 4.4 Top-N Products by Revenue
```python
top_n_products(n)
```

### 4.5 Monthly Summary (Revenue, Profit, Units, Discounts)
Aggregates metrics by year-month, including:
 
- Total Revenue
- Total Profit
- Units Sold
- Discounts Applied

### 4.6 Category Contribution (% of Total Revenue)
```python
category_contribution()
```

### 4.7 Customer Lifetime Revenue
```python
customer_lifetime_revenue()
```

### 4.8 Customer Lifetime Revenue

### 4.9 Average Profit by Category
```python
avg_profit_by_category()
```


#### File Structure
assignment2/
    sales_analysis.py
    sales_data_large.csv
    generate_csv.py
    test_sales_analysis.py
    README.md

### Test Coverage
The test suite (test_sales_analysis.py) validates:
- Revenue and profit calculations
- Category and region aggregation accuracy
- Correct ordering of Top-N products
- Monthly time-series summary fields
- Category contribution percentages
- Customer lifetime revenue mapping
- Payment method distribution
- Profitability grouping 

---

### Running Tests
```bash
pytest assignment2 -vv
```

### Running the Analysis Manually
```bash
python assignment2/sales_analysis.py
```

### Requirements
- Python 3.8+
- pandas
- pytest

### Install required packages manually :
```bash
pip install pandas pytest
```
