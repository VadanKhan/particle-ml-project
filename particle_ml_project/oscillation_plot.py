import numpy as np
import matplotlib.pyplot as plt

# Define the equation
def equation(L, theta):
    return (np.sin(2*theta)**2)*(np.sin(L)**2)**2

# Generate x values
x_values = np.linspace(0, np.pi, 100)  # Generate 100 points from -10 to 10

# Evaluate the equation for y values
y_values1 = equation(x_values, np.pi/6)
y_values2 = equation(x_values, np.pi/4)
y_values3 = equation(x_values, np.pi/3)

# Plot the equation
plt.plot(x_values, y_values1, label='theta = 0', color = 'blue')
plt.plot(x_values, y_values2, label='theta = pi/4', color = 'green')
plt.plot(x_values, y_values3, label='theta = pi/2', color = 'red')

# Add labels and title
plt.xlabel('L')
plt.ylabel('probability of oscillation')
plt.title('Plot')

# Add a legend
plt.legend()

# Show the plot
plt.show()

