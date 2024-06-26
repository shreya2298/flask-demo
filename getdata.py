import mysql.connector

def fetch_all_rows_as_dict(id):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='192.168.1.2',
            user='root',
            password='shreya',
            
            database='flaskdb'
        )

        cursor = connection.cursor(dictionary=True)
        # query = "SELECT * FROM userdata"
        query = f"SELECT * FROM userdata WHERE id = {id}"

        cursor.execute(query)
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        # Convert the rows to a list of dictionaries
        result = []
        for row in rows:
            result.append(dict(row))
        
        return result

    except mysql.connector.Error as err:
        return f"Error: {err}"
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
