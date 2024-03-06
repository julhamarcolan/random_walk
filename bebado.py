"""
Random Walk Simulation of Drunkards

Author: Julia Marcolan

This script simulates random walks for a specified number of drunkards over a specified number of steps.
Each drunkard randomly decides whether to step left or right at each iteration.

Parameters:
- NB: Number of drunkards in the simulation.
- N: Number of steps each drunkard takes.
- L: Size of each drunkard's step.
- x: List to store the final distances traveled by each drunkard.

The script iterates over each drunkard, calculates the final distances from the starting point, and displays a histogram of the final distances.

"""

import matplotlib.pyplot as plt
import numpy as np

# Parameters
NB = 100000  # Number of drunkards
N = 5000     # Number of steps each drunkard takes
L = 1        # Size of each drunkard's step
x = []       # List to store the final distances

# Loop for each drunkard in the simulation
for _ in range(NB):
    # Generate N random steps to the left (-1) or right (1) using numpy
    steps = np.random.choice([-1, 1], N)
    
    # Calculate the final distance traveled by the drunkard by summing all steps and multiplying by the step size (L)
    final_distance = np.sum(steps) * L
    
    # Append the calculated final distance to the list x, which will store the final distances of all drunkards
    x.append(final_distance)

# Display the histogram of final distances
plt.hist(x, bins=1000, color='blue', alpha=0.7)
plt.xlabel('Final Distance')
plt.ylabel('Frequency')
plt.title('Histogram of Random Walk Simulation for Drunkards')
plt.grid(True)
plt.show()
