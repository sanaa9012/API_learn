import pandas as pd
import psycopg2
import os 

DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DBNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_USER = os.getenv('USER')

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)

query = "SELECT * FROM sales_data"

try:
    df = pd.read_sql_query(query, conn)
    
    df.to_csv('data.csv', index = False)
    
    print("Data exported successfully!")
    
finally:
    conn.close()