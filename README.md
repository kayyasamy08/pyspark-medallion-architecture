# PySpark Medallion Architecture Using Databricks

## Project Overview

This project demonstrates the Medallion Architecture using PySpark in Databricks. Decathlon product data is processed through three layers: Bronze, Silver, and Gold.

The project covers raw data ingestion, data cleaning, and brand-level business summaries using PySpark and Delta tables.

## Architecture

Source Data → Bronze → Silver → Gold

### 1. Bronze Layer — Raw Data Ingestion

* Reads raw product data from `workspace.default.decathlon_21439`.
* Adds an `ingestion_timestamp` column using `current_timestamp()`.
* Writes the data to a Delta table named `bronze_decathlon_spark`.

### 2. Silver Layer — Data Cleaning

* Removes duplicate products based on `objectID`.
* Filters records with missing product names.
* Removes records where `sellingPrice` is missing or less than or equal to zero.
* Writes cleaned data to `silver_decathlon_spark`.

### 3. Gold Layer — Business Summary

Groups products by brand and calculates:

* Total products
* Average selling price
* Minimum selling price
* Maximum selling price

The aggregated data is stored in `gold_decathlon_summary_spark`.

## Technologies Used

* Python
* PySpark
* Databricks
* Delta Lake
* Medallion Architecture

## Project Structure

```text
pyspark-medallion-architecture/
├── README.md
├── 01_bronze_layer.py
├── 02_silver_layer.py
└── 03_gold_layer.py
```

## Key Learnings

* Reading source tables using PySpark
* Adding ingestion timestamps
* Removing duplicate and invalid records
* Performing group-by aggregations
* Writing DataFrames to Delta tables

## Output

The Gold layer provides brand-level product counts and selling-price metrics for product analysis.

## Author

Ayyasamy
