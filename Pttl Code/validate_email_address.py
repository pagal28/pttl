import re

# Regular expression pattern for validating an email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Take user input
email = input("Enter your email address: ")

# Check if the email matches the pattern
if re.match(email_pattern, email):
    print("✅ Valid email address!")
else:
    print("❌ Invalid email address. Please enter a valid one.")
