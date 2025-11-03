import re

# Get file name from user
filename = input("Enter the name of the text file (with extension): ")

try:
    # Read the file content
    with open(filename, 'r') as file:
        text = file.read()

    # Get search and replace patterns from user
    search_pattern = input("Enter the text or regex pattern to search for: ")
    replace_text = input("Enter the replacement text: ")

    # Perform search and replace using regular expressions
    new_text = re.sub(search_pattern, replace_text, text)

    # Display the updated content
    print("\n--- Updated File Content ---")
    print(new_text)

    # Ask user if they want to save changes
    choice = input("\nDo you want to overwrite the file with changes? (yes/no): ").lower()
    if choice == 'yes':
        with open(filename, 'w') as file:
            file.write(new_text)
        print("✅ File updated successfully!")
    else:
        print("❌ Changes not saved.")

except FileNotFoundError:
    print("⚠️ Error: File not found. Please check the file name and try again.")
