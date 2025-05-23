##PART 2
import math
### Calculating Initial Values over an interval
T = 3  # final t
t0 = 2  # initial t
dt = 0.1  # step
n = int((T - t0) / dt)  #note that n is going to be 10
y0 = 3

# function
def function(r, s):
    return (1 / r) * (2 - s)

# actual value
def true_value(t):
    return (2 / t) + 2


t_values = [t0 + i * dt for i in range(n + 1)]
y = [y0] + [0] * n  # Initialize y values

for j in range(n):
    y[j + 1] = y[j] + dt * function(t_values[j], y[j])

# error
print(f"{'t: ':<8}{'Calculated y: ':<24}{'True y: ':<24}{'Error: ':<20}")
print("=" * 90)
for i in range(n + 1):
    t = t_values[i]
    y_calc = y[i]
    true_y = true_value(t)
    error = abs(y_calc - true_y)
    print(f"{t:<5}	{y_calc:<20}	{true_y:<20}	{error:<20}")
