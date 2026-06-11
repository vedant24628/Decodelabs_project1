Data Analytics Project 1: Data Cleaning & Preparation
## Overview
This project focuses on cleaning and preparing a raw dataset for analysis. The goal is to ensure data quality by handling missing values, removing duplicates, and correcting data formats before performing any analysis or visualization.

## Project Objective
* Identify and handle missing values.
* Detect and remove duplicate records.
* Validate and correct date formats.
* Prepare a clean dataset for further analytics tasks.

## Technologies Used
* Python
* Pandas
* OpenPyXL
* Microsoft Excel

## Dataset
The dataset contains transaction/order-related information including:
* Order IDs
* Dates
* Customer Details
* Product Information
* Coupon Codes

## Data Cleaning Tasks Performed
### 1. Missing Value Handling
* Identified null values in the dataset.
* Replaced missing values in the `CouponCode` column with `NO_COUPON`.

### 2. Duplicate Detection
* Checked for duplicate rows.
* Verified duplicate Order IDs.
* Removed duplicates where applicable.

### 3. Date Format Validation
* Converted date columns into standard datetime format.
* Verified that no incorrectly formatted dates remained.

### 4. Data Verification
* Confirmed:
  * Zero duplicate Order IDs
  * Zero incorrectly formatted dates
  * Clean and analysis-ready dataset

## Project Structure
Data-Analytics-Project-1/

├── Dataset for Data Analytics.xlsx

├── Cleaned_Dataset.xlsx

├── project1.py

└── README.md

## Python Libraries Required
pip install pandas openpyxl

## How to Run
python project1.py

## Output
The script generates:
Cleaned_Dataset.xlsx
containing the cleaned and validated data.

## Learning Outcomes
Through this project, I learned:
* Data cleaning techniques
* Handling missing values
* Removing duplicates
* Working with Excel files using Python
* Data preparation best practices
* Using Pandas for real-world datasets

## Author
Vedant Sonparote

## Internship Program
Data Analytics – Project 1
