# Automated-Data-Cleaning-System-using-python
The Automated Data Cleaning System using Python streamlines preprocessing for CSV and Excel datasets, using Pandas and NumPy to remove duplicates, handle missing values, and ensure data integrity. It supports mean imputation, categorical filtering, and automated file detection, making it ideal for ETL and machine learning workflows.


## Overview

The Automated Data Cleaning System using Python streamlines preprocessing for CSV and Excel datasets, ensuring data integrity for analysis and machine learning. It detects and removes duplicates, handles missing values using mean imputation, and validates file paths. Built with Pandas, NumPy, OpenPyXL, and OS modules, it automates dataset cleaning and saves both cleaned and duplicate records, making it ideal for ETL workflows and data preprocessing tasks. 


## Objectives

- Automate the cleaning process for CSV and Excel datasets to ensure data integrity.
- Detect and remove duplicate records, saving them separately for reference.
- Handle missing values by applying mean imputation for numerical data and dropping categorical entries with null values.
- Validate file paths and ensure correct file format detection (CSV or Excel).
- Save cleaned datasets automatically for further analysis and machine learning workflows.

## Tasks
- To create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- It should check number of duplicats and remove all the duplicates 
- It should keep a copy of all the duplicates
- It should check for missing values 
- If any column that is numeric it should replace nulls with mean else it should drop that rows
- At end it should save the data as clean data and also return 
- Duplicates records, clean_data 


# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# data_path = 'sales.xlsx'
# data_name = 'jan_sales'
