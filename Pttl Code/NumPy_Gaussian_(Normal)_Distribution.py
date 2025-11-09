# ---------------------------------------------------------
# Program: Generate Random Numbers for Gaussian Distribution using NumPy
# Subject: Python Practical – NumPy
# Author: <Your Name>
# ---------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ------------------- User Defined Function -------------------
def generate_gaussian(mean, std_dev, num_samples):
    """
    Generates random numbers following a Gaussian (Normal) distribution.
    """
    numbers = np.random.normal(mean, std_dev, num_samples)
    return numbers


# ------------------- Main Program -------------------
def main():
    print("=== GAUSSIAN RANDOM NUMBER GENERATOR ===")

    mean = float(input("Enter mean (μ): "))
    std_dev = float(input("Enter standard deviation (σ): "))
    num_samples = int(input("Enter number of samples to generate: "))

    # Call user-defined function
    gaussian_numbers = generate_gaussian(mean, std_dev, num_samples)

    print("\nFirst 10 Gaussian random numbers:")
    print(gaussian_numbers[:10])

    # Optional: visualize data
    choice = input("\nDo you want to see a histogram? (yes/no): ").lower()
    if choice == 'yes':
        plt.hist(gaussian_numbers, bins=30, color='skyblue', edgecolor='black')
        plt.title("Histogram of Gaussian Random Numbers")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()


# ------------------- Entry Point -------------------
if __name__ == "__main__":
    main()


# pip install numpy matplotlib
# python assignment5_numpy.py

# output:
# === GAUSSIAN RANDOM NUMBER GENERATOR ===
# Enter mean (μ): 0
# Enter standard deviation (σ): 1
# Enter number of samples to generate: 1000
# First 10 Gaussian random numbers:
# [ 0.16 -0.52  0.44 ...]
