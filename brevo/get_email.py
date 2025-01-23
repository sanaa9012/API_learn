import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import get_email_query
from brevo.brevo import send_welcome_email  

def get_emails():
    
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    cursor.execute(get_email_query)
    emails = cursor.fetchall()  
    
    cursor.close()
    connection.close()
    
    for email_data in emails:
        email = email_data.get("email") 
        if email:
            send_welcome_email(email) 
    
    return {"message": "Welcome emails sent successfully!"}