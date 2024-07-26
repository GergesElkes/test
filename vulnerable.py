import os
import sqlite3
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# SQL Injection Vulnerability
def get_user_data(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

# Command Injection Vulnerability
def list_files(directory):
    files = os.system(f"ls {directory}")
    return files

# Hardcoded Secret
def connect_to_service():
    secret_key = "hardcoded_secret_key"
    return secret_key

# Clear-text Logging of Sensitive Information
def process_payment(card_number, amount):
    logging.info(f"Processing payment of {amount} for card number {card_number}")
    # Simulate payment processing
    return True

# Insufficient Input Validation
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    # Example calls to the vulnerable functions
    user_data = get_user_data("1 OR 1=1")
    print(user_data)

    files = list_files("; rm -rf /")
    print(files)

    secret = connect_to_service()
    print(f"Connecting with secret: {secret}")

    payment_status = process_payment("1234-5678-9012-3456", 100)
    print(f"Payment status: {payment_status}")

    data = read_file("../../../etc/passwd")
    print(data)
