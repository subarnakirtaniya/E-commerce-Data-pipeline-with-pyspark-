# E-commerce-Data-pipeline-with-pyspark-
Build a pipeline that extracts sales data → transforms it → loads into a warehouse → creates analytics dashboard.
                 +----------------------+
                 |   Sales CSV Dataset  |
                 |   (50,000 records)   |
                 +----------+-----------+
                            |
                            |
                            v
                +-----------------------+
                |     PySpark ETL       |
                | Extract + Transform   |
                | Data Cleaning         |
                +----------+------------+
                           |
                           |
                           v
                +-----------------------+
                |     PostgreSQL        |
                |   Data Warehouse      |
                |  (Fact + Aggregates)  |
                +----------+------------+
                           |
                           |
                           v
                +-----------------------+
                |   Apache Airflow      |
                |  Schedule ETL DAG     |
                |  Daily Batch Run      |
                +----------+------------+
                           |
                           |
                           v
                +-----------------------+
                |      Power BI         |
                |  Sales Dashboard      |
                |  Business Insights    |
                +-----------------------+
                

# End-to-End Data Engineering Pipeline

This project demonstrates a complete Data Engineering pipeline using PySpark, PostgreSQL, and Airflow.

## Architecture

CSV Data → PySpark ETL → PostgreSQL → Airflow → Power BI

## Tech Stack

Python
PySpark
PostgreSQL
Apache Airflow
Power BI

## Features

ETL pipeline
Data cleaning and transformation
Workflow orchestration
Data warehouse storage
Analytics dashboard

## Project Structure

data → raw datasets
etl → extraction and transformation scripts
airflow_dag → scheduled pipeline
sql → database tables
dashboard → Power BI dashboard

## Dashboard Insights

Daily revenue trend
Top selling products
Customer purchase behaviour

## How to Run

Install requirements

pip install -r requirements.txt

Run pipeline

python etl/extract.py
python etl/transform.py
python etl/load.py


Key Data Engineering Concepts Demonstrated

ETL Pipeline
Batch Data Processing
Data Transformation
Workflow Orchestration
Data Warehousing
Data Analytics
