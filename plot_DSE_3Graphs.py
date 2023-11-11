import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the log file
with open('design_space_exploration.txt', 'r') as file:
    log_content = file.read()

# Extract data using regular expressions
pattern = re.compile(r"approximate bits\n\[(\d+\.\d+), (\d+\.\d+), (\d+\.\d+)\]")
matches = pattern.findall(log_content)

# Convert data to numpy array
data = np.array([list(map(float, match)) for match in matches])

# Create a single figure with subplots
fig = plt.figure(figsize=(18, 6))

# 3D Plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(data[:, 1], data[:, 0], data[:, 2], c='blue', marker='o')
ax1.set_xlabel('Delay')
ax1.set_ylabel('Area')
ax1.set_zlabel('Approximate Adder Precision')
ax1.set_title('3D Plot')

# Precision vs Area
ax2 = fig.add_subplot(132)
ax2.scatter(data[:, 0], data[:, 2], c='green', marker='o')
ax2.set_xlabel('Area')
ax2.set_ylabel('Approximate Adder Precision')
ax2.set_title('Precision vs Area')

# Precision vs Parasitic Loss
ax3 = fig.add_subplot(133)
ax3.scatter(data[:, 1], data[:, 2], c='red', marker='o')
ax3.set_xlabel('Delay')
ax3.set_ylabel('Approximate Adder Precision')
ax3.set_title('Precision vs Delay')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


