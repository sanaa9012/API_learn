import pandas as pd
import psycopg2
import os
from psycopg2 import sql
import openpyxl

DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DBNAME')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')

excel_file = "data.xlsx"

df = pd.read_excel(excel_file)

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(
    'INSERT INTO sales_data ("Postcode", "Sales_Rep_ID", "Sales_Rep_Name", "Year", "Value") VALUES (%s, %s, %s, %s, %s)', (row['Postcode'], row['Sales_Rep_ID'], row['Sales_Rep_Name'], row['Year'], row['Value']))
 
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully.")