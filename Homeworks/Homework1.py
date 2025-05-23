import math

"""
#import numpy as np
#Part 1
#Approximating the derivative using forward, backward, and centered difference
#python uses sin in radians by default, so we must first convert our degrees into radians to get the correct output
"""
#def a simple function for the problem f(x) = e^sinx, we can use this function instead of manually typing everything in, and for quick testing to make sure the function works
def func(x):
    return pow(math.e, math.sin(x))

#we know the value of f'(x) at x = 0 is 1, therefore for our error values, we use 1 as the actual value
def Forward_approximation(a,h):
    Forward = (func(a+h)-func(a))/h
    return Forward

def Backward_approximation(a,h):
    Backward = (func(a)-func(a-h))/h
    return Backward

def Centered_approximation(a,h):
    Centered = (func(a+h)-func(a-h))/(2*h)
    return Centered

def Forward_error(f):
    return abs(1-f)

def Backward_error(b):
    return abs(1-b)

def Centered_error(c):
    return abs(1-c)
#Tests
"""
#print(Forward_approximation(a,h))
#print(Backward_approximation(a,h))
#print(Centered_approximation(a,h))
#print(Forward_error(Forward_approximation(a,h)))
#print(Backward_error(Backward_approximation(a,h)))
#print(Centered_error(Centered_approximation(a,h)))
"""
#Part 2

print('\nTable 1')
print("H Value        | Forward Approximation | Error      ")
print("-"*50)
for i in range(1,11):
    h = (1/2) ** i 
    a = 0
    print(f"{h:<14} | {Forward_approximation(a, h):<20} | {Forward_error(Forward_approximation(a, h)):<10}")

print("\nTable 2")
print("H Value        | Backward Approximation | Error      ")
print("-"*50)
for i in range(1,11):
    h = (1/2) ** i 
    a = 0
    print(f"{h:<14} | {Backward_approximation(a, h):<20} | {Backward_error(Backward_approximation(a, h)):<10}")

print("\nTable 3")
print("H Value        | Centered Approximation | Error      ")
print("-"*50)
for i in range(1,11):
    h = (1/2) ** i 
    a = 0
    print(f"{h:<14} | {Centered_approximation(a, h):<20} | {Centered_error(Centered_approximation(a, h)):<10}")
