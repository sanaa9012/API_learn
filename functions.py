import pandas as pd
from sharedcode.db_connections import get_db_connection
from sharedcode.query import keyword_query

conn = get_db_connection()

try:
    df = pd.read_sql_query(keyword_query, conn)
    
finally: 
    conn.close()
    
print(df.head())