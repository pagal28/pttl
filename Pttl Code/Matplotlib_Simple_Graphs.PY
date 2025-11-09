# ---------------------------------------------------------
# Program: Plot Different Graphs using Matplotlib
# Subject: Python Practical – Data Visualization
# Author: <Your Name>
# ---------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# ------------------- Functions -------------------

def line_graph(x, y):
    """Plots a simple Line Graph"""
    plt.plot(x, y, color='blue', marker='o', linestyle='-', label='Line Graph')
    plt.title("Line Graph")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()


def bar_graph(x, y):
    """Plots a Bar Graph"""
    plt.bar(x, y, color='green', label='Bar Graph')
    plt.title("Bar Graph")
    plt.xlabel("Categories / X-axis")
    plt.ylabel("Values / Y-axis")
    plt.legend()
    plt.show()


def scatter_graph(x, y):
    """Plots a Scatter Plot"""
    plt.scatter(x, y, color='red', label='Scatter Plot')
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()


def pie_chart(labels, values):
    """Plots a Pie Chart"""
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title("Pie Chart Example")
    plt.show()


def histogram():
    """Plots a Histogram with random data"""
    data = np.random.randn(1000)       # Generate 1000 random values
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


# ------------------- Main Program -------------------

def main():
    print("=== MULTI-GRAPH PLOTTING USING MATPLOTLIB ===")

    while True:
        print("\nChoose a graph type:")
        print("1. Line Graph")
        print("2. Bar Graph")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice in ['1', '2', '3']:
            n = int(input("Enter number of data points: "))
            x, y = [], []
            for i in range(n):
                xi = float(input(f"Enter X[{i+1}]: "))
                yi = float(input(f"Enter Y[{i+1}]: "))
                x.append(xi)
                y.append(yi)

            if choice == '1':
                line_graph(x, y)
            elif choice == '2':
                bar_graph(x, y)
            elif choice == '3':
                scatter_graph(x, y)

        elif choice == '4':
            n = int(input("Enter number of slices: "))
            labels, values = [], []
            for i in range(n):
                labels.append(input(f"Label {i+1}: "))
                values.append(float(input(f"Value {i+1}: ")))
            pie_chart(labels, values)

        elif choice == '5':
            histogram()

        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()


# pip install matplotlib numpy
# === MULTI-GRAPH PLOTTING USING MATPLOTLIB ===

# Choose a graph type:
# 1. Line Graph
# 2. Bar Graph
# 3. Scatter Plot
# 4. Pie Chart
# 5. Histogram
# 6. Exit
# Enter your choice (1-6): 1
# Enter number of data points: 5
# Enter X[1]: 1
# Enter Y[1]: 2
# Enter X[2]: 2
# Enter Y[2]: 4
# Enter X[3]: 3
# Enter Y[3]: 6
# Enter X[4]: 4
# Enter Y[4]: 8
# Enter X[5]: 5
# Enter Y[5]: 10
