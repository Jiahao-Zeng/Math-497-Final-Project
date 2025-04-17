import numpy as np
import matplotlib.pyplot as plt

# Parameters
rho_l = 0.5
v = 0.5
T = 2
i_values = [4, 5, 6, 7, 8]
t_values = [0.2, 0.4]
x_target = 0.5
gamma_values = [0, 1.75]

# Question 1: Error vs dx at t = 0.4 for gamma = 0 and 1.75
error_results = {}
for gamma in gamma_values:
    error_results[gamma] = {}
    for i in i_values:
        dx = (1/2)**i
        dt = 0.8 * dx * ((2 - gamma) / (2 + gamma)) if gamma != 0 else 0.8 * dx
        nu = v * dt / dx
        M = int(1/dx)
        N = int(T/dt)

        P = np.zeros((N+1, M+1))
        P[:, 0] = rho_l

        for j in range(1, M+1):
            P[1, j] = (1 - nu) * P[0, j] + nu * P[0, j-1]

        for n in range(1, N):
            for j in range(1, M+1):
                P[n+1, j] = (
                    (gamma + (1 - nu) * (1 - gamma / 2)) * P[n, j]
                    - (gamma / 2) * P[n-1, j]
                    + nu * (1 - gamma / 2) * P[n, j-1]
                )

        for t in t_values:
            n_t = int(t / dt)
            rho_exact = np.array([rho_l if x < v*t else 0 for x in np.linspace(0, 1, M+1)])
            error = dx * np.sum(np.abs(rho_exact - P[n_t, :]))
            error_results[gamma].setdefault(t, []).append((dx, error))

# Plotting error at t = 0.4
plt.figure(figsize=(8,6))
for gamma in gamma_values:
    dx_vals, error_vals = zip(*error_results[gamma][0.4])
    plt.plot(dx_vals, error_vals, marker='o', label=f'gamma={gamma}')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$\Delta x$')
plt.ylabel('Error at t=0.4')
plt.title('Error vs $\Delta x$ for different gamma values')
plt.legend()
plt.grid()
plt.show()

# Question 2: Plot at x=0.5 for gamma=0 and gamma=1.75, dx=1/2^6
plt.figure(figsize=(8,6))
x_index = int(0.5 / ((1/2)**6))
for gamma in gamma_values:
    dx = (1/2)**6
    dt = 0.8 * dx * ((2 - gamma) / (2 + gamma)) if gamma != 0 else 0.8 * dx
    nu = v * dt / dx
    M = int(1/dx)
    N = int(T/dt)

    P = np.zeros((N+1, M+1))
    P[:, 0] = rho_l
    for j in range(1, M+1):
        P[1, j] = (1 - nu) * P[0, j] + nu * P[0, j-1]
    for n in range(1, N):
        for j in range(1, M+1):
            P[n+1, j] = (
                (gamma + (1 - nu) * (1 - gamma / 2)) * P[n, j]
                - (gamma / 2) * P[n-1, j]
                + nu * (1 - gamma / 2) * P[n, j-1]
            )

    t_exact = np.linspace(0, T, N+1)
    rho_exact = np.array([rho_l if v*t < 0.5 else 0 for t in t_exact])
    plt.plot(t_exact, P[:, x_index], '--', marker='o', label=f'gamma={gamma}')
plt.plot(t_exact, rho_exact, label='Exact', linewidth=2)
plt.xlabel('Time t')
plt.ylabel('Density at x=0.5')
plt.legend()
plt.title('Exact vs Approx. Solutions at x=0.5')
plt.grid()
plt.show()

# Question 3: Plot at t = 0.4 over 0 <= x <= 1
dx = (1/2)**6
gamma = 1.75
dt = 0.8 * dx * ((2 - gamma) / (2 + gamma))
nu = v * dt / dx
M = int(1/dx)
N = int(T/dt)

P = np.zeros((N+1, M+1))
P[:, 0] = rho_l
for j in range(1, M+1):
    P[1, j] = (1 - nu) * P[0, j] + nu * P[0, j-1]
for n in range(1, N):
    for j in range(1, M+1):
        P[n+1, j] = (
            (gamma + (1 - nu) * (1 - gamma / 2)) * P[n, j]
            - (gamma / 2) * P[n-1, j]
            + nu * (1 - gamma / 2) * P[n, j-1]
        )

x_vals = np.linspace(0, 1, M+1)
t_index = int(0.4 / dt)
rho_exact = np.array([rho_l if x < v*0.4 else 0 for x in x_vals])

plt.figure(figsize=(8,6))
plt.plot(x_vals, P[t_index, :], '--', marker='o', label='Numerical')
plt.plot(x_vals, rho_exact, label='Exact', linewidth=2)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Exact vs Approx Solution at t=0.4')
plt.legend()
plt.grid()
plt.show()

# Question 5: Periodic initial/boundary, sin(2πx) init, gamma = 0 and 1.75, dx=1/2^8
x_points = 2**8
x = np.linspace(0, 1, x_points + 1)
times_to_plot = [2*T, 5*T, 10*T]

for gamma in gamma_values:
    dx = 1 / x_points
    dt = 0.8 * dx * ((2 - gamma) / (2 + gamma)) if gamma != 0 else 0.8 * dx
    nu = v * dt / dx
    N = int(10 * T / dt)
    M = x_points

    P = np.zeros((N+1, M+1))
    P[0, :] = np.sin(2 * np.pi * x)

    def get_p(n, j):
        return P[n, j % (M+1)]

    for j in range(M+1):
        P[1, j] = (1 - nu) * get_p(0, j) + nu * get_p(0, j-1)

    for n in range(1, N):
        for j in range(M+1):
            P[n+1, j] = (
                (gamma + (1 - nu) * (1 - gamma / 2)) * get_p(n, j)
                - (gamma / 2) * get_p(n-1, j)
                + nu * (1 - gamma / 2) * get_p(n, j-1)
            )

    plt.figure(figsize=(12, 8))
    for t_val in times_to_plot:
        n = int(t_val / dt)
        plt.plot(x, P[n, :], '--', label=f'Approx gamma={gamma}, t={t_val}')
    plt.plot(x, np.sin(2 * np.pi * x), label='Exact', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.title(f'Periodic IC/BC: Exact vs Approx (gamma={gamma})')
    plt.legend()
    plt.grid()
    plt.show()
