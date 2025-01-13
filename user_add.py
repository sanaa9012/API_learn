import psycopg2
from psycopg2 import sql
import os

def insert_cars(brand, model, year, color, user_id):
    print('Insert function called!')
    
    conn = psycopg2.connect(
        dbname=os.getenv('DBNAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    
    cursor = conn.cursor()
    
    try:
        # SQL query to insert data into the users table
        insert_query = """
            INSERT INTO cars (brand, model, year, color, user_id)
            VALUES (%s, %s, %s, %s, %s);
        """
        
        # Execute the query with provided values
        cursor.execute(insert_query, (brand, model, year, color, user_id))
        
        # Commit the transaction
        conn.commit()
        
        print("Data inserted successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()  # Rollback in case of error
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
# Call the function 
insert_cars("her", "model1", "1982", "teal", "94971190-e7dd-4395-8849-9771406ee006")    


