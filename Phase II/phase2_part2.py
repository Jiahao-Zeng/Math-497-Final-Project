import numpy as np
import matplotlib.pyplot as plt

# Given parameters
rho_l = 0.25
v = 0.5
T = 2
i_values = [3, 4, 5, 6, 7, 8]
errors = {}
t_values = [0.2, 0.4, 0.6, 0.8, 1.0]
gamma = 0.75

def compute_numerical_solution(dx, dt, M, N):
    P = np.zeros((N + 1, M + 1))
    P[:, 0] = rho_l  # Boundary condition

    # First step using upwind
    for j in range(1, M + 1):
        P[1, j] = (1 - v) * P[0, j] + v * P[0, j - 1]

    # Subsequent steps using new scheme
    for n in range(1, N):
        for j in range(1, M + 1):
            P[n + 1, j] = (
                (gamma + (1 - v) * (1 - gamma / 2)) * P[n, j]
                - (gamma / 2) * P[n - 1, j]
                + v * (1 - gamma / 2) * P[n, j - 1]
            )
    return P

# Question 2: x = 0.5 over time
dx = (1 / 2) ** 6
dt = 0.8 * dx * ((2 - gamma) / (2 + gamma))
M = int(1 / dx)
N = int(T / dt)

P_q2 = compute_numerical_solution(dx, dt, M, N)

x_index = int(0.5 / dx)
t_exact = np.linspace(0, T, N + 1)
rho_exact = np.array([rho_l if v * t < 0.5 else 0 for t in t_exact])

plt.figure(figsize=(8, 6))
plt.plot(t_exact, P_q2[:, x_index], label='Numerical Solution', linestyle='--', marker='o')
plt.plot(t_exact, rho_exact, label='Exact Solution', linestyle='-', linewidth=2)
plt.xlabel('Time t')
plt.ylabel('Density')
plt.legend()
plt.title('Exact vs Approximated Solution at x=0.5')
plt.grid()
plt.show()

# Question 1: Error table
for i in i_values:
    dx = (1 / 2) ** i
    dt = 0.8 * dx * ((2 - gamma) / (2 + gamma))
    M = int(1 / dx)
    N = int(T / dt)

    P = compute_numerical_solution(dx, dt, M, N)

    error_vals = []
    for t in t_values:
        n_t = int(t / dt)
        rho_exact = np.array([rho_l if x < v * t else 0 for x in np.linspace(0, 1, M + 1)])
        error = dx * np.sum(np.abs(rho_exact - P[n_t, :]))
        error_vals.append(error)

    errors[dx] = error_vals

print("\nError Table:")
print(f"{'Δx':<10}{'t=0.2':<10}{'t=0.4':<10}{'t=0.6':<10}{'t=0.8':<10}{'t=1.0':<10}")
for dx, err in errors.items():
    print(f"{dx:<10.6f}{err[0]:<10.6f}{err[1]:<10.6f}{err[2]:<10.6f}{err[3]:<10.6f}{err[4]:<10.6f}")

# Plotting errors
plt.figure(figsize=(8, 6))
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

# Question 3: Solution at t = 0.5
dx = (1 / 2) ** 6
dt = 0.8 * dx * ((2 - gamma) / (2 + gamma))
M = int(1 / dx)
N = int(T / dt)

P_q3 = compute_numerical_solution(dx, dt, M, N)

t_index = int(0.5 / dt)
x_exact = np.linspace(0, 1, M + 1)
rho_exact = np.array([rho_l if x < v * 0.5 else 0 for x in x_exact])

plt.figure(figsize=(8, 6))
plt.plot(x_exact, P_q3[t_index, :], label='Numerical Solution', linestyle='--', marker='o')
plt.plot(x_exact, rho_exact, label='Exact Solution', linestyle='-', linewidth=2)
plt.xlabel('Position x')
plt.ylabel('Density')
plt.legend()
plt.title('Exact vs Approximated Solution at t=0.5')
plt.grid()
plt.show()

# Question 4: Surface plot
dx = (1 / 2) ** 6
dt = 0.8 * dx * ((2 - gamma) / (2 + gamma))
M = int(1 / dx)
N = int(T / dt)

P_q4 = compute_numerical_solution(dx, dt, M, N)

X, T_vals = np.meshgrid(np.linspace(0, 1, M + 1), np.linspace(0, T, N + 1))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T_vals, P_q4, cmap='viridis')
ax.set_xlabel('Position x')
ax.set_ylabel('Time t')
ax.set_zlabel('Density')
ax.set_title('Approximated Solution Surface')
plt.show()
