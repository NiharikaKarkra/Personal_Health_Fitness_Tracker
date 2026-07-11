import mysql.connector
from config import DB_CONFIG

#Connecting Database

def connect_database():
    """
    Creates and returns a MYSQL database connection.
    """

    try: 
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            #print("Connected to MYSQL database")
            return connection

    except mysql.connector.Error as error:
        #print("Database Connection Error:", error)
        return None

#Executing Query

def execute_query(query, values=None):
    """
    Execute INSERT, UPDATE and DELETE queries.
    """

    connection = connect_database()

    if connection is None:
        return False
    cursor = connection.cursor()

    try:
        cursor.execute(query, values)
        connection.commit()
        return True
    
    except Exception as error:
        print(error)
        return False
    
    finally:
        cursor.close()
        connection.close()

#Fetch one record

def fetch_one(query, values=None):
    """
    Returns one record.
    """
    connection = connect_database()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute(query, values)
        return cursor.fetchone()
    
    except Exception as error:
        print(error)
        return None

    finally:
        
        cursor.close()
        connection.close()

#Fetch multiple record

def fetch_all(query, values=None):
    """
    Returns multiple rows.
    """

    connection = connect_database()

    if connection is None:
        return[]
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, values)
        return cursor.fetchall()

    except Exception as error:
        print(error)
        return[]

    finally:
        cursor.close()
        connection.close()



