import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email using regex
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate and display data
def submit_form():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()
    gender = gender_var.get()

    # Validation checks
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Input Error", "Age must be a positive number!")
        return
    if not is_valid_email(email):
        messagebox.showerror("Input Error", "Invalid email address!")
        return
    if gender == "":
        messagebox.showerror("Input Error", "Please select your gender!")
        return

    # Display submitted data
    result_label.config(
        text=f"✅ Submitted Data:\nName: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}",
        fg="green"
    )

    # Clear fields after submission
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    gender_var.set("")

# Create the main window
root = tk.Tk()
root.title("User Input Form")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title Label
tk.Label(root, text="User Registration Form", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# Name Field
tk.Label(root, text="Name:", bg="#f0f0f0").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

# Age Field
tk.Label(root, text="Age:", bg="#f0f0f0").pack()
entry_age = tk.Entry(root, width=40)
entry_age.pack(pady=5)

# Email Field
tk.Label(root, text="Email:", bg="#f0f0f0").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

# Gender Selection (Radio Buttons)
tk.Label(root, text="Gender:", bg="#f0f0f0").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#f0f0f0").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#f0f0f0").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", bg="#f0f0f0").pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="white", width=15).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10, "bold"))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
