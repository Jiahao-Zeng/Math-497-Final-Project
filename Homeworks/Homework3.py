#in this assignment we do 2 parts and see the error ratios to see if they are meaningful

import math
import numpy as np

#define function
def f(x):
   return math.pow(math.e, math.sin(x))

# True derivative function
def true_value(x):
    return math.cos(x) * math.pow(math.e, math.sin(x))

#fd, bd, and centered
def forward(x, h):
    return (f(x + h) - f(x)) / h

def backward(x, h):
    return (f(x) - f(x - h)) / h

def centered(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Define x0 and h values
x0 = 1  # Point where we approximate the derivative
h_values = [2**-i for i in range(1, 11)]  # h = 1/2, 1/4, ..., 1/1024

# Append errors to list so we can easily change values if need be
fd_errors = []
bd_errors = []
cd_errors = []

for h in h_values:
    fd_approx = forward(x0, h)
    bd_approx = backward(x0, h)
    cd_approx = centered(x0, h)
    exact = true_value(x0)

    fd_errors.append(abs(fd_approx - exact))
    bd_errors.append(abs(bd_approx - exact))
    cd_errors.append(abs(cd_approx - exact))

# Error ratio
fd_error_ratios = [fd_errors[i] / fd_errors[i+1] for i in range(len(fd_errors)-1)]
bd_error_ratios = [bd_errors[i] / bd_errors[i+1] for i in range(len(bd_errors)-1)]
cd_error_ratios = [cd_errors[i] / cd_errors[i+1] for i in range(len(cd_errors)-1)]

print(f"{'h':<20} {'FD Error':<25} {'FD Ratio':<20} {'BD Error':<25} {'BD Ratio':<20} {'CD Error':<25} {'CD Ratio'}")
print("="*150)

for i in range(len(h_values)):
    h = h_values[i]
    fd_err = fd_errors[i]
    bd_err = bd_errors[i]
    cd_err = cd_errors[i]
    
    fd_ratio = fd_error_ratios[i-1] if i > 0 else "--"
    bd_ratio = bd_error_ratios[i-1] if i > 0 else "--"
    cd_ratio = cd_error_ratios[i-1] if i > 0 else "--"
    
    print(f"{h:<20} {fd_err:<25} {fd_ratio:<20} {bd_err:<25} {bd_ratio:<20} {cd_err:<25} {cd_ratio}")

#PART2
array = [3, 4, 5]
hvals = [math.pi * (1 / 2**i) for i in array]

print("\nSecond Part: On [0, pi/2] for h = (pi/2)^i, i = 3, 4, 5")
print(f"{'h':<20} {'FD Error':<25} {'FD Ratio':<20} {'BD Error':<25} {'BD Ratio':<20} {'CD Error':<25} {'CD Ratio'}")
print("="*150)

fd_errors = []
bd_errors = []
cd_errors = []

for h in hvals:
    fd_approx = forward(x0, h)
    bd_approx = backward(x0, h)
    cd_approx = centered(x0, h)
    exact = true_value(x0)

    fd_errors.append(abs(fd_approx - exact))
    bd_errors.append(abs(bd_approx - exact))
    cd_errors.append(abs(cd_approx - exact))

fd_error_ratios = [fd_errors[i] / fd_errors[i+1] for i in range(len(fd_errors)-1)]
bd_error_ratios = [bd_errors[i] / bd_errors[i+1] for i in range(len(bd_errors)-1)]
cd_error_ratios = [cd_errors[i] / cd_errors[i+1] for i in range(len(cd_errors)-1)]

for i in range(len(hvals)):
    h = hvals[i]
    fd_err = fd_errors[i]
    bd_err = bd_errors[i]
    cd_err = cd_errors[i]
    
    fd_ratio = fd_error_ratios[i-1] if i > 0 else "--"
    bd_ratio = bd_error_ratios[i-1] if i > 0 else "--"
    cd_ratio = cd_error_ratios[i-1] if i > 0 else "--"
    
    print(f"{h:<20} {fd_err:<25} {fd_ratio:<20} {bd_err:<25} {bd_ratio:<20} {cd_err:<25} {cd_ratio}")

