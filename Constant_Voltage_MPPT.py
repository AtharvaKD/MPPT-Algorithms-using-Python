#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# Constants
V_REF = 36.0      # Reference voltage (V)
DELTA_D = 0.02    # Step size for duty cycle change
D = 0.5           # Initial duty cycle

# Simulation parameters
time_steps = 100
V_PV = np.full(time_steps, 34.0)  # Initialize PV voltage

# Store duty cycle values for plotting
D_values = []

# MPPT Algorithm
for t in range(time_steps):
    if V_PV[t] < V_REF:
        D = min(D + DELTA_D, 1.0)  # Increase duty cycle
    elif V_PV[t] > V_REF:
        D = max(D - DELTA_D, 0.0)  # Decrease duty cycle

    D_values.append(D)   #It stores the current duty cycle 𝐷 at each time step in the D_values list.This is useful for plotting the duty cycle variation over time.
    V_PV[t] = V_REF + np.random.uniform(-1, 1)  # Simulated voltage variation
    
#It simulates real-world variations in the PV voltage
#Instead of keeping Vpv constant, it adds a small random fluctuation (np.random.uniform(-1, 1)).
#np.random.uniform(-1, 1) generates a random number between -1V and +1V.

# Plot Results
plt.plot(D_values, label="Duty Cycle (D)", color='g')
plt.axhline(y=V_REF, color='r', linestyle='--', label="V_REF (36V)")
plt.xlabel("Time Step")
plt.ylabel("Duty Cycle")
plt.legend()
plt.title("Constant Voltage MPPT Simulation")
plt.show()


