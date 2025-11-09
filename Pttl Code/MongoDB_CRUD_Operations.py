# ---------------------------------------------------------
# Program: MongoDB CRUD Operations using Python (PyMongo)
# Subject: Python Practical (Database Connectivity)
# Author: <Your Name>
# ---------------------------------------------------------

from pymongo import MongoClient

# ------------------- Function 1 -------------------
def connect_mongodb():
    """
    Connect to MongoDB database and return the collection object.
    """
    try:
        client = MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB
        db = client["school_db"]  # Create or connect to database
        collection = db["students_collection"]  # Create or connect to collection
        print("✅ Connected to MongoDB successfully!\n")
        return client, collection
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        exit()


# ------------------- Function 2 -------------------
def insert_data(collection):
    """
    Insert one or multiple student documents into the collection.
    """
    print("\n--- INSERT DATA ---")
    n = int(input("How many student records do you want to insert? "))
    students = []
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        students.append({"name": name, "age": age, "grade": grade})
    if n == 1:
        collection.insert_one(students[0])
    else:
        collection.insert_many(students)
    print("✅ Record(s) inserted successfully!\n")


# ------------------- Function 3 -------------------
def read_data(collection):
    """
    Read and display student documents (with optional condition).
    """
    print("\n--- READ DATA ---")
    choice = input("Do you want to apply a condition? (yes/no): ").lower()
    if choice == "yes":
        field = input("Enter field name (e.g., age): ")
        value = input("Enter condition value (e.g., 20): ")
        try:
            value = int(value)
        except:
            pass
        query = {field: value}
        records = collection.find(query)
    else:
        records = collection.find()

    print("\n--- Student Records ---")
    for rec in records:
        print(rec)
    print("-----------------------\n")


# ------------------- Function 4 -------------------
def update_data(collection):
    """
    Update a student document based on name or condition.
    """
    print("\n--- UPDATE DATA ---")
    name = input("Enter student name to update: ")
    field = input("Enter field to update (e.g., grade): ")
    new_value = input("Enter new value: ")
    result = collection.update_one({"name": name}, {"$set": {field: new_value}})
    if result.modified_count > 0:
        print("✅ Record updated successfully!\n")
    else:
        print("⚠️ No record found with that name.\n")


# ------------------- Function 5 -------------------
def delete_data(collection):
    """
    Delete a student record by name.
    """
    print("\n--- DELETE DATA ---")
    name = input("Enter student name to delete: ")
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("✅ Record deleted successfully!\n")
    else:
        print("⚠️ No record found with that name.\n")


# ------------------- Main Function -------------------
def main():
    client, collection = connect_mongodb()

    while True:
        print("=== MONGODB CRUD MENU ===")
        print("1. Insert Record(s)")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert_data(collection)
        elif choice == '2':
            read_data(collection)
        elif choice == '3':
            update_data(collection)
        elif choice == '4':
            delete_data(collection)
        elif choice == '5':
            print("👋 Exiting program...")
            client.close()
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()



# 🧩 How to Run
# 1️⃣ Install PyMongo (only once)
# pip install pymongo

# 2️⃣ Start MongoDB server

# If you’re using:

# MongoDB Compass / Local MongoDB, start the Mongo service.

# Default URI is mongodb://localhost:27017/.

# 3️⃣ Run the program
# python assignment4_mongo.py

# 🧾 Sample Output
# ✅ Connected to MongoDB successfully!

# === MONGODB CRUD MENU ===
# 1. Insert Record(s)
# 2. Read Records
# 3. Update Record
# 4. Delete Record
# 5. Exit
# Enter your choice (1-5): 1

# --- INSERT DATA ---
# How many student records do you want to insert? 2
# Enter name: Aarav
# Enter age: 21
# Enter grade: A
# Enter name: Riya
# Enter age: 22
# Enter grade: B
# ✅ Record(s) inserted successfully!

# Enter your choice (1-5): 2
# Do you want to apply a condition? (yes/no): yes
# Enter field name (e.g., age): age
# Enter condition value (e.g., 20): 21

# --- Student Records ---
# {'_id': ObjectId('...'), 'name': 'Aarav', 'age': 21, 'grade': 'A'}
# -----------------------

# Enter your choice (1-5): 3
# --- UPDATE DATA ---
# Enter student name to update: Aarav
# Enter field to update (e.g., grade): grade
# Enter new value: A+
# ✅ Record updated successfully!

# Enter your choice (1-5): 4
# --- DELETE DATA ---
# Enter student name to delete: Riya
# ✅ Record deleted successfully!

# Enter your choice (1-5): 5
# 👋 Exiting program...
