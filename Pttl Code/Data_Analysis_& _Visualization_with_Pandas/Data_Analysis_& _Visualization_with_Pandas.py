# ---------------------------------------------------------
# Program: Data Analysis & Visualization using Pandas
# Subject: Python Practical – Pandas + Visualization
# Author: <Your Name>
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------- User Defined Functions -------------------

def load_data():
    """Loads dataset from CSV."""
    file = input("Enter dataset filename (e.g., data2.csv): ")
    df = pd.read_csv(file)
    df['Month'] = pd.to_datetime(df['Month'])
    print("\n✅ Dataset loaded successfully!\n")
    print("Preview:\n", df.head())
    return df


def analyze_data(df):
    """Performs descriptive analysis and grouping."""
    print("\n--- Summary Statistics ---")
    print(df.describe())

    product_sales = df.groupby("Product")["Sales"].sum()
    region_sales = df.groupby("Region")["Sales"].sum()
    monthly_sales = df.groupby("Month")["Sales"].sum()
    profit_product = df.groupby("Product")["Profit"].sum()

    return product_sales, region_sales, monthly_sales, profit_product


def visualize_data(product_sales, region_sales, monthly_sales, df):
    """Generates various visualizations."""

    # 1. Bar Chart – Sales by Product
    plt.figure(figsize=(7,5))
    sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis")
    plt.title("Total Sales by Product")
    plt.ylabel("Sales")
    plt.show()

    # 2. Line Chart – Monthly Trend
    plt.figure(figsize=(8,5))
    monthly_sales.plot(marker='o', linestyle='-', color="blue")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

    # 3. Pie Chart – Sales by Region
    plt.figure(figsize=(6,6))
    region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap="Set3")
    plt.title("Sales Distribution by Region")
    plt.ylabel("")
    plt.show()

    # 4. Scatter Plot – Sales vs Profit
    plt.figure(figsize=(7,5))
    sns.scatterplot(x="Sales", y="Profit", hue="Product", size="Region",
                    data=df, palette="Set1", sizes=(50,200))
    plt.title("Sales vs Profit by Product & Region")
    plt.show()

    # 5. Box Plot – Profit by Product
    plt.figure(figsize=(7,5))
    sns.boxplot(x="Product", y="Profit", data=df, palette="coolwarm")
    plt.title("Profit Distribution by Product")
    plt.show()


# ------------------- Main Program -------------------

def main():
    print("=== PANDAS DATA ANALYSIS & VISUALIZATION ===")
    df = load_data()
    product_sales, region_sales, monthly_sales, profit_product = analyze_data(df)
    visualize_data(product_sales, region_sales, monthly_sales, df)
    print("\n✅ Analysis & visualization completed successfully!")


if __name__ == "__main__":
    main()

# python -m venv myenv
# myenv\Scripts\activate
# pip install pandas matplotlib seaborn

# Sample Dataset (data2.csv)
# Month	Product	Region	Sales	Profit
# 2025-01	Laptop	North	40000	7000
# 2025-01	Mobile	South	30000	5000
# 2025-02	Tablet	North	25000	4000
# 2025-03	Laptop	South	45000	9000
# 2025-04	Mobile	North	32000	6000


# Month,Product,Region,Sales,Profit
# 2025-01,Laptop,North,40000,7000
# 2025-01,Mobile,South,30000,5000
# 2025-02,Tablet,North,25000,4000
# 2025-03,Laptop,South,45000,9000
# 2025-04,Mobile,North,32000,6000
