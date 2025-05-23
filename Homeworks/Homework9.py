import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def solve_density(dx, dt, T=1, X=1):
    v = dt / dx  # calculate our v
    M = int(X / dx)  #number of steps in s
    N = int(T / dt)  #number of steps int 
    
    P = np.zeros((N+1, M+1))  #create the grid
    P[:, 0] = 0.5  #initialize our boundary condition P^n_0 = 0.5
    
    for n in range(N):
        for j in range(1, M+1):
            P[n+1, j] = (1 - v) * P[n, j] + v * P[n, j-1]  #solution
    
    return P, dx * np.arange(M+1), dt * np.arange(N+1)

def plot_solution(P, x, t, title):
    X, T = np.meshgrid(x, t)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, P, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('Density P')
    ax.set_title(title)
    plt.show()

def exact_solution(x, t):
    return np.where(x < t, 0.5, 0)

def plot_exact_solution(dx, dt, title):
    M = int(1 / dx)
    N = int(1 / dt)
    x = dx * np.arange(M+1)
    t = dt * np.arange(N+1)
    X, T = np.meshgrid(x, t)
    Z = exact_solution(X, T)
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, Z, cmap='coolwarm')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('Exact Solution')
    ax.set_title(title)
    plt.show()

#run for each case
cases = [(0.2, 0.2), (0.2, 0.1), (0.01, 0.008)]
for dx, dt in cases:
    P, x, t = solve_density(dx, dt)
    plot_solution(P, x, t, f'Approximate Solution for dx={dx}, dt={dt}')
    plot_exact_solution(dx, dt, f'Exact Solution for dx={dx}, dt={dt}')
