import numpy as np
import matplotlib.pyplot as plt

# Given parameters
rho_l = 0.5
v = 0.5  # Given in the problem
T = 2  # Final time
i_values = [3, 4, 5, 6, 7, 8]
errors = {}
t_values = [0.2, 0.4, 0.6, 0.8, 1.0]

for i in i_values:
    dx = (1/2)**i
    dt = 0.8 * dx  # Given dt condition
    M = int(1/dx)  # Number of spatial points
    N = int(T/dt)  # Number of time steps
    
    P = np.zeros((N+1, M+1))  # Initialize P array
    P[:, 0] = rho_l  # Boundary condition
    
    for n in range(N):
        for j in range(1, M+1):
            P[n+1, j] = (1-v) * P[n, j] + v * P[n, j-1]
    
    error_vals = []
    for t in t_values:
        n_t = int(t/dt)
        rho_exact = np.array([rho_l if x < v*t else 0 for x in np.linspace(0, 1, M+1)])
        error = dx * np.sum(np.abs(rho_exact - P[n_t, :]))
        error_vals.append(error)
    
    errors[dx] = error_vals

# Print error table
print("\nError Table:")
print(f"{'Δx':<10}{'t=0.2':<10}{'t=0.4':<10}{'t=0.6':<10}{'t=0.8':<10}{'t=1.0':<10}")
for dx, err in errors.items():
    print(f"{dx:<10.6f}{err[0]:<10.6f}{err[1]:<10.6f}{err[2]:<10.6f}{err[3]:<10.6f}{err[4]:<10.6f}")

# Plot errors for t = 0.4 and t = 1 against different dx values
plt.figure(figsize=(8,6))
for idx, t in enumerate(t_values):
    plt.plot(errors.keys(), [err[idx] for err in errors.values()], marker='o', label=f't={t}')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$\Delta x$')
plt.ylabel('Error')
plt.legend()
plt.title('Error vs $\Delta x$ for different t values')
plt.grid()
plt.show()
