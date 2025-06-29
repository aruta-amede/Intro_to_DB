#!/usr/bin/python3
"""
Python script to create the 'alx_book_store' database in MySQL.
Includes all required components: file existence, correct imports, 
connection handling, database creation, and exception management.
"""

import mysql.connector  # Required import statement
from mysql.connector import Error

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
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
