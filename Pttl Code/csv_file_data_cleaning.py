import pandas as pd

# Step 1: Load the CSV file
filename = input("Enter the CSV file name (with extension): ")

try:
    df = pd.read_csv(filename)
    print("\n✅ CSV file loaded successfully!\n")

    # Step 2: Display first few rows
    print("📋 First 5 Rows of Data:")
    print(df.head())

    # Step 3: Check for missing values
    print("\n🔍 Missing Values Summary:")
    print(df.isnull().sum())

    # Step 4: Fill missing values (example: fill numeric columns with mean, text with 'Unknown')
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna('Unknown', inplace=True)
        else:
            df[col].fillna(df[col].mean(), inplace=True)
    print("\n🧹 Missing values filled!")

    # Step 5: Remove duplicate rows
    before = len(df)
    df.drop_duplicates(inplace=True)
    after = len(df)
    print(f"🗑️ Removed {before - after} duplicate rows.")

    # Step 6: Convert data types (example)
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
    print("🔢 Data type conversion attempted (where applicable).")

    # Step 7: Save the cleaned data to a new file
    cleaned_filename = "cleaned_" + filename
    df.to_csv(cleaned_filename, index=False)
    print(f"\n💾 Cleaned data saved as '{cleaned_filename}'")

except FileNotFoundError:
    print("⚠️ Error: File not found. Please check the file name and try again.")
