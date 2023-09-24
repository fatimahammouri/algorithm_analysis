# Code for plotting Graph for Algorithms time complexity
# Code skeleton was generated using ChatGPT

import matplotlib.pyplot as plt

# Data for four algorithms (replace with your own data)
tree_traversal_algorithm = [(100000, 0.00941), (200000, 0.0189), (300000, 0.0296), (400000, 0.03969),
                            (500000, 0.04727), (600000, 0.0613), (700000, 0.0661), (800000, 0.0778),
                            (900000, 0.0870), (1000000, 0.0931), (1100000, 0.1063), (1200000, 0.1142),
                            (1300000, 0.1281), (1400000, 0.1348), (1500000, 0.1430),
                            (2000000, 0.1890), (3000000, 0.2804), (4000000, 0.3772),
                            (5000000, 0.4639), (6000000, 0.5962), (7000000, 0.6640),
                            (10000000, 1.2204)]

merge_sort_algorithm = [(100000, 0.1973), (200000, 0.4187), (300000, 0.6450), (400000, 0.9012),
                        (500000, 1.1242), (600000, 1.3947), (700000, 1.6966), (800000, 1.9003),
                        (900000, 2.2844), (1000000, 2.4694), (1100000, 2.7563), (1200000, 3.0379),
                        (1300000, 3.3428), (1400000, 3.6092), (1500000, 3.7791),
                        (2000000, 5.2178), (3000000, 8.2542), (4000000, 11.1543),
                        (5000000, 14.5292), (6000000, 17.5289), (7000000, 23.075),
                        (10000000, 39.0859)]

binary_search_algorithm = [(100000, 0.000005578), (200000, 0.000005602), (300000, 0.000005698), (400000, 0.000006818),
                        (500000, 0.000007687), (600000, 0.00001406), (700000, 0.000009775), (800000, 0.00001001),
                        (900000, 0.000009059), (1000000, 0.00001001), (1100000, 0.0000090599), (1200000, 0.000009775),
                        (1300000, 0.000008106), (1400000, 0.0000090599), (1500000, 0.000008344),
                        (2000000, 0.000008106), (3000000, 0.000009060), (4000000, 0.00001001),
                        (5000000, 0.00001002), (6000000, 0.00001096), (7000000, 0.000008822),
                        (10000000, 0.00001121)]

brute_force_algorithm = [(100000, 0.3140), (200000, 0.6238), (300000, 0.9554), (400000, 1.3038),
                        (500000, 1.5838), (600000, 1.8739), (700000, 2.2327), (800000, 2.5438),
                        (900000, 2.8467), (1000000, 3.0996), (1100000, 3.6207), (1200000, 3.6889),
                        (1300000, 4.0793), (1400000, 4.3897), (1500000, 4.8010),
                        (2000000, 6.2720), (3000000, 9.2238), (4000000, 12.7585),
                        (5000000, 15.7855), (6000000, 18.9591), (7000000, 21.6395),
                        (10000000, 42.4421)]

# Extract x and y values for each algorithm
x_values = [point[0] for point in tree_traversal_algorithm]
y_tree_traversal_algorithm = [point[1] for point in tree_traversal_algorithm]
y_merge_sort_algorithm = [point[1] for point in merge_sort_algorithm]
y_binary_search_algorithm = [point[1] for point in binary_search_algorithm]
y_brute_force_algorithm = [point[1] for point in brute_force_algorithm]

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(x_values, y_tree_traversal_algorithm, label='Tree Traversal Algorithm')
plt.plot(x_values, y_merge_sort_algorithm, label='Merge Sort Algorithm')
plt.plot(x_values, y_binary_search_algorithm, label='Binary Search Algorithm ')
plt.plot(x_values, y_brute_force_algorithm, label='Brute Force Algorithm')

# Add labels and a legend
plt.xlabel('Number of Data Points')
plt.ylabel('Runtime (seconds)')
plt.title('Algorithm Runtimes vs. Number of Data Points')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
