# ---------------------------------------------------------
# Program: Interactive Search and Replace in File using Regex
# Subject: Python Practical (re Module + File Handling)
# Author: <Your Name>
# ---------------------------------------------------------

import re

# ------------------- Function 1 -------------------
def create_file(filename):
    """
    Creates a file and lets the user enter content line by line.
    """
    print("\n--- Create a New File ---")
    print("Enter the file contents (type 'end' on a new line to stop):")

    lines = []
    while True:
        line = input()
        if line.lower() == 'end':
            break
        lines.append(line)

    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"\n✅ File '{filename}' created successfully!\n")


# ------------------- Function 2 -------------------
def display_file(filename):
    """
    Displays file contents with line numbers.
    """
    print("\n--- Current File Contents ---")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("File is empty.")
                return []
            for i, line in enumerate(lines, start=1):
                print(f"{i}: {line.strip()}")
            return lines
    except FileNotFoundError:
        print("❌ File not found.")
        return []


# ------------------- Function 3 -------------------
def search_and_replace_line(filename, output_file):
    """
    Allows user to pick a line and perform regex-based search and replace.
    """
    lines = display_file(filename)
    if not lines:
        return
    
    try:
        line_no = int(input("\nEnter line number where you want to make changes: "))
        if line_no < 1 or line_no > len(lines):
            print("❌ Invalid line number.")
            return

        search_text = input("Enter text/pattern to search: ")
        replace_text = input("Enter replacement text: ")

        # Perform regex replacement in selected line
        updated_line = re.sub(search_text, replace_text, lines[line_no - 1])

        # Replace that line in the list
        lines[line_no - 1] = updated_line

        # Write updated content to new file
        with open(output_file, 'w') as f:
            f.writelines(lines)

        print(f"\n✅ Line updated successfully! Changes saved to '{output_file}'")

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")


# ------------------- Main Function -------------------
def main():
    print("=== INTERACTIVE SEARCH AND REPLACE USING REGEX ===")
    filename = input("Enter filename to create (with extension): ")
    create_file(filename)

    choice = input("Do you want to perform search and replace? (yes/no): ").lower()
    if choice == 'yes':
        output_file = input("Enter output filename (with extension): ")
        search_and_replace_line(filename, output_file)
    else:
        print("\nProgram exited without replacement.")


# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()
