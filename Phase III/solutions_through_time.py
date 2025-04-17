import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

# Parameters
rho_l = 0.5
v = 0.5
T = 2
gamma_values = [0, 1.75]
dx = 1 / 2**7
dt_dict = {}
P_dict = {}

# Grid setup
x = np.linspace(0, 1, int(1/dx) + 1)
M = len(x) - 1

# Compute solutions
for gamma in gamma_values:
    dt = 0.8 * dx * ((2 - gamma) / (2 + gamma)) if gamma != 0 else 0.8 * dx
    N = int(T / dt)
    dt_dict[gamma] = dt

    P = np.zeros((N+1, M+1))
    P[:, 0] = rho_l

    # Initial step
    for j in range(1, M+1):
        P[1, j] = (1 - v*dt/dx) * P[0, j] + (v*dt/dx) * P[0, j-1]

    # Time stepping
    for n in range(1, N):
        for j in range(1, M+1):
            P[n+1, j] = (
                (gamma + (1 - v*dt/dx) * (1 - gamma / 2)) * P[n, j]
                - (gamma / 2) * P[n-1, j]
                + (v*dt/dx) * (1 - gamma / 2) * P[n, j-1]
            )
    P_dict[gamma] = P

# --- GIF Setup ---
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)
filenames = []

# Frame generation
for n in range(0, min(len(P_dict[0]), len(P_dict[1.75])), 5):  # every 5th frame
    t = n * dt_dict[0]
    exact = np.array([rho_l if x_val < v*t else 0 for x_val in x])

    plt.figure(figsize=(8, 6))
    plt.plot(x, exact, label='Exact', linewidth=2)
    plt.plot(x, P_dict[0][n], '--', label='Gamma=0')
    plt.plot(x, P_dict[1.75][n], '--', label='Gamma=1.75')
    plt.title(f'Time = {t:.2f}')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.legend()
    plt.grid()
    filename = f"{output_folder}/frame_{n:04d}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# --- Create GIF ---
gif_filename = "advection_evolution.gif"
with imageio.get_writer(gif_filename, mode='I', duration=0.1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up
for filename in filenames:
    os.remove(filename)

print(f"GIF saved as '{gif_filename}'")
