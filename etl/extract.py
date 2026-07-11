import pandas as pd
import os
from pathlib import Path

raw_file_path = '/Users/aady/Desktop/Ayush Vats/ETL Pipeline Project/data/raw'
raw_files = []

# List of objects of raw data paths
obj = os.scandir(raw_file_path)

# Create a list of raw/ directory file_name and file_path
for x in obj:
    if x.is_file():
        raw_files.append([x.name , x.path])

def get_amazon_data():
    for name,path in raw_files:
        if(name.startswith('Amazon')):
            return path
        

def get_sales_data():
    for name,path in raw_files:
        if(name.startswith('Sale')):
            return path
        

def get_cloud_warehouse_data():
    for name,path in raw_files:
        if(name.startswith('Cloud')):
            return path