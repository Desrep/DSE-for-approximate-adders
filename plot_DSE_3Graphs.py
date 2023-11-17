import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the log file
with open('design_space_exploration.txt', 'r') as file:
    log_content = file.read()

# Extract data using regular expressions
pattern = re.compile(r"approximate bits\n\[(\d+\.\d+), (\d+\.\d+)\]")
matches = pattern.findall(log_content)

# Convert data to numpy array
data = np.array([list(map(float, match)) for match in matches])

# Create a single figure with subplots
fig = plt.figure(figsize=(14, 6))

# Precision vs Area delay
ax1 = fig.add_subplot(111)
ax1.scatter(data[:, 0], data[:, 1], c='green', marker='o')
ax1.set_xlabel('Area*delay')
ax1.set_ylabel('Approximate Adder Precision')
ax1.set_title('Precision vs area*delay')


# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


