#Before running:

#Install MySQL connector:

#pip install mysql-connector-python

#Ensure MySQL is running and you have a database named testdb.

#CREATE DATABASE testdb;

import mysql.connector

# Step 1: Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",         # Change this to your MySQL username
    password="password", # Change this to your MySQL password
    database="testdb"    # Ensure this database exists, or create it first
)

cursor = connection.cursor()
print("✅ Connected to MySQL database successfully!")

# Step 2: Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(50),
        salary FLOAT
    )
""")
print("🧱 Table 'employees' created successfully!")

# Step 3: Insert sample data
sample_data = [
    ("Sneha Bansal", "IT", 55000),
    ("Amit Sharma", "HR", 40000),
    ("Neha Patel", "Finance", 60000),
    ("Rahul Verma", "IT", 70000)
]

cursor.executemany("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", sample_data)
connection.commit()
print("📥 Sample data inserted successfully!")

# Step 4: Select query with conditions
print("\n📊 Employees in IT department with salary > 50000:")
cursor.execute("SELECT * FROM employees WHERE department = 'IT' AND salary > 50000")
for row in cursor.fetchall():
    print(row)

# Step 5: Update records
cursor.execute("UPDATE employees SET salary = salary + 5000 WHERE department = 'HR'")
connection.commit()
print("\n💰 Updated salary for HR department employees!")

# Step 6: Delete records
cursor.execute("DELETE FROM employees WHERE salary < 45000")
connection.commit()
print("🗑️ Deleted employees with salary less than 45000!")

# Step 7: Display remaining records
print("\n📋 Remaining employees:")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# Step 8: Close connection
cursor.close()
connection.close()
print("\n🔒 MySQL connection closed.")
