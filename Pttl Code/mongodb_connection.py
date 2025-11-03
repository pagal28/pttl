#pip install pymongo
#Start MongoDB server
#Run this in your terminal:
#mongod


from pymongo import MongoClient

# Step 1: Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Default local MongoDB
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
    exit()

# Step 2: Create / Select Database and Collection
db = client["sampleDB"]              # Database name
collection = db["employees"]         # Collection name

# Step 3: Create (Insert Documents)
employees_data = [
    {"name": "Sneha Bansal", "age": 23, "department": "IT", "salary": 55000},
    {"name": "Amit Sharma", "age": 27, "department": "HR", "salary": 45000},
    {"name": "Neha Patel", "age": 29, "department": "Finance", "salary": 60000},
]
insert_result = collection.insert_many(employees_data)
print(f"📥 Inserted {len(insert_result.inserted_ids)} employee records.")

# Step 4: Read (Find Documents)
print("\n📊 All Employee Records:")
for emp in collection.find():
    print(emp)

# Step 5: Read with Condition
print("\n🔍 Employees with salary > 50000:")
for emp in collection.find({"salary": {"$gt": 50000}}):
    print(emp)

# Step 6: Update (Modify a Record)
update_result = collection.update_one(
    {"name": "Amit Sharma"},
    {"$set": {"salary": 48000, "department": "Admin"}}
)
print(f"\n✏️ Updated {update_result.modified_count} record(s).")

# Step 7: Delete (Remove a Record)
delete_result = collection.delete_one({"name": "Neha Patel"})
print(f"🗑️ Deleted {delete_result.deleted_count} record(s).")

# Step 8: Display Remaining Records
print("\n📋 Remaining Employees:")
for emp in collection.find():
    print(emp)

# Step 9: Close Connection
client.close()
print("\n🔒 MongoDB connection closed.")
