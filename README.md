Build Challenge – Assignments 1 & 2

This repository contains two independent assignments demonstrating core competencies in concurrent programming, functional data processing, and analytical computation using Python. Both assignments include complete implementations and automated test suites using pytest.

Assignment 1: Producer–Consumer Pattern
Overview

This assignment implements a classic Producer–Consumer concurrency model using Python threads, condition variables, and a custom blocking buffer. The primary objectives are:

Thread synchronization

Concurrent producer and consumer execution

Blocking queue behavior

Wait/notify coordination

Multi-producer and multi-consumer handling

The design follows standard concurrency principles and ensures safe communication between threads without deadlocks or race conditions.

Implementation Summary

The solution provides the following components:

BlockingBuffer

A custom FIFO buffer implemented using threading.Condition.
Key characteristics:

Threads block when the buffer is full or empty

Mutual exclusion around shared state

Controlled wake-up via notify_all

Maintains strict FIFO ordering

Producer

Reads items from a source list

Inserts items into the buffer

Does not send sentinel values (clean separation of concerns)

Supports any number of concurrent producers

Consumer

Continuously reads from the buffer

Terminates only when it receives a sentinel (None)

Supports multiple concurrent consumers

Sentinel Dispatch

A dedicated helper function ensures that termination signals equal the number of consumers, preventing early shutdown or indefinite blocking.

Test Coverage

The test suite validates the following behaviors:

Basic producer–consumer data flow

Blocking semantics when the buffer is full or empty

Multiple producers writing concurrently

Multiple consumers retrieving concurrently

Handling of empty inputs

Proper shutdown using sentinels

Preservation of FIFO ordering

How to Run

From the project root:
pytest assignment1 -vv


Assignment 2: Functional Programming and Sales Data Analysis
Overview

This assignment demonstrates functional programming concepts, stream-style operations, and data aggregation techniques through analysis of a structured sales dataset. The solution uses a synthetic dataset of 1,000 records that reflects realistic attributes found in retail and financial domains.

Primary objectives:

Functional transformation pipelines

Stream-like data operations

Grouping and aggregation

Lambda-based derived fields

Analytical computation over a large dataset

Dataset Description

The dataset was generated to simulate realistic e-commerce transactions and includes the following fields:

order_id: Unique transaction identifier

customer_id: Customer reference

product, category: Item classification

price, cost: Pricing and margin inputs

quantity: Units sold

discount: Percentage discount applied

region: Geographic segmentation

payment_method: Transaction channel

date: Transaction date (2023–2024 range)

These fields support a wide range of analytical operations including revenue analysis, profitability assessment, customer segmentation, time-based trends, and category-level insights.

Functional Programming Techniques

The implementation uses Pandas to emulate functional programming and stream operations:

Chained transformations using .assign()

Lambda expressions for computed fields (revenue, profit, etc.)

Vectorized operations without manual loops

Declarative grouping and aggregation pipelines

Stream-like flows resembling Java Streams (group → aggregate → sort → collect)

Analytical Operations Implemented

The analysis component provides the following capabilities:

Total revenue computation

Revenue grouped by category

Revenue grouped by region

Top-N products by revenue

Monthly revenue, profit, quantity, and discount summary

Percentage contribution by category

Customer lifetime revenue

Payment-method distribution

Average profit by category

These functions operate efficiently over the 1,000-row dataset.

Test Coverage

Automated tests validate:

Structural correctness of outputs

Positive revenue and profit metrics

Grouping accuracy for category and region

Ordering of top-N results

Monthly summary field integrity

Category contribution percentages summing to approximately 100%

Customer-level aggregation

Payment-method distribution across all records

Category-level profit aggregations

All tests pass successfully on the generated dataset.

How to Run

To execute the analysis tests:
pytest assignment2 -vv

Repository Structure : 
assignment1/
    producer_consumer.py
    test_producer_consumer.py

assignment2/
    sales_data_large.csv
    sales_analysis.py
    test_sales_analysis.py
    generate_csv.py

Conclusion

This repository demonstrates competencies across two important domains:

Concurrent system design using shared buffers, condition variables, and coordinated thread execution.

Functional programming and analytical data processing using pandas with stream-like transformation pipelines, complex aggregations, and reproducible computation.

Both solutions are fully tested and follow production-quality design standards suitable for modern engineering workflows.