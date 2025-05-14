
---
layout: article
title: name here
permalink: /Lecture Notes & Overview/
use_math: true
---
##### First Derivative Approximation
$$
\text{First derivatve: }f'(a) = \lim_{ h \to 0 } \frac{f(a=h)-f(a)}{h}
$$
$$
\text{Slope: } \frac{f(a+h-f(a))}{a+h-a}
$$
- We can use the slop of the point as an approximation of the slope of the tangent line

##### 1. Forward Difference:
- The first derivative approximation of function f(x) at point x = a, given the h-value is:
$$
f'(a) \approx \frac{f(a+h)-f(a)}{h}
$$
##### 2. Backward Difference: 
$$
f'(a) \approx \frac{f(a) - f(a-h)}{h}
$$
##### 3. Centered difference: 
$$
f'(a) \approx \frac{f(a+h)-f(a-h)}{2h}
$$
Example 1:
- For h =1 and h =0.1, approximate f'(1) with f(x)= $x^3$ using forward, backward, and centered difference methods.
- Forward: 
$$
\begin{align}
h &= 1 \\
a&=1 \\
h&=0.1 \\
a &=1 \\
\text{Forward Difference: }\frac{f(2) -f(1)}{1} &= 7 \\
\text{Backward Difference: }\frac{f(1) -f(0)}{1} &=1 \\
\text{Centered Difference: }\frac{f(2)-f(0)}{2} &= 4 \\
\text{Forward Difference: }\frac{f(1.1) -f(1)}{0.1} &= 3.31 \\
\text{Backward Difference: }\frac{f(1) -f(0.9)}{0.1} &= 2.71 \\
\text{Centered Difference: }\frac{f(2)-f(0.9)}{0.2} &= 3.01
\end{align}
$$
- Finding the error
$$
\begin{align}
\mid \text{true value - approximated value}\mid \\
\text{Forward Difference Error @ h = 1:} \lvert 3-7 \rvert &= 4\\
\text{Backward Difference Error @ h = 1:} \lvert 3-1 \rvert &= 2\\
\text{Centered Difference Error @ h = 1:} \lvert 3-4 \rvert &= 1\\

\end{align}
$$
##### Algorithm
- Define function f(x)
- Input x = a
- Input $h = \frac{1}{2}^i$ ; $i = 1,2,\dots,10$
- Calculate:
$$
FD = \frac{f(a+h) -f(a)}{h} \text{ BD OR CD}
$$
- Evaluate Error
- Print the calculation
- For future reference don't limit the rounding as the numbers will be non-zero but never should be 0

##### First derivative approximation on an Interval $[a,b]$
Limit definition for derivative as a function:
$$
\begin{align}
f'(x) = \lim_{ h \to 0 } \frac{f(x+h)-f(x)}{h} 
\end{align}
$$
approximating $f'(x_{i})$:
##### 1. Forward Difference:
- The first derivative approximation of function f(x) at point x = a, given the h-value is:
$$
f'(x_{i}) \approx \frac{f(x_{i}+h)-f(x_{i})}{h}
$$
##### 2. Backward Difference: 
$$
f'(x_{i}) \approx \frac{f(x_{i}) - f(x_{i}-h)}{h}
$$
##### 3. Centered difference: 
$$
f'(x_{i}) \approx \frac{f(x_{i}+h)-f(x_{i}-h)}{2h}
$$
- For the first point you need to use forward difference, and for the last point you need to use the backward difference. Anything in between a and b you can use centered difference.
- Algorithm
	- Define f(x)
	- Input h value
	- Input a & b for interval $[a,b]$
	- Set x values as an array
	- Approximate 1st derivative over x values in the array
	- FD, BD, CD
	- Evaluate the error of approximation at any x values in the array -> array of point-wise errors
	- $$
\begin{align}
&f(x) \text{ over } [a,b] \\
&f_{\text{avg}} =\frac{1}{b-a}\int_{a}^{b} f(x)dx
\end{align}
$$
	- evaluate average error: $\left[ \sum_{}^{}(\text{error at any x}) *h \right] \frac{*1}{b-a}$

##### Using Taylor Series to Calculate error
1.  FD $f'(x_{i}) \approx \frac{f(x_{i+1}-f(x_{i}))}{h} \text{; } h =x_{i+1}-x_{i}$
- $\text{around } x = a_{i}; f(x) = \sum_{n = 0}^{\infty} \frac{1}{n!}f^{n}a(x-a)^n$
- Taylor series expansion of f(x) around xi:
	- $f(x) = ( x_{i}+f'(x_{i})(x-x_{i})+\frac{1}{2}f''(c)(x-x_{i})^2$

$$
\begin{align}
&\text{choose }x = x_{i+1}:  \\
&f(x_{i+1}) = f(x_{i}) + f'(x_{i})(x_{i+1}-x_{i}) + \frac{1}{2}f''(c)(x_{i+1}-x_{i})^2 \\
& f(x_{i+1}) = f(x_{i}) + hf'(x_{i}) + \frac{1}{2}f''(c)h^2 \\
& \frac{f(x_{i+1})-f(x_{i})}{h} = f'(x_{i})+\frac{1}{2}f''(c) \text{ which gives us } x_{i} \leq C \leq x_{i+1} \\
&[\frac{f(x_{i+1})-f(x_{i})}{h}] \text{FD } - f'(x_{i}) = \frac{1}{2}f''(c)h \\
&|\frac{f(x_{i+1})-f(x_{i})}{h} - f'(x_{i})| = |\frac{1}{2}f''(c)h|
\end{align}
$$
##### Differential Equation Approximation:
- For functions of one variable a differential equation is an equation involving any derivative of the function
- Example: 
	- $y'+y(t)=e^{t} \to y' = e^{t}-ty(t), f(t,y)$
	- $y''-\sin ty'(t)=0$
	- $y'(t)=\frac{1}{t}-\frac{1}{t^{2}}y(t)+y^{2}(t), f(t,y)$
	- $y(t)y'(t)+y''(t)=\cos t$
- Note: If the differential equation involves the first derivative, then it is called a first order differential equation. Or 1st order ODE "Ordinary Differential Equation"

First Order ODE:
- $y'(t) = f(t,y)$
- $y(t_{0}) = y_{0}$ on $[t_{0},T]$ (This is the Initial Value or initial condition)

Population Model (Real world example)

$\frac{dP}{dt} = kP$
$P(t_{0})=P_{0}$

How do we solve the above initial value differential equation numerically if an analytical solution doesn't exist?
$y'(t) = f(t,y)$

We Begin by discretizing the interval $[t_{0}, T]$:
- $t_{0},t_{1},t_{2},\dots,t_{n}=T$
- The goal is to find $y(t_{1}),y(t_{2}),y(t_{3}),\dots,y(t_{N})$
- $\Delta t = t_{i+1}-t_{i}$ for all $i = 0, \dots, N-1$
- $t_{0},t_{1}=t_{0}+\Delta t, t_{2}=t_{1}+\Delta{t} ,\dots$

Forward Difference as it relates to a differential equation:
$$
y'(t_{i})\approx \frac{y(t_{i+1})-y(t_{i})}{\Delta t}
$$
Let $y(t_{i})=y_{i}, \to y'_{i} \approx \frac{y_{i+1}-y_{i}}{\Delta t}$; $y_{i}' = f(t_{i},y_{i})$

$\frac{y_{i+1}-y_{i}}{\Delta t} \approx f(t_{i},y_{i})$ solve for $y_{i+1}$
$y_{i+1} \approx y_{i} + \Delta tf(t_{i,y_{i}})$

For Example:
Given the initial value problem, where the true solution is: $y = -\frac{1}{t}$
$y'(t)=\frac{1}{t^{2}}-\frac{1}{t}y-y^{2}$; $y(1)=-1$
$y(t_{0})=y_{0}=-1$

We can now use the forward difference to approximate the solution on $[1,2]$ with $\Delta t = 0.2$
$i = 0,1,2,3,4,5$
$t_{0}=1, t_{1} = 1.2, t_{2} = 1.4, t_{3} = 1.6, t_{4} = 1.8 t_{5} = 2$
$y_{i+1}=y_{i}+\Delta\left( \frac{1}{t_{i^{2}}} -\frac{1}{ti}y_i-y^{2}_{i}\right)$

Doing the calculations we get

| i   | $t_{i}$ | $y_{i+1}$     |
| --- | ------- | ------------- |
| 1   | 1.2     | -0.8          |
| 2   | 1.4     | -0.6557       |
| 3   | 1.6     | -0.545976     |
| 4   | 1.8     | -0.45922195   |
| 5   | 2       | -0.3669193442 |

##### Plotting Solution & Error Notes:


##### Approximating the 2nd Derivative

$$
\begin{align}
&f''(a) = \lim_{ h \to 0 } \frac{f'(a+h)-f'(a) }{h} \to f''(a) \approx \frac{f'(a+h)-f'(a)}{h} \\
& f''(a) \approx \frac{\frac{1}{h}[f(a+h)-f(a)-(f(a)-f(a+h))]}{h} \\
& \approx \frac{f(a+h)-2f(a)+f(a+h)}{h^2}
\end{align}
$$
##### Functions of two variables

##### Functions of two variables

The graph of a single‐variable function is
$$
y = f(x)
\quad\longleftrightarrow\quad
(x,\,f(x)),
$$
while a two‐variable function is
$$
z = f(x,y)
\quad\longleftrightarrow\quad
(x,\,y,\,f(x,y)).
$$

**Examples:**
- Volume of a cylinder of radius \(r\) and height \(h\):
  $$
  V(r,h) = \pi\,r^2\,h.
  $$
- Population at location \(x\) and time \(t\):
  $$
  P(x,t).
  $$
- Temperature along a rod at \(x\) and \(t\):
  $$
  T(x,t).
  $$
- Total vitamin C intake (tablet + glass of OJ):
  $$
  C(x,y) = 500x + 300y,
  \quad
  C(1,2) = 500\,(1) + 300\,(2) = 1100\text{ mg}.
  $$

##### Partial derivatives

For \(z = f(x,y)\), we define

$$
f_x(x,y) = \frac{\partial f}{\partial x}(x,y),
\qquad
f_y(x,y) = \frac{\partial f}{\partial y}(x,y).
$$

- **Notation:** \(\partial z/\partial x,\;\partial f/\partial x,\;f_x\) and \(\partial z/\partial y,\;\partial f/\partial y,\;f_y\).

- **Example function:**
  $$
  f(x,y) = x^2 - 3xy + 2y^3.
  $$
  Then
  $$
  f_x(x,y) = 2x - 3y,
  \quad
  f_y(x,y) = -3x + 6y^2.
  $$

- **At the point \((1,-1)\):**
  $$
  f_x(1,-1) = 2(1) - 3(-1) = 5,
  \quad
  f_y(1,-1) = -3(1) + 6(-1)^2 = 3.
  $$

##### Limit definitions

$$
f_x(x,y)
= \lim_{h\to 0}\;\frac{f(x+h,y) - f(x,y)}{h},
\qquad
f_y(x,y)
= \lim_{h\to 0}\;\frac{f(x,y+h) - f(x,y)}{h}.
$$

##### Example: Numerical approximation of partials

Approximate \(f_x(1,-1)\) and \(f_y(1,-1)\) for \(h=0.5,\,0.1,\,0.05\), where
$f(x,y)=x^2 -3xy +2y^3.$
Use the forward‐difference formulas:
$$
f_x(x,y)\approx \frac{f(x+h,y) - f(x,y)}{h},
\qquad
f_y(x,y)\approx \frac{f(x,y+h) - f(x,y)}{h}.
$$

##### Algorithm

1. **Define**  
   \(\displaystyle f(x,y)=x^2 -3xy +2y^3.\)

2. **For each** \(h\in\{0.5,\,0.1,\,0.05\}\):  
   - Compute
     $$
     f_x(1,-1;h)
     = \frac{f(1+h,-1)-f(1,-1)}{h},
     \quad
     f_y(1,-1;h)
     = \frac{f(1,-1+h)-f(1,-1)}{h}.
     $$
2. **Tabulate** the results $(h,\;f_x,\;f_y)$.


##### Real life applications Using Traffic Model

##### Conservation of Vehicles

- Number of cars between \(A\) and \(B\):
  $$
  N_{AB}(t) = \int_A^B \rho(x,t)\,dx.
  $$
- Flux at \(x,t\): \(q(x,t)\).
- Conservation law (inflow minus outflow):
  $$
  \frac{dN_{AB}}{dt}
  = q(A,t) - q(B,t).
  $$
- By the Fundamental Theorem of Calculus:
  $$
  \frac{d}{dt}\!\int_A^B \rho(x,t)\,dx
  = \int_A^B \rho_t(x,t)\,dx
  = q(A,t) - q(B,t)
  = -\int_A^B q_x(x,t)\,dx.
  $$
- Since this holds for any \(A,B\), we get the local PDE:
  $$
  \boxed{\rho_t + q_x = 0.}
  $$

---

##### Traffic Flow Model

- Assume linear flux: 
  $$
  q = v\,\rho,\qquad v\neq 1\ (\text{constant speed}).
  $$
- Governing PDE:
  $$
  \boxed{\rho_t + v\,\rho_x = 0.}
  $$
- Domain: \(0\le x\le 1,\;0\le t\le 1.\)
- Initial condition:
  $$
  \rho(x,0) = \rho_0.
  $$
- Boundary condition:
  $$
  \rho(0,t) = \rho_L.
  $$

---

##### Discretization

- Spatial grid: 
  $$
  x_j = j\,\Delta x,\quad j=0,\dots,M.
  $$
- Time steps:
  $$
  t^n = n\,\Delta t,\quad n=0,\dots,N.
  $$
- Numerical solution:
  $$
  P_j^n \approx \rho(x_j,\,t^n).
  $$

---

##### Finite‐Difference Approximations

- Time derivative:
  $$
  \rho_t(x_j,t^n)
  \approx 
  \frac{P_j^{n+1} - P_j^n}{\Delta t}.
  $$
- Spatial derivative (upwind/backward):
  $$
  \rho_x(x_j,t^n)
  \approx
  \frac{P_j^n - P_{j-1}^n}{\Delta x}.
  $$

---

##### Upwind Scheme

- Plug into \(\rho_t + v\,\rho_x = 0\):
  $$
  \frac{P_j^{n+1} - P_j^n}{\Delta t}
  + v\,\frac{P_j^n - P_{j-1}^n}{\Delta x}
  = 0.
  $$
- Define the CFL number:
  $$
  \nu = \frac{v\,\Delta t}{\Delta x}.
  $$
- Solve for \(P_j^{n+1}\):
  $$
  \boxed{
    P_j^{n+1}
    = P_j^n - \nu\,(P_j^n - P_{j-1}^n)
    = (1-\nu)\,P_j^n + \nu\,P_{j-1}^n.
  }
  $$

---

##### Initial & Boundary Conditions

- **Initial:**  
  $$
  P_j^0 = \rho_0,\quad j=0,\dots,M.
  $$
- **Boundary:**  
  $$
  P_0^n = \rho_L,\quad n=0,\dots,N.
  $$

---

##### CFL Condition

- For stability (and to respect causality), require
  $$
  \nu \le 1.
  $$

### Traffic Flow Algorithm

##### Conservation of the Number of Vehicles

- **Total cars between \(A\) and \(B\):**
  $$
  N_{AB}(t) = \int_{A}^{B}\!\rho(x,t)\,dx,
  $$
  where \(\rho(x,t)\) is the car density.

- **Flux at a point:** \(q(x,t)\).

- **Rate of change = inflow − outflow:**
  $$
  \frac{dN_{AB}}{dt}
  = q(A,t)\;-\;q(B,t).
  $$

- **By the FTC and interchanging \(\tfrac{d}{dt}\) with the integral:**
  $$
  \int_{A}^{B}\rho_t\,dx
  = q(A,t)-q(B,t)
  = -\int_{A}^{B}q_x\,dx.
  $$

- **Local form (for all \(A,B\)):**
  $$
  \boxed{\rho_t + q_x = 0.}
  $$

- **Linear flux model:** \(q = v\,\rho\) \(\,(\,v\neq1\text{ constant speed}\,)\)  
  so the PDE becomes
  $$
  \boxed{\rho_t + v\,\rho_x = 0.}
  $$

---

##### Variables, Domain & Conditions

- **Independent variables:**  
  \(0 \le x \le 1,\quad 0 \le t \le 1.\)

- **Initial condition:**  
  $$
  \rho(x,0) = \rho_0,\quad 0 \le x \le 1.
  $$

- **Boundary condition:**  
  $$
  \rho(0,t) = \rho_L,\quad 0 \le t \le 1.
  $$

---

##### Discretization

- **Spatial mesh:**  
  $$
  x_j = j\,\Delta x,\quad j=0,1,\dots,M,
  \quad \Delta x = \frac{1}{M}.
  $$

- **Time steps:**  
  $$
  t^n = n\,\Delta t,\quad n=0,1,\dots,N,
  \quad \Delta t = \frac{1}{N}.
  $$

- **Approximation:**  
  $$
  P_j^n \approx \rho(x_j,\,t^n).
  $$

---

##### Finite‐Difference Approximations

- **Time derivative (forward):**  
  $$
  \rho_t(x_j,t^n)
  \approx
  \frac{P_j^{n+1} - P_j^n}{\Delta t}.
  $$

- **Spatial derivative (backward/upwind):**  
  $$
  \rho_x(x_j,t^n)
  \approx
  \frac{P_j^n - P_{j-1}^n}{\Delta x}.
  $$

---

##### Upwind Scheme

1. Substitute into \(\rho_t + v\,\rho_x = 0\):
   $$
   \frac{P_j^{n+1}-P_j^n}{\Delta t}
   + v\,\frac{P_j^n - P_{j-1}^n}{\Delta x}
   = 0.
   $$

2. Define the Courant number:
   $$
   \nu = \frac{v\,\Delta t}{\Delta x}.
   $$

3. Solve for \(P_j^{n+1}\):
   $$
   \boxed{
     P_j^{n+1}
     = P_j^n - \nu\,(P_j^n - P_{j-1}^n)
     = (1-\nu)\,P_j^n + \nu\,P_{j-1}^n.
   }
   $$

---

##### Stability (CFL Condition)

- To ensure stability and causality:
  $$
  \nu \le 1
  \quad\Longleftrightarrow\quad
  v\,\frac{\Delta t}{\Delta x} \le 1.
  $$
