import numpy as np
import matplotlib.pyplot as plt

# Given parameters
rho_l = 0.75 # Changed to 0.75 for Question 6
v = 0.5
T = 2  # Final time
i_values = [3, 4, 5, 6, 7, 8]
errors = {}
t_values = [0.2, 0.4, 0.6, 0.8, 1.0]

# Question 2: Compute and plot the exact and numerical solution at x = 0.5
dx = (1/2)**6  # Given dx for part 2
dt = 0.8 * dx  # Given dt condition
M = int(1/dx)  # Number of spatial points
N = int(T/dt)  # Number of time steps

P = np.zeros((N+1, M+1))  # Initialize P array
P[:, 0] = rho_l  # Boundary condition

for n in range(N):
    for j in range(1, M+1):
        P[n+1, j] = (1-v) * P[n, j] + v * P[n, j-1]

# Extract solution at x = 0.5
x_index = int(0.5 / dx)
t_exact = np.linspace(0, 1, N+1)
rho_exact = np.array([rho_l if v*t < 0.5 else 0 for t in t_exact])

plt.figure(figsize=(8,6))
plt.plot(t_exact, P[:, x_index], label='Numerical Solution', linestyle='--', marker='o')
plt.plot(t_exact, rho_exact, label='Exact Solution', linestyle='-', linewidth=2)
plt.xlabel('Time t')
plt.ylabel('Density')
plt.legend()
plt.title('Exact vs Approximated Solution at x=0.5')
plt.grid()
plt.show()

# Question 1: Compute the error for different dx values
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

# Question 3: Compute and plot the exact and numerical solution at t = 0.5
dx = (1/2)**6  # Given dx for part 3
dt = 0.8 * dx  # Given dt condition
M = int(1/dx)  # Number of spatial points
N = int(T/dt)  # Number of time steps

P = np.zeros((N+1, M+1))  # Initialize P array
P[:, 0] = rho_l  # Boundary condition

for n in range(N):
    for j in range(1, M+1):
        P[n+1, j] = (1-v) * P[n, j] + v * P[n, j-1]

# Extract solution at t = 0.5
t_index = int(0.5 / dt)
x_exact = np.linspace(0, 1, M+1)
rho_exact = np.array([rho_l if x < v*0.5 else 0 for x in x_exact])

plt.figure(figsize=(8,6))
plt.plot(x_exact, P[t_index, :], label='Numerical Solution', linestyle='--', marker='o')
plt.plot(x_exact, rho_exact, label='Exact Solution', linestyle='-', linewidth=2)
plt.xlabel('Position x')
plt.ylabel('Density')
plt.legend()
plt.title('Exact vs Approximated Solution at t=0.5')
plt.grid()
plt.show()

# Question 4: Plot the exact solution and approximated solution surfaces
dx = (1/2)**6  # Given dx for part 4
dt = 0.8 * dx  # Given dt condition
M = int(1/dx)  # Number of spatial points
N = int(T/dt)  # Number of time steps

P = np.zeros((N+1, M+1))  # Initialize P array
P[:, 0] = rho_l  # Boundary condition

for n in range(N):
    for j in range(1, M+1):
        P[n+1, j] = (1-v) * P[n, j] + v * P[n, j-1]

X, T_vals = np.meshgrid(np.linspace(0, 1, M+1), np.linspace(0, T, N+1))

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T_vals, P, cmap='viridis')
ax.set_xlabel('Position x')
ax.set_ylabel('Time t')
ax.set_zlabel('Density')
ax.set_title('Approximated Solution Surface')
plt.show()
