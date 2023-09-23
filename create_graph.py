# Code for plotting Graph of time complexity
# for the four tested algorithms
# Credit: ChatGPT
import matplotlib.pyplot as plt

# Data for four algorithms (replace with your own data)
algorithm1_data = [(100, 0.5), (200, 1.0), (300, 1.5), (400, 2.0)]
algorithm2_data = [(100, 0.3), (200, 0.8), (300, 1.2), (400, 1.7)]
algorithm3_data = [(100000, 0.7), (200000, 1.3), (300000, 2.0), (400000, 2.8)]
algorithm4_data = [(100000, 0.4), (200000, 0.9), (300000, 1.4), (400000, 2.2)]

# Extract x and y values for each algorithm
x_values = [point[0] for point in algorithm1_data]
y_algorithm1 = [point[1] for point in algorithm1_data]
y_algorithm2 = [point[1] for point in algorithm2_data]
y_algorithm3 = [point[1] for point in algorithm3_data]
y_algorithm4 = [point[1] for point in algorithm4_data]

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(x_values, y_algorithm1, label='Algorithm 1')
plt.plot(x_values, y_algorithm2, label='Algorithm 2')
plt.plot(x_values, y_algorithm3, label='Algorithm 3')
plt.plot(x_values, y_algorithm4, label='Algorithm 4')

# Add labels and a legend
plt.xlabel('Number of Data Points')
plt.ylabel('Runtime (seconds)')
plt.title('Algorithm Runtimes vs. Number of Data Points')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
