import numpy as np
import matplotlib.pyplot as plt

### Define Step sizes
dx = (1/2)**6  # dx
dt = (1/2) * dx  # dt
v = dt / dx  # v ratio

### Grid points
x_values = np.arange(0, 1 + dx, dx)  
t_values = np.arange(0, 1 + dt, dt) 

M = len(x_values) - 1  # Number of space steps
N = len(t_values) - 1  # Number of time steps

### QUESTION 1: Solve the first numerical scheme

### P Values for Q1
P_q1 = np.zeros((N + 1, M + 1))

### Boundary Conditions 
P_q1[:, 0] = 0.5  

### Using upwind
for n in range(N):
    for j in range(1, M + 1):
        P_q1[n + 1, j] = (1 - v) * P_q1[n, j] + v * P_q1[n, j - 1]

### Define the exact solution function p(x, t)
def rho_exact(x, t):
    return 0.5 if 0 <= x < t else 0

### QUESTION 3: Compute approximation errors for Question 1

errors_q1 = {}  

for t_check in [0.2, 0.4, 0.6, 0.8, 1.0]:
    n_index = int(t_check / dt)  
    exact_rho = np.array([rho_exact(x, t_check) for x in x_values])  
    error_norm = dx * np.sum(np.abs(exact_rho - P_q1[n_index, :]))  
    errors_q1[t_check] = error_norm

### Print the errors for Q1
print("\nApproximation errors for Question 1:")
for t, err in errors_q1.items():
    print(f"t = {t}: {err:.6e}")

### QUESTION 2: Solve the modified method
gamma = 1

### P values for Q2
P_q2 = np.zeros((N + 1, M + 1))

### Boundary Condition
P_q2[:, 0] = 0.5  

### Step 1 and Step 2: Use Upwind Scheme to Fill Missing Data
for n in range(2):  # Compute for n = 0 and n = 1 using upwind
    for j in range(1, M + 1):
        P_q2[n + 1, j] = (1 - v) * P_q2[n, j] + v * P_q2[n, j - 1]

### Remaining steps: Use saved upwind results in second-order scheme
for n in range(2, N):  # Start from n=2 since we now have enough data
    for j in range(1, M + 1):  
        P_q2[n + 1, j] = (gamma + (1 - v) * (1 - gamma / 2)) * P_q2[n, j] - (gamma / 2) * P_q2[n - 1, j] + v * (1 - gamma / 2) * P_q2[n, j - 1]

### Print density values at specified time steps for Question 2
print("\nDensity values for Question 2:")
for t_check in [0.2, 0.4, 0.6, 0.8, 1.0]:
    n_index = int(t_check / dt)  
    print(f"t = {t_check}: {P_q2[n_index, :]}")

### QUESTION 3: Compute approximation errors for Question 2

errors_q2 = {}

for t_check in [0.2, 0.4, 0.6, 0.8, 1.0]:
    n_index = int(t_check / dt)  
    exact_rho = np.array([rho_exact(x, t_check) for x in x_values])  
    error_norm = dx * np.sum(np.abs(exact_rho - P_q2[n_index, :]))  
    errors_q2[t_check] = error_norm

### Print the errors for Question 2
print("\nApproximation errors for Question 2:")
for t, err in errors_q2.items():
    print(f"t = {t}: {err:.6e}")

### QUESTION 4: Plot error values from Question 1 and Question 3

### User error values for plots
t_vals = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
errors_q1_vals = np.array([errors_q1[t] for t in t_vals])  
errors_q2_vals = np.array([errors_q2[t] for t in t_vals])  

plt.figure(figsize=(8, 5))
plt.plot(t_vals, errors_q1_vals, marker='o', linestyle='-', color='red', label='Error in Q1')
plt.plot(t_vals, errors_q2_vals, marker='s', linestyle='-', color='blue', label='Error in Q2')

plt.xlabel('Time (t)')
plt.ylabel('Error Norm ||E^n||')
plt.title('Approximation Errors vs. Time')
plt.legend()
plt.grid(True)

plt.show()
