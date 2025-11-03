import numpy as np

# Take user input for parameters
mean = float(input("Enter the mean (mu): "))
std_dev = float(input("Enter the standard deviation (sigma): "))
size = int(input("Enter how many random numbers to generate: "))

# Generate random numbers using Gaussian (Normal) distribution
random_numbers = np.random.normal(mean, std_dev, size)

# Display the generated numbers
print("\n🎲 Generated Gaussian Random Numbers:")
print(random_numbers)

# Optional: Show summary statistics
print("\n📊 Summary:")
print(f"Mean of generated numbers: {np.mean(random_numbers):.2f}")
print(f"Standard deviation: {np.std(random_numbers):.2f}")
