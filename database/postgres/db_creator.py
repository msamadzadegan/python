import psycopg2
from psycopg2 import sql
import random
import string
from datetime import datetime, timedelta

# Database connection parameters
db_params = {
    'dbname': 'my_database',
    'user': 'my_user',
    'password': 'my_password',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Function to create tables
def create_tables():
    for i in range(10):
        table_name = f"table_{i+1}"
        cur.execute(sql.SQL("""
            CREATE TABLE IF NOT EXISTS {} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                email VARCHAR(255),
                address TEXT,
                date_joined TIMESTAMP
            )
        """).format(sql.Identifier(table_name)))
    conn.commit()

# Function to generate random data
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def insert_data(table_name, num_records):
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2024, 1, 1)
    
    for _ in range(num_records):
        name = random_string(10)
        age = random.randint(18, 100)
        email = f"{random_string(5)}@{random_string(3)}.com"
        address = random_string(50)
        date_joined = random_date(start_date, end_date)
        
        cur.execute(sql.SQL("""
            INSERT INTO {} (name, age, email, address, date_joined)
            VALUES (%s, %s, %s, %s, %s)
        """).format(sql.Identifier(table_name)), (name, age, email, address, date_joined))
    
    conn.commit()

# Create tables
create_tables()

# Insert random data into each table
num_records_per_table = 1000000  # Adjust this number based on the size of data you want
for i in range(10):
    insert_data(f"table_{i+1}", num_records_per_table)

# Close the database connection
cur.close()
conn.close()
