The difference for approximating the second derivative of a function requires the function value at three consecutive points. Given the $h$ value $(h = x_{i+1}-x_{i})$, the three-point difference formula for the 2nd derivative approximation is as follows:

$$
\begin{align}
f''(x_{i}) \approx \frac{f(x_{i+1})-2f(x_{i})+f(x_{i-1})}{h^2}
\end{align}
$$

Note that this formula can be useful for numerically solving differential equations involving 2nd order derivatives.
1. Use the above difference formula for approximating the solution to the following differential equation with given boundary values on the interval $[0,1]$ for $h = 0.2$.

$$
\begin{align}
y'' = 4x^3, y(0 = 1),y(1) = 2
\end{align}
$$

2. Use the Geogebra and come up with the 3D graph of $f(x,y) = x^2-3xy+2y^3$ on the interval $[-1,1]$ by $[-2,2]$

Solution for #1:

$$
\begin{align}
t_{0}=0 \\
t_{1}=0.2 \\
t_{2}=0.4 \\
t_{3}=0.6 \\
t_{4}=0.8 \\
t_{5}=1
\end{align}
$$

Initial Conditions:
$y(0)=1$
$y(1)=2$

Solve at $4(x_{i})^{3}$

$$
\begin{align}
&\frac{y_{2}-2y_{1}+y_{0}}{h^{2}}=\frac{y_{2}-2y_{1}+1}{0.04}=4(0.2)^{3}=0.0128 \\
&\frac{y_{3}-2y_{2}+y_{1}}{h^{2}}=\frac{y_{3}-2y_{2}+y_{1}}{0.04}=0.012024 \\
&\frac{y_{4}-2y_{3}+y_{2}}{h^{2}}=\frac{y_{4}-2y_{3}+y_{2}}{0.04}=0.03456 \\
&\frac{y_{5}-2y_{4}+y_{3}}{h^{2}}=\frac{y_{5}-2y_{4}+y_{3}}{0.04}=2-2y_{4}+y_{3}=0.08192
\end{align}
$$

setup a systems of equations:

$$
\begin{bmatrix}
0 & 0 & 1 & -2  & -0.99872 \\
0 & 1 & -2 & 1  & 0.01024 \\
1 & -2 &1 & 0 & 0.03465 \\
-2 & 1 & 0 & 0 & -1.91808
\end{bmatrix}
$$

RREF

$$
\begin{align}
&y_{5}=2 \\
&y_{4}=1.709376 \\
&y_{3}=1.500672 \\
&y_{2}=1.326528 \\
&y_{1}=1.162624 \\
&y_{0}=1 \\
\end{align}
$$
