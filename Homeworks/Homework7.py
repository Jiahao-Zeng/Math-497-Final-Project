import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define our function f(x,t) = x^2*e^t

def f(x, t):
    return x**2 * np.exp(t)

def fx(x, t):
    return 2 * x * np.exp(t)

def ft(x, t):
    return x**2 * np.exp(t)

#Evaluate the true values at (-1,1)
x_val, t_val = -1, 1
fx_true = fx(x_val, t_val)
ft_true = ft(x_val, t_val)

print("\nTrue Partial Derivatives at (-1,1):")
print(f"fx({x_val}, {t_val}) = {fx_true}")
print(f"ft({x_val}, {t_val}) = {ft_true}")

#approximation with different h values
h_values = [0.1, 0.01, 0.001, 0.0001]

print("\nApproximation of the partial derivatives:")
print(f"{'h':<10}{'fx_approx':<20}{'fx_error':<20}{'ft_approx':<20}{'ft_error':<20}")
print("=" * 90)

for h in h_values:
    fx_approx = (f(x_val + h, t_val) - f(x_val, t_val)) / h
    ft_approx = (f(x_val, t_val + h) - f(x_val, t_val)) / h
    fx_error = abs(fx_approx - fx_true)
    ft_error = abs(ft_approx - ft_true)
    print(f"{h:<10}{fx_approx:<20}{fx_error:<20}{ft_approx:<20}{ft_error:<20}")

#plotting with 3d and mesh using matplotlib "meshgrid"
x_values = np.linspace(-2, 2, 50) # f_x interval
t_values = np.linspace(-1, 3, 50) # f_y interval
X, T = np.meshgrid(x_values, t_values)
Z = f(X, T)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, Z, cmap='viridis', edgecolor='k')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('f(x,t)')
ax.set_title('f(x,t) over the interval [-2,2] & [-1,3]')
plt.show()
