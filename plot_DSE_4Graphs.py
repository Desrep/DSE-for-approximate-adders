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
fig = plt.figure(figsize=(18, 10))

# 3D Plot
ax1 = fig.add_subplot(221, projection='3d')
ax1.scatter(data[:, 1], data[:, 0], data[:, 2], c='blue', marker='o')
ax1.set_xlabel('Delay')
ax1.set_ylabel('Area')
ax1.set_zlabel('Adder Precision')
ax1.set_title('3D Plot')

# Precision vs Area
ax2 = fig.add_subplot(222)
ax2.scatter(data[:, 0], data[:, 2], c='green', marker='o')
ax2.set_xlabel('Area')
ax2.set_ylabel('Adder Precision')
ax2.set_title('Precision vs Area')

# Precision vs Parasitic Loss
ax3 = fig.add_subplot(223)
ax3.scatter(data[:, 1], data[:, 2], c='red', marker='o')
ax3.set_xlabel('Parasitic Loss')
ax3.set_ylabel('Adder Precision')
ax3.set_title('Precision vs Delay')

# Precision vs Parasitic Loss * Area
ax4 = fig.add_subplot(224)
product_of_loss_area = data[:, 0] * data[:, 1]
ax4.scatter(product_of_loss_area, data[:, 2], c='purple', marker='o')
ax4.set_xlabel('Parasitic Loss * Area')
ax4.set_ylabel('Adder Precision')
ax4.set_title('Precision vs Delay x Area')


# Adjust layout
plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)  # Adjust these values to fit your needs

# Show the plots
plt.show()

