# This is a data cleaning application 


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