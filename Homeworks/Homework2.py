#h will be pi/8, pi/16, pi/32
import math
import numpy as np



# True derivative function
def true_value(x):
    return math.cos(x) * math.pow(math.e, math.sin(x))

# Function f(x)
def func(x):
    return math.pow(math.e, math.sin(x))

# Forward difference approximation
def forward(x, h):
    return (func(x + h) - func(x)) / h

# Backward difference approximation
def backward(x, h):
    return (func(x) - func(x - h)) / h

# Centered difference approximation
def centered(x, h):
    return (func(x + h) - func(x - h)) / (2 * h)

# Interval [a, b]
a = 0
b = math.pi / 2

# Array for h values
array = [2, 3, 4]
hvals = [math.pi * (1 / 2**i) for i in array]

# Loop for h = pi/4
h1 = hvals[0]
interval1 = np.linspace(a, b, int(b / h1) + 1)

print("Table for h = pi/4: ")
print("-" * 30)
errors1 = []
for x in interval1:
    if x == interval1[0]:
        approx = forward(x, h1)
        print(f"Forward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    elif x == interval1[-1]:
        approx = backward(x, h1)
        print(f"Backward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    else:
        approx = centered(x, h1)
        print(f"Centered = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    errors1.append(abs(approx - true_value(x)))
average_error1 = sum(errors1) * h1 * (1 / (b - a))
print(f"\nAverage Error for h = pi/4: {average_error1}")
print("=" * 50, '\n')



# Loop for h = pi/8
h2 = hvals[1]
interval2 = np.linspace(a, b, int(b / h2) + 1)

print("Table for h = pi/8: ")
print("-" * 30)
errors2 = []
for x in interval2:
    if x == interval2[0]:
        approx = forward(x, h2)
        print(f"Forward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    elif x == interval2[-1]:
        approx = backward(x, h2)
        print(f"Backward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    else:
        approx = centered(x, h2)
        print(f"Centered = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    errors2.append(abs(approx - true_value(x)))
average_error2 = sum(errors2) * h2 * (1 / (b - a))
print(f"\nAverage Error for h = pi/8: {average_error2}")
print("=" * 50, '\n')




# Loop for h = pi/16
h3 = hvals[2]
interval3 = np.linspace(a, b, int(b / h3) + 1)

print("Table for h = pi/16: ")
print("-" * 30)
errors3 = []
for x in interval3:
    if x == interval3[0]:
        approx = forward(x, h3)
        print(f"Forward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    elif x == interval3[-1]:
        approx = backward(x, h3)
        print(f"Backward = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    else:
        approx = centered(x, h3)
        print(f"Centered = {approx}, True = {true_value(x)}, Error = {abs(approx - true_value(x))}")
    errors3.append(abs(approx - true_value(x)))
average_error3 = sum(errors3) * h3 * (1 / (b - a))
print(f"\nAverage Error for h = pi/16: {average_error3}")
print("=" * 50)

