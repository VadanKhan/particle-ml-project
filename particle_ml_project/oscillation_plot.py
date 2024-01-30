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

# Plots for different mixing angles
mixing_angle_consts = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi])
mixing_plots = []
for mixing_angle in mixing_angle_consts:
    plot_set = equation(L_values, mixing_angle)
    np.append(mixing_plots, plot_set)
  
# Final Plotting
colours_mixing = ['blue', 'green', 'red', 'orange', 'magenta']
style_mixing = ['solid', 'solid', 'solid', 'dashed', 'dashed']
labels_mixing = [r'theta = 0', r'theta = $\pi/6$', r'theta = $\pi/4$', r'theta = $\pi/3$', r'theta = $pi$']

for i, plot in enumerate(mixing_plots):
    plt.plot(L_values, plot, label=labels_mixing[i], color=colours_mixing[i], linestyle=style_mixing[i])

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
