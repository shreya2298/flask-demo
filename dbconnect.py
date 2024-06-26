import mysql.connector

def insert_data(values):

    conn = mysql.connector.connect(
        host='192.168.1.2',
        user='root',
        password='shreya',
        database='flaskdb'
    )
    # Creating cursor object
    cursor = conn.cursor()
    
    # Insert command/statement with named placeholders
    insert_st = "INSERT INTO userdata(id, name, age) VALUES (%(id)s, %(name)s, %(age)s)"

    try:
        # Iterate over each dictionary and execute the insert statement
        for val in values:
            cursor.execute(insert_st, val)

        # Commit changes to the database
        conn.commit()
        print("Data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")

    finally:
        # Disconnect from server
        cursor.close()
        conn.close()
        print("Connection closed.")
        
        return "Data inserted"


# raw = [
#     {"id": "20", "name": "Bhushii", "age": "30"},
#     {"id": "31", "name": "Shreu", "age": "25"},
# ]

# insert_data(raw)



def get_data(table, id):

    conn = mysql.connector.connect(
        host='192.168.1.2',
        user='root',
        password='shreya',
        database='flaskdb'
    )
    # Creating cursor object
    cursor = conn.cursor()
    
    # Insert command/statement with named placeholders
    select_st = f"SELECT * FROM {table} WHERE id = {id}"

    try:
        cursor.execute(select_st, val)
        conn.commit()
        print("Data returned successfully!")

    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")

    finally:
        # Disconnect from server
        cursor.close()
        conn.close()
        print("Connection closed.")
        
        return "Data got"

get_data("userdata",1)
# raw = [
#     {"id": "20", "name": "Bhushii", "age": "30"},
#     {"id": "31", "name": "Shreu", "age": "25"},
# ]

# insert_data(raw)