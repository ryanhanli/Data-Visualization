import matplotlib.pyplot as plt

# Part 2 x_values = [1, 2, 3, 4, 5]
# Part 2 y_values = [1, 4, 9, 16, 25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Part 1 ax.scatter(2,4, s=200) # s sets size of dot
# Part 2 ax.scatter(x_values, y_values, s=100)
# Part 3 ax.scatter(x_values, y_values, c='red', s=10) #You can use string or rgb tuple ranging from 0-1 where 1 is lightest for ex. c=(0, 0.8, 0)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # Colormap example.  We pass list of y-values to c and then tell pyplot which colormap to use
# using the cmap argument.  This cmap colors higher y-values dark blue.

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0,1100,0,1100000])

# If you want to save the plot instead of show it just run this
# plt.savefig('squares_plot.png', bbox_inches='tight')
# Saves to same directory as this file and second argument trims extra white space
plt.show()
