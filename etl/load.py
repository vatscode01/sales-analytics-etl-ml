import psycopg2
from config import db_config

# connection = psycopg2.connect(database="etl_pipline", user="postgres", password="aady_02", 
#                               host="localhost", port=5432)

# cursor = connection.cursor()

# cursor.execute("SELECT * from portal.portal_users;")

# # Fetch all rows from database
# record = cursor.fetchall()

# print("Data from Database:- ", record)

connection = psycopg2.connect(**db_config);

# cursor = connection.cursor()