### PART 3 PLOTTING
import matplotlib.pyplot as plt
import math
### Calculating Initial Values over an interval
T = 2 #final t
t0 = 1 #initial t
dt = 0.05 #step
n = int((T-t0)/dt) #note that n is going to be equal to 5 here
y0 = -1

# function
def function(r,s):
    return (1/r**2) - (s/r) - (s**2)


t_values = [t0 + i * dt for i in range(n + 1)]
y = [y0] + [0] * n

value = [t0+i*dt for i in range(n+1)]
y = [y0 for i in range(n+1)]
for j in range(n):
    y[j+1] = y[j]+dt*function(value[j],y[j])

for i in range(n+1):
    print(value[i],y[i])

def true_value(t):
    return -1/t


true = []
#error
print(f"{'t: ':<8}{'Calculated y: ':<24}{'True y: ':<24}{'Error: ':<20}")
print("=" * 90)
for i in range(n + 1):
    t = t_values[i]
    y_calc = y[i]
    true_y = true_value(t)
    true.append(true_value(t))
    error = abs(y_calc- true_y)
    print(f"{t:<5.2f}\t{y_calc:<20}\t{true_y:<20}\t{error:<20}")

print(t_values)

plt.figure(figsize=(8, 5))
plt.plot(t_values, y, label="Approximate Solution", linestyle="--", marker="o")
plt.plot(t_values, true, label="True Solution", linestyle="-", marker="x")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Approximation vs. True Solution")
plt.legend()
plt.grid()
plt.show()

#avg error calculation

step_values = [0.2, 0.1, 0.05, 0.0125, 0.00625]
average_errors = []  # List to store average errors for each step size

for dt in step_values:
    #initial
    t0, T, y0 = 1, 2, -1
    n = int((T - t0) / dt)  # Number of steps

    t_values = [t0 + i * dt for i in range(n + 1)]
    y = [y0] + [0] * n

    for j in range(n):
        y[j + 1] = y[j] + dt * function(t_values[j], y[j])

    true = [true_value(t) for t in t_values]
    errors = [abs(y[i] - true[i]) for i in range(n + 1)]
    average_error = sum(errors) / len(errors)  # Compute average error
    average_errors.append(average_error)  # Store the average error

plt.figure(figsize=(8, 5))
plt.plot(step_values, average_errors, marker="o", linestyle="--")
plt.xlabel("Step Size (Δt)")
plt.ylabel("Average Error")
plt.title("Average Error vs. Step Size")
plt.grid()
plt.show()
