# -*- coding: utf-8 -*-
"""2702350075-AnnisaLuthfiahRahmah-Euler-Method.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vvN9FAlyZf0FS4OJLu9Xm2ENqOienQNy
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
# %matplotlib inline

# Define parameters
f = lambda t, s:np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h)
s0 = -1 # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
  s[i + 1] = s[i] + h*f(t[i] , s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \ for simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

h = 0.01 # Step size
t = np.arange(0, 1 + h, h)
s0 = -1 # Initial Condition

# Explicit Euler Methode
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \ for simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

"""Quiz 1

y' + 4y = x^2
y(0) = 1
"""

f = lambda x, y: x**2 - 4*y #ODE
h = 0.1 # Step Size
t = np.arange(0, 1 + h, h)
y0 = 1 # Initial condition

y = np.zeros(len(t))
y[0] = y0

for i in range(0, len(t) - 1):
  y[i + 1] = y[i] + h*f(t[i] , y[i])

y_exact = (31/32) * np.exp(-4*t) + (1/4) * t**2 - (1/8) * t + (1/32)

plt.figure(figsize = (12, 8))
plt.plot(t, y, 'bo--', label='Approximate')
plt.plot(t, y_exact, 'g', label='Exact')
plt.title('Approximate and Exact Solution \ for simple ODE')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

"""Quiz 2

y'= sin y y(0) = 1

from x = 0 to 0.5 in steps of h = 0.1. Keep four decimal places in the computations
"""

f = lambda x, y: np.sin(y) #ODE
h = 0.1 # Step Size
t = np.arange(0, 0.5 + h, h)
y0 = 1 # Initial condition

y = np.zeros(len(t))
y[0] = y0

for i in range(0, len(t) - 1):
  y[i + 1] = y[i] + h*f(t[i] , y[i])

exact_solution = lambda y: np.log(1 / np.sin(y) - 1 / np.tan(y)) + 0.604582
y_exact = np.linspace(y0, np.max(y), 100)
x_exact = exact_solution(y_exact)

plt.figure(figsize = (12, 8))
plt.plot(t, y, 'bo--', label='Approximate')
plt.plot(x_exact, y_exact, 'g', label='Exact')
plt.title('Approximate and Exact Solution \ for simple ODE')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()