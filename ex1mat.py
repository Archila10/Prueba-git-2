import matplotlib.pyplot as plt

# Data to pyplot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot data 
ax.plot(x, y)

# Add title and labels
ax.set_title('Simple Line Plot')
ax.set_xlabel('x value')
ax.set_ylabel('y values')

# Display the plot
plt.show()