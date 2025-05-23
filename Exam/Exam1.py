import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 497 EXAM 1 PART 2

# Question 1
def func(x):
    return x**3 - 7*x**2 + 1

def Forward_approximation(a, h):
    return (func(a + h) - func(a)) / h

def Forward_error(f, true_value):
    return abs(true_value - f)
print("Table 1: Forward Difference Approximation f'(1)")
print("H Value        | Forward Approximation")
for i in range(1, 11):
    h = (1/2) ** i
    a = 1
    forward_approx = Forward_approximation(a, h)
    print(f"{h:<14} | {forward_approx:<20}")

# Question 2
# True derivative f'(x) = 3x^2 - 14x => f'(1) = -11
true_derivative = -11
print("Table 2: Forward Difference Approximation and Errors for f'(1)")
print("H Value        | Forward Approximation | Error               |Error / h")
print("-" * 80)
previous_error = None
for i in range(1, 11):
    h = (1/2) ** i
    a = 1
    forward_approx = Forward_approximation(a, h)
    error = Forward_error(forward_approx, true_derivative)
    if previous_error is not None:
        error_ratio = previous_error/error
    else:
        error_ratio= "N/A"
    print(f"{h:<14} | {forward_approx:<20} | {error:<20} | {error_ratio:<10}")
    previous_error = error  # Store current error for next iteration
#we can see that as h decreases by 1/2 our error is 2x more precise, this is concurrent with O(h)

# Question 3
def three_point_fd(x, h):
    return (-3*func(x) + 4*func(x + h) - func(x + 2*h)) / (2*h)
print("\nTable 3: Three-Point Approximation of f'(x) over [0,1]")
print("x Value        | Three-Point Approximation")
print("-" * 50)
x_values = [i / 10 for i in range(11)]
h = 0.01 
for x in x_values:
    three_point_approx = three_point_fd(x, h)
    print(f"{x:<14} | {three_point_approx:<20}")


# Question 4
def g(x):
    return 2* np.exp(-x)
def third_derivative_approximation(h):
    x_i = 0 
    return (g(x_i + 2*h) - 2*g(x_i + h) + 2*g(x_i - h) - g(x_i - 2*h)) / (2 * h**3)
print("\nTable 4: Third derivative approximation of g'''(x)")
print("H Value        | Approximation (true value = -2)")
print("-" * 50)
for i in range(1, 4):
    h = 0.1 ** i
    approximation = third_derivative_approximation(h)
    
    
    print(f"{h:<14.5f} {approximation:<20}")

# Question 5-7
### Calculating Initial Values over an interval
import numpy as np
import matplotlib.pyplot as plt

T = 1
t0 = 0
y0 = -1
true_value = lambda t: (t + 1) - 2 * np.exp(t)
step_values = [0.1, 0.01, 0.001, 0.0001]
plot_values = [0.01]
def function(y, t):
    return y - t

for dt in plot_values:
    n = int((T - t0) / dt)
    t_values = [t0 + i * dt for i in range(n + 1)]
    y = [y0] + [0] * n
    
    for j in range(n):
        y[j + 1] = y[j] + dt * function(y[j], t_values[j])

    true = [true_value(t) for t in t_values]
    errors = [abs(y[i] - true[i]) for i in range(n + 1)]
    
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, y, label=f"Approx. Solution (dt={dt})", linestyle="--", marker="o")
    plt.plot(t_values, true, label="True Solution", linestyle="-", marker="x")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title(f"Approximation vs. True Solution (dt={dt})")
    plt.legend()
    plt.grid()
    plt.show()

    average_error = sum(errors) / len(errors)
    print(f"Average Error for dt={dt}: {average_error:.6f}")

average_errors = []
for dt in step_values:
    n = int((T - t0) / dt)
    t_values = [t0 + i * dt for i in range(n + 1)]
    y = [y0] + [0] * n
    
    for j in range(n):
        y[j + 1] = y[j] + dt * function(y[j], t_values[j])
    
    true = [true_value(t) for t in t_values]
    errors = [abs(y[i] - true[i]) for i in range(n + 1)]
    average_error = sum(errors) / len(errors)
    average_errors.append(average_error)

plt.figure(figsize=(8, 5))
plt.plot(step_values, average_errors, marker="o", linestyle="--")
plt.xlabel("Step Size (Δt)")
plt.ylabel("Average Error")
plt.title("Average Error vs. Step Size")
plt.grid()
plt.show()


# Question 8 - 10
def f(x, t):
    return (x**2)*t * (t**2)

def fx_partial(x, t):
    return 2*x*t

def ft_partial(x, t):
    return (x**2) * (2*t)


x_val, t_val = -1, 1
fx_true = fx_partial(x_val, t_val)
ft_true = ft_partial(x_val, t_val)

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
#3d graphs with different step sizes
step_sizes = [(0.01, 0.01)]
for dx, dt in step_sizes:
    x_values = np.arange(0, 2 + dx, dx)
    t_values = np.arange(-2, 0 + dt, dt)
    X, T = np.meshgrid(x_values, t_values)
    Z = f(X, T)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, Z, cmap='viridis', edgecolor='k')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('f(x,t)')
    ax.set_title(f'3D Plot of f(x,t) with dx={dx}, dt={dt}')
    plt.show()
