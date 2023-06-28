#necessary import
import psycopg2
import pandas as pd

#get credentials
credentials=[]
with open('./db_credential.txt','r') as file:
    for item in file.readlines():
        credentials.append(item.strip('\n'))

# Database connection details from credentials file on disk
host = credentials[0]
port = credentials[1]
database = credentials[2]
user = credentials[3]
password = credentials[4]


# Establish a connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Test the connection by executing a simple query
cursor.execute('SELECT version()')
version = cursor.fetchone()
print(f"PostgreSQL version: {version[0]}")

# SQL statements to create the table schemas
create_table1_query = '''
CREATE TABLE demographics (
  college_towns varchar(50) PRIMARY KEY,
  population integer,
  unemployment_rate numeric,
  median_income numeric,
  median_age numeric,
  cost_of_living_index numeric
)
'''
create_table2_query = '''
CREATE TABLE internet_speed (
  town_id serial PRIMARY KEY,
  college_towns varchar(50) REFERENCES demographics(college_towns),
  median_download_speed numeric,
  median_upload_speed numeric,
  median_latency numeric
)
'''

create_table3_query = '''
CREATE TABLE walkability_scores (
  walkability_id serial PRIMARY KEY,
  college_town varchar(50) REFERENCES demographics(college_towns),
  walk_score integer,
  bike_score integer,
  num_eateries integer
)
'''

create_table4_query = '''
CREATE TABLE coworking_spaces (
  coworking_spaces_id serial PRIMARY KEY,
  college_towns varchar(50) REFERENCES demographics(college_towns),
  num_coworking_space integer
)
'''

# Execute the SQL statements to create the tables
cursor.execute(create_table1_query)
cursor.execute(create_table2_query)
cursor.execute(create_table3_query)
cursor.execute(create_table4_query)

# Commit the changes to the database
conn.commit()

#close connection
conn.close()
