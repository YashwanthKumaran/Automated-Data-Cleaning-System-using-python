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


## This is a data cleaning application 
```python


# importing dependencies
import pandas as pd
import numpy as np
import openpyxl
import os
import time
import xlrd
import random

def data_cleaning_master(data_path,data_name):

    print("Thank you for sharing the Dataset!")

    #Checking if the path exists
    if not os.path.exists(data_path):
        print("Please enter correct path")
        return

    else:
        if data_path.endswith('.csv'):
            print("Dataset is csv")
            data = pd.read_csv(data_path , encoding_errors='ignore')
        
        elif data_path.endswith('.xlsx'):
            print("Dataset is excel file")
            data = pd.read_excel(data_path )
        
        else:
            print("Unknown file type")
            return
        

    #Showing number of records in the dataset
    print(f"The Dataset contains Total Rows:{data.shape[0]}\n Total Columns: {data.shape[1]}")

    #Start Cleaning

    #Checking Duplicates
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()

    print(f"Total duplicate records the dataset has: {total_duplicate}")

    #Saving the duplicates
    if total_duplicate > 0:
        duplicate_record = data[duplicates]
        duplicate_record.to_csv(f"{data_name}_duplicates.csv",index=None)

    #Deleting the duplicates
    df = data.drop_duplicates()

    #Finding missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_columns = df.isnull().sum()

    print(f"Total missing values in the Dataset:{total_missing_values}")
    print(f"Missing values in the Dataset by columns{missing_value_columns}")


    #Dealing with missing values
    #fillna -- int & float
    #dropna -- Any object

    columns = df.columns

    for col in columns:
        if df[col].dtype in (int,float):
            df[col].fillna(df[col].mean())
        else:
            df.dropna(subset = col, inplace = True)
            

    #Dataset is cleaned
    print(f"The Dataset is cleaned! Number of Rows{df.shape[0]}\n Number of Columns{df.shape[1]}")

    #Saving the cleaned dataset
    df.to_csv(f"{data_name}_cleaned_dataset.csv",index = None)
    print("Dataset is saved!")

if __name__ ==  "__main__":
    #Ask path and file name
    data_path = input("Enter the dataset path : ")
    data_name = input("Enter the dataset name : ")


    #Calling the function
    data_cleaning_master(data_path,data_name)
    data_path = input("Enter the Dataset path")
    data_name = input("Enter the Dataset name")

```




## Findings and Conclusion
Data Integrity: The system successfully identifies and removes duplicate records, ensuring cleaner datasets for analysis.
Missing Value Handling: Applying mean imputation for numerical data and removing incomplete categorical entries improves dataset consistency.
File Type Validation: The automated file format detection (CSV/XLSX) ensures seamless data processing without manual intervention.
Data Quality Enhancement: Cleaning the dataset improves accuracy and reliability, making it more suitable for ETL workflows and machine learning applications.
Automated Preprocessing: The system streamlines data validation, cleaning, and saving, reducing manual effort and ensuring efficient data handling.



This project is part of my portfolio, showcasing the Python skills essential for data analyst roles.



Thank you!
