import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
filename = input("Enter the dataset file name (with .csv extension): ")

try:
    df = pd.read_csv(filename)
    print("\n✅ Dataset loaded successfully!\n")

    # Step 2: Display basic information
    print("📋 First 5 rows of the dataset:")
    print(df.head())

    print("\n📊 Dataset Summary:")
    print(df.info())

    print("\n📈 Descriptive Statistics:")
    print(df.describe())

    # Step 3: Check for missing values
    print("\n🔍 Missing Values per Column:")
    print(df.isnull().sum())

    # Step 4: Handle missing values (optional)
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Step 5: Generate insightful plots
    print("\n🖼️ Generating insightful plots...")

    # 1️⃣ Histogram for numerical data
    df.hist(figsize=(10, 6), bins=20, color='skyblue', edgecolor='black')
    plt.suptitle("Distribution of Numerical Features", fontsize=14)
    plt.show()

    # 2️⃣ Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

    # 3️⃣ Boxplot to check for outliers
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df.select_dtypes(include=['float64', 'int64']))
    plt.title("Boxplot of Numeric Columns (Outlier Detection)")
    plt.show()

    # 4️⃣ If categorical columns exist, show category counts
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=col, palette='viridis')
        plt.title(f"Count of Categories in {col}")
        plt.xticks(rotation=30)
        plt.show()

    # 5️⃣ Pairplot for numerical relationships
    if len(df.select_dtypes(include=['float64', 'int64']).columns) >= 2:
        sns.pairplot(df.select_dtypes(include=['float64', 'int64']))
        plt.suptitle("Pairplot of Numerical Features", y=1.02)
        plt.show()

    print("\n✅ Analysis completed successfully!")

except FileNotFoundError:
    print("⚠️ Error: File not found. Please check the file name and try again.")
