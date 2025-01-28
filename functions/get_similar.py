import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import keyword_query

def get_similar(keyword):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cursor.execute(keyword_query, (keyword,))
    similar = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return similar