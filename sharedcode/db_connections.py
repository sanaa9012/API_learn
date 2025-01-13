import os 
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname  =os.getenv('DBNAME'),
        user    =os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host    =os.getenv('HOST'),
        port    =os.getenv('PORT')
    )
    return conn