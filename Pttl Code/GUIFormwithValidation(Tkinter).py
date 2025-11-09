# ---------------------------------------------------------
# Program: GUI Form with Validation using Tkinter
# Subject: Python Practical – GUI in Python
# Author: <Your Name>
# ---------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import re
import csv

# ------------------- Validation Functions -------------------
def validate_name(name):
    """Validates that name contains only alphabets and spaces."""
    return bool(re.fullmatch(r'[A-Za-z ]+', name.strip()))

def validate_email(email):
    """Validates standard email format."""
    return bool(re.fullmatch(r'[\w\.-]+@[\w\.-]+\.\w+', email.strip()))

def validate_age(age):
    """Validates age (1-120)."""
    return age.isdigit() and (0 < int(age) < 120)

def validate_phone(phone):
    """Validates 10-digit phone number."""
    return bool(re.fullmatch(r'\d{10}', phone.strip()))

# ------------------- Form Submission -------------------
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    phone = entry_phone.get()
    gender = gender_var.get()

    # Validation checks
    if not validate_name(name):
        messagebox.showerror("Invalid Input", "Enter a valid name (letters only).")
        return
    if not validate_email(email):
        messagebox.showerror("Invalid Input", "Enter a valid email.")
        return
    if not validate_age(age):
        messagebox.showerror("Invalid Input", "Enter a valid age (1–120).")
        return
    if not validate_phone(phone):
        messagebox.showerror("Invalid Input", "Enter a 10-digit phone number.")
        return
    if gender == "":
        messagebox.showerror("Invalid Input", "Select a gender.")
        return

    # Insert data into table
    tree.insert("", "end", values=(name, email, age, phone, gender))
    clear_form()
    messagebox.showinfo("Success", "Data submitted successfully!")

# ------------------- Clear Form -------------------
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    gender_var.set("")

# ------------------- Export to CSV -------------------
def export_data():
    rows = tree.get_children()
    if not rows:
        messagebox.showwarning("No Data", "No records to export.")
        return

    with open("form_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Age", "Phone", "Gender"])
        for row in rows:
            writer.writerow(tree.item(row)["values"])
    messagebox.showinfo("Exported", "Data exported to form_data.csv")

# ------------------- Delete Row -------------------
def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Select a row to delete.")
        return
    tree.delete(selected)
    messagebox.showinfo("Deleted", "Selected record deleted.")

# ------------------- GUI Setup -------------------
root = tk.Tk()
root.title("User Registration Form")
root.geometry("750x450")
root.configure(bg="#f3f4f6")

# Labels and Inputs
tk.Label(root, text="Name:", bg="#f3f4f6").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", bg="#f3f4f6").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root, width=25)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:", bg="#f3f4f6").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(root, width=25)
entry_age.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", bg="#f3f4f6").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_phone = tk.Entry(root, width=25)
entry_phone.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:", bg="#f3f4f6").grid(row=4, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar()
ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"], width=22).grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Submit", command=submit_form, bg="#16a34a", fg="white").grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_form, bg="#2563eb", fg="white").grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Export CSV", command=export_data, bg="#f59e0b", fg="white").grid(row=5, column=2, padx=10, pady=10)
tk.Button(root, text="Delete Row", command=delete_selected, bg="#dc2626", fg="white").grid(row=5, column=3, padx=10, pady=10)

# Table
columns = ("Name", "Email", "Age", "Phone", "Gender")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
