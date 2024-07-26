import os
import sqlite3

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

    data = read_file("../../../etc/passwd")
    print(data)
