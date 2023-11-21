import numpy as np
import matplotlib.pyplot as plt

def process_file(file_path, color):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        # Skip lines starting with '0b'
        if line.startswith('0b'):
            continue

        # Split the line into values
        values = list(map(float, line.strip('[]\n').split(', ')))
        data.append(values)

    # Convert data to numpy array
    data = np.array(data)

    # Precision vs Delay * Area
    if data.shape[1] == 3:
        product_of_loss_area = data[:, 0] * data[:, 1]
        plt.scatter(product_of_loss_area, data[:, 2], c=color, marker='o', label=file_path)
    elif data.shape[1] == 2:
        plt.scatter(data[:, 0], data[:, 1], c=color, marker='o', label=file_path)

# Create a single figure
fig, ax = plt.subplots(figsize=(10, 6))

# Process and plot the first file (design_space_exploration.txt) in light gray
process_file('design_space_exploration.txt', color='lightgray')

# Process and plot the second file (Algo_Data.txt) in bright red, skipping lines starting with '0b'
process_file('EDA_Algo_DSE.txt', color='red')

# Set labels and title
ax.set_xlabel('Delay * Area')
ax.set_ylabel('Approximate Adder Precision')
ax.set_title('Precision vs Delay * Area')

# Add a legend
ax.legend()

# Show the plot
plt.show()

