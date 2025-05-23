### PART 1
import math
### Calculating Initial Values over an interval
T = 2 #final t
t0 = 1 #initial t
dt = 0.2 #step
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

#error
print(f"{'t: ':<8}{'Calculated y: ':<24}{'True y: ':<24}{'Error: ':<20}")
print("=" * 90)
for i in range(n + 1):
    t = t_values[i]
    y_calc = y[i]
    true_y = true_value(t)
    error = abs(y_calc- true_y)
    print(f"{t:<5.2f}\t{y_calc:<20}\t{true_y:<20}\t{error:<20}")

