# ---------------------------------------------------------
# Program: Email Validation using Regular Expressions
# Subject: Python Practical (re Module)
# Author: <Your Name>
# ---------------------------------------------------------

import re  # Importing Regular Expression module

# ------------------- User Defined Function -------------------
def validate_email(email):
    """
    Function to validate an email address using regex.
    Parameters:
        email (str): Email address entered by the user.
    Returns:
        bool: True if valid, False if invalid.
    """
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Using re.fullmatch() to check entire string validity
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


# ------------------- Main Program -------------------
def main():
    print("=== EMAIL VALIDATION PROGRAM USING REGEX ===")
    email = input("Enter an email address to validate: ")

    # Calling the user-defined function
    if validate_email(email):
        print("✅ The entered email address is VALID.")
    else:
        print("❌ The entered email address is INVALID.")

# Entry point
if __name__ == "__main__":
    main()
