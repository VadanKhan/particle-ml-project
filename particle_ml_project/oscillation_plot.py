import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

# Define the equation
def equation(L, mixing_angle):
    energy = 1 #Energy of neutrino in GeV
    delta_mass_squared = 1 #Difference in the squares of reset mass energies of neutrino mass states in (eV)^2
    return (np.sin(2*mixing_angle)**2)*(np.sin(1.27*delta_mass_squared**2*L/energy)**2)**2

# Generate x values
L_values = np.linspace(0, 10, 500)  # Generate 100 points from -10 to 10

# Evaluate the equation for y values
P_values1 = equation(L_values, 0)
P_values2 = equation(L_values, np.pi/6)
P_values3 = equation(L_values, np.pi/4)
P_values4 = equation(L_values, np.pi/3)
P_values5 = equation(L_values, np.pi)

# Plot the equation
plt.plot(L_values, P_values1, label= r'theta = 0', color = 'blue')
plt.plot(L_values, P_values2, label= r'theta = $\pi/6$', color = 'green')
plt.plot(L_values, P_values3, label= r'theta = $\pi/4$', color = 'red')
plt.plot(L_values, P_values4, label= r'theta = $\pi/3$', color = 'orange', linestyle = 'dashed')
plt.plot(L_values, P_values5, label= r'theta = $pi$', color = 'magenta', linestyle = 'dashed')


# Add labels and title
plt.xlabel('L (km)')
plt.ylabel('Probability of Oscillation')
plt.title('Probability of neutrino flavour oscillation in the two-flavour approximation')

# Add a legend
plt.legend()

# Saving the plot
dir_path = os.path.join(Path(__file__).parent, "Figures")
file_path = os.path.join(dir_path, "prob_neutrinostate_oscillation.png")
os.makedirs(dir_path, exist_ok=True)
plt.savefig(file_path)

# Show the plot
plt.show()
