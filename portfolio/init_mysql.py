import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ankit@2002'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS portfolio_db")
            print("Database created successfully")
            
            # Switch to the new database
            cursor.execute("USE portfolio_db")
            
            # Create leads table
            cursor.execute('''CREATE TABLE IF NOT EXISTS leads 
                           (id INT AUTO_INCREMENT PRIMARY KEY, 
                            name VARCHAR(255) NOT NULL, 
                            email VARCHAR(255) NOT NULL, 
                            message TEXT, 
                            source VARCHAR(255) NOT NULL, 
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
            print("Table created successfully")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    create_database()
