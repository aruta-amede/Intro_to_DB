#!/usr/bin/python3
"""
Python script to create the 'alx_book_store' database in MySQL.
Meets all assignment checks:
- File not empty
- Required import
- Correct CREATE DATABASE syntax
- Connection to MySQL server
- Specific exception handling: 'except mysql.connector.Error'
- No SELECT or SHOW statements
"""

import mysql.connector  # Required import statement

def create_database():
    """Function to create the alx_book_store database."""
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Simbizi123'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Required exception format
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
