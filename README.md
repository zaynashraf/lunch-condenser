# Lunch Metrics Condenser
## Overview
Python-based script designed to process registration data from Excel or CSV files, specifically focusing on lunch-related responses. It consolidates two columns ("Lunch Purchase" and "Lunch") into one singular column ("Lunch Included"), generating a clean output file and summary metrics to assist event organizers.

## Features
Automated Lunch Data Processing: Merges and normalizes values from Lunch and Lunch Purchase columns into a single, simplified column (Lunch Included).

Condensed Metrics Output: Displays clear summaries of lunch selections (Yes/No) for easy tracking and reporting.

File Format Support: Handles both .csv and .xlsx/.xls files for flexible input options.

Data Cleaning: Replaces verbose responses with simplified categories to reduce clutter and confusion.

Output File Generation: Saves a cleaned CSV file with condensed lunch data (<original_filename>_condensed.csv).

Auto Dependency Handling: Installs pandas automatically if not already available in the environment.

## Technologies Used
Python

pandas – for data manipulation and analysis

## How to Run
Make sure Python is installed on your system.

Open a terminal or command prompt.

Run the script using:

```
python condenser.py [your_input_file.xlsx or .csv]
```
If no file is provided, it defaults to Registration Badge Printing.xlsx.

View the console output for lunch metrics.

Check directory for the new file:

```php
<original_filename>_condensed.csv
```
