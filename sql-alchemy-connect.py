from sqlalchemy import create_engine, text

# Define the connection parameters
host = '192.168.1.2'
user = 'root'
password = 'shreya'
database = 'flaskdb'

# Create the connection string
connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

# Connect to the database
engine = create_engine(connection_string)

# Test the connection
connection = engine.connect()

# Insert statement with named placeholders
insert_st = text("INSERT INTO userdata (id, name, age) VALUES (:id, :name, :age)")

# Values to insert
values = [
    {'id': '3', 'name': 'Bhushan', 'age': '30'},
    {'id': '2', 'name': 'Shreya', 'age': '25'}
]

try:
    # Begin a transaction
    with connection.begin() as transaction:
        # Iterate over each dictionary and execute the insert statement
        for val in values:
            connection.execute(insert_st, **val)
    print("Data inserted successfully!")

except Exception as e:
    print(f"Error inserting data: {e}")

finally:
    # Close the connection
    connection.close()
    print("Connection closed.")
