import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

# import pandas

# Define the equation


def equation(L, mixing_angle, delta_mass, energy):

    # Energy of neutrino in GeV
    # Difference in the squares of reset mass energies of neutrino mass states in (eV)^2
    return (np.sin(2*mixing_angle)**2)*(np.sin(1.27*delta_mass**2*L/energy)**2)**2


# Generate x values
L_values = np.linspace(0, 10, 500)  # Generate 100 points from -10 to 10

# Plots for different mixing angles
mixing_angle_consts = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi])
colours_mixing = ['blue', 'green', 'red', 'orange', 'magenta']
style_mixing = ['solid', 'solid', 'solid', 'dashed', 'dashed']
labels_mixing = [r'$\theta$ = 0', r'$\theta$ = $\pi/6$',
                 r'$\theta$ = $\pi/4$', r'$\theta$ = $\pi/3$', r'$\theta$ = $\pi$']
mixing_plots = []
for mixing_angle in mixing_angle_consts:
    plot_set = equation(L_values, mixing_angle, 1, 1)
    mixing_plots.append(plot_set)

# Plots for different difference in mass
delta_mass_consts = np.array([0, 1, 1.414, 1.616, 1.95])
colours_mass = ['blue', 'green', 'red', 'orange', 'magenta']
style_mass = ['solid', 'solid', 'solid', 'solid', 'solid']
labels_mass = [r'$\Delta m_{12}$ = 0', r'$\Delta m_{12}$ = 1',
               r'$\Delta m_{12}$ = 2', r'$\Delta m_{12}$ = 3', r'$\Delta m_{12}$ = 4']
mass_plots = []
for mass_diff in delta_mass_consts:
    plot_set = equation(L_values, np.pi/4, mass_diff, 1)
    mass_plots.append(plot_set)

# Plots for different different neutrino energies
energy_consts = np.array([1, 2, 3, 4])
colours_energy = ['blue', 'green', 'red', 'orange']
style_energy = ['solid', 'solid', 'solid', 'solid']
labels_energy = [r'$E$ = 1', r'$E$ = 2', r'$E$ = 3', r'$E$ = 4']
energy_plots = []
for energy in energy_consts:
    plot_set = equation(L_values, np.pi/4, 1, energy)
    energy_plots.append(plot_set)

# Final Plotting
fig, axs = plt.subplots(3, figsize=(10, 15))

# Mixing angles plot
for i, plot in enumerate(mixing_plots):
    axs[0].plot(L_values, plot, label=labels_mixing[i],
                color=colours_mixing[i], linestyle=style_mixing[i])
axs[0].set_xlabel('L (km)')
axs[0].set_ylabel('Probability of Oscillation')
axs[0].set_title('Probability of neutrino flavour oscillation for different mixing angles')
axs[0].legend()

# Mass difference plot
for i, plot in enumerate(mass_plots):
    axs[1].plot(L_values, plot, label=labels_mass[i],
                color=colours_mass[i], linestyle=style_mass[i])
axs[1].set_xlabel('L (km)')
axs[1].set_ylabel('Probability of Oscillation')
axs[1].set_title('Probability of neutrino flavour oscillation for different mass differences')
axs[1].legend()

# Neutrino energies plot
for i, plot in enumerate(energy_plots):
    axs[2].plot(L_values, plot, label=labels_energy[i],
                color=colours_energy[i], linestyle=style_energy[i])
axs[2].set_xlabel('L (km)')
axs[2].set_ylabel('Probability of Oscillation')
axs[2].set_title('Probability of neutrino flavour oscillation for different neutrino energies')
axs[2].legend()

# Saving the plot
dir_path = os.path.join(Path(__file__).parent, "Figures")
file_path = os.path.join(dir_path, "prob_neutrinostate_oscillation.png")
os.makedirs(dir_path, exist_ok=True)
plt.savefig(file_path)

# Show the plot
plt.show()
