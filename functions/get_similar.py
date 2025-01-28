import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import get_similar_query

def get_similar():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cursor.execute(get_similar_query)
    similar = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return similar