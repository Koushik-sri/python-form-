import mysql.connector 
# this need to be imported by "pip install mysql-connector-python"
import getpass
# for hiding the password input (optional)
username = input("Enter ur name:")
password = getpass.getpass("Enter ur password:") 
# hides password in terminal

try :
    conn = mysql.connector.connect(
        host="localhost",
        user="your mysql username",
        password="your mysql password",
        database="user_data"
    )
    # this is used to connect to the database
    
    cursor = conn.cursor()
    # this is used to create a cursor object to execute SQL queries
    
    query = "INSERT INTO users (username,password) values (%s,%s)"
    # It’s telling MySQL:
    # "Insert a new row into the users table, and set the username and password columns." 
    # %s are placeholders for the actual values (to prevent SQL injection attacks).
    
    values = (username, password)
    #This is a tuple of values that will replace %s in the query.
    
    cursor.execute(query, values)
    # This executes the query with the provided values.
    
    conn.commit()
    # This commits the transaction, making the changes permanent in the database.
    
    print("User registered successfully!")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    # This will print any error that occurs during the connection or execution of the query.    
    
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        # This ensures that the cursor and connection are closed properly, even if an error occurs.
        