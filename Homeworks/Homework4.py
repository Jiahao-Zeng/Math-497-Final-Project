import math
import numpy as np

#define function
def f(x):
    return np.exp(2*x + 1)

# True derivative function
def true_value(x):
    return 2 * np.exp(2*x + 1)

# Three-point forward difference formula
def three_point_fd(x, h):
    return (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2*h)

# Three-point backward difference formula
def three_point_bd(x, h):
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)

# Centered difference formula
def centered(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Define interval and h values
x_values = [round(i * 0.1, 1) for i in range(11)]  # 11 points in [0,1]
h_values = [0.1, 0.01, 0.001]

for h in h_values:
    print(f"\n{'='*40}")
    print(f"Table for h = {h} ")
    print(f"{'='*40}\n")
    print(f"{'x':<12}{'Approximation':<25}{'Actual Value':<25}{'Error'}")
    print("-"*80)

    for i in x_values:
        if i == 0:
            approx = three_point_fd(i, h)
        elif i == len(x_values) - 1:
            approx = three_point_bd(i, h)
        else:
            approx = centered(i, h)
        
        true_val = true_value(i)
        error = abs(approx - true_val)
        
        print(f"{i:<10}{approx:<25}{true_val:<25}{error}")
    print(f"\n{'-'*40}")
    print(f"{'='*40}\n")

