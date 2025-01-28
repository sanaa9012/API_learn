add_car_query = "INSERT INTO cars(brand, model, year, color, user_id) VALUES( %s, %s, %s, %s, %s)"

car_by_id_query = "SELECT * FROM cars WHERE user_id = %s"

cars_query = "SELECT * FROM cars"

create_user_query = "INSERT INTO users (name, email, uid) VALUES (%s, %s, %s)"

sales_data_query = "SELECT * FROM sales_data"

user_by_id_query = "SELECT * FROM users WHERE id = %s"

users_query = "SELECT * FROM users"

get_email_query = "SELECT email FROM users" 

keyword_query = "SELECT id, \"Questions\" FROM  questions, to_tsquery('english', %s) query WHERE to_tsvector('english', \"Questions\") @@ query;"