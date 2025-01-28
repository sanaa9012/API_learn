import pandas as pd
import psycopg2
from sharedcode.db_connections import get_db_connection

conn = get_db_connection()

query = "SELECT * FROM sales_data"

try:
    df = pd.read_sql_query(query, conn)
    
    df.to_csv('data.csv', index = False)
    
    print("Data exported successfully!")
    
finally:
    conn.close()
    
print(df.head())