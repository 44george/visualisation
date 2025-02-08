import numpy as np
import matplotlib.pyplot as plt

# Data from the chart
months = ["07-2019", "08-2019", "09-2019", "10-2019", "11-2019"]
blue_data = [50, 53, 59, 56, 62]  # First bar group
pink_data = [39, 47, 42, 51, 51]  # Second bar group
yellow_data = [70, 80, 90, 87, 92]  # Third bar group

# Set position for each bar
x = np.arange(len(months))
width = 0.25  # Width of bars

# Create the bar chart
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x - width, blue_data, width, label="Source 1", color='blue')
ax.bar(x, pink_data, width, label="Source 2", color='pink')
ax.bar(x + width, yellow_data, width, label="Source 3", color='orange')

# Labels and Title
ax.set_xlabel("Months")
ax.set_ylabel("Visitors (in thousands)")
ax.set_title("Visitors by Web Traffic Sources")
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Show plot
plt.show()
