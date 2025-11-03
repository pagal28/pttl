import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]
y3 = [10, 8, 6, 4, 2]

# 1️⃣ Line Graph
plt.figure(figsize=(7, 4))
plt.plot(x, y1, color='blue', marker='o', label='y = 2x')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 2️⃣ Bar Graph
plt.figure(figsize=(7, 4))
plt.bar(x, y2, color='orange')
plt.title("Bar Graph Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 3️⃣ Scatter Plot
plt.figure(figsize=(7, 4))
plt.scatter(x, y3, color='green', marker='x')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
