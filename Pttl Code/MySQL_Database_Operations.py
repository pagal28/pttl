# ---------------------------------------------------------
# Program: MySQL Database CRUD Operations using Python
# Subject: Python Practical (Database Connectivity)
# Author: <Your Name>
# ---------------------------------------------------------

import pymysql

# ------------------- Function 1 -------------------
def connect_database():
    """
    Establishes a connection to the MySQL database.
    Returns: connection and cursor objects.
    """
    try:
        conn = pymysql.connect(
            host='localhost',     # MySQL server (use '127.0.0.1' if localhost fails)
            user='root',          # Your MySQL username
            password='1234',      # Your MySQL password
            database='testdb'     # Database name
        )
        cursor = conn.cursor()
        print("✅ Connected to MySQL Database successfully!\n")
        return conn, cursor
    except Exception as e:
        print(f"❌ Database Connection Failed: {e}")
        exit()


# ------------------- Function 2 -------------------
def create_table(cursor):
    """
    Creates a table named 'students' if not already present.
    """
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
    """
    cursor.execute(query)
    print("✅ Table 'students' created (if not exists).\n")


# ------------------- Function 3 -------------------
def insert_record(cursor, conn):
    """
    Inserts a new student record into the table.
    """
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print("✅ Record inserted successfully!\n")


# ------------------- Function 4 -------------------
def read_records(cursor):
    """
    Reads and displays records with optional condition.
    """
    condition = input("Enter condition (e.g., age > 20) or press Enter for all: ")
    query = "SELECT * FROM students"
    if condition.strip():
        query += " WHERE " + condition
    cursor.execute(query)
    records = cursor.fetchall()
    print("\n--- Student Records ---")
    for record in records:
        print(record)
    print("-----------------------\n")


# ------------------- Function 5 -------------------
def update_record(cursor, conn):
    """
    Updates an existing student record.
    """
    name = input("Enter the name of student to update: ")
    new_age = int(input("Enter new age: "))
    cursor.execute("UPDATE students SET age = %s WHERE name = %s", (new_age, name))
    conn.commit()
    print("✅ Record updated successfully!\n")


# ------------------- Function 6 -------------------
def delete_record(cursor, conn):
    """
    Deletes a student record from the table.
    """
    name = input("Enter the name of student to delete: ")
    cursor.execute("DELETE FROM students WHERE name = %s", (name,))
    conn.commit()
    print("✅ Record deleted successfully!\n")


# ------------------- Main Function -------------------
def main():
    conn, cursor = connect_database()
    create_table(cursor)

    while True:
        print("=== MySQL CRUD MENU ===")
        print("1. Insert Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert_record(cursor, conn)
        elif choice == '2':
            read_records(cursor)
        elif choice == '3':
            update_record(cursor, conn)
        elif choice == '4':
            delete_record(cursor, conn)
        elif choice == '5':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

    cursor.close()
    conn.close()


# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()




# 🧩 How to Run
# 1️⃣ Install the required library (only once)

# Open your terminal or VS Code and run:

# pip install pymysql

# 2️⃣ Ensure MySQL is running

# Open your MySQL Workbench / XAMPP / WAMP and start the MySQL server.

# 3️⃣ Create a database

# In MySQL:

# CREATE DATABASE testdb;

# 4️⃣ Run the program
# python assignment3_mysql.py

# 🧾 Sample Output
# ✅ Connected to MySQL Database successfully!
# ✅ Table 'students' created (if not exists).

# === MySQL CRUD MENU ===
# 1. Insert Record
# 2. Read Records
# 3. Update Record
# 4. Delete Record
# 5. Exit
# Enter your choice (1-5): 1
# Enter student name: Aryan
# Enter student age: 21
# ✅ Record inserted successfully!

# Enter your choice (1-5): 2
# Enter condition (e.g., age > 20) or press Enter for all:
# --- Student Records ---
# (1, 'Aryan', 21)
# -----------------------

# Enter your choice (1-5): 3
# Enter the name of student to update: Aryan
# Enter new age: 22
# ✅ Record updated successfully!

# Enter your choice (1-5): 5
# 👋 Exiting program...