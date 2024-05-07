# -*- coding: utf-8 -*-
"""Sesi04_newton-raphson.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19iumoQVM4cVX5ccjzcAGMlUkIqa_0uty
"""

import numpy as np

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4)) / (f_prime(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))

def my_newton(f, df, x0, tol):
  # output is an estimation of the root of f
  # using the Newton Raphson method
  # recusrsive implementation

  if abs(f(x0)) < tol:
    return x0
  else:
    return my_newton(f, df, x0 - f(x0)/df(x0), tol)

estimate = my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =", np.sqrt(2))

"""Quiz 1 Newton Raphson

f(x) = x^3 - 3x^2 + 2x
  x0 = 1.5
  tol = 0.01

Jawaban Quiz 1
"""

import numpy as np

f_quiz1 = lambda x: x**3 - 3*x**2 + 2*x
f_prime_quiz1 = lambda x: 3*x*2 - 6*x + 2

def my_newton(f, df, x0, tol):
  # output is an estimation of the root of f
  # using the Newton Raphson method
  # recusrsive implementation

  if abs(f(x0)) < tol:
    return x0
  else:
    return my_newton(f,df, x0 - f(x0)/df(x0), tol)

estimate_quiz1 = my_newton(f_quiz1, f_prime_quiz1, 1.5, 0.01)

print("Quiz 1 Newton Rapshon")
print("estimate =", estimate_quiz1)
print("f(estimate) =", f_quiz1(estimate_quiz1))
print("sqrt(2) =", np.sqrt(2))

"""Quiz 2 Newton Raphson

f(x) = e^x - 2x
  x0 = 1
  tol = 0.001

Jawaban Quiz 2
"""

import numpy as np

f_quiz2 = lambda x:np.exp(x) -2*x
f_prime_quiz2 = lambda x: np.exp(x) - 2

def my_newton(f, df, x0, tol):
  # output is an estimation of the root of f
  # using the Newton Raphson method
  # recusrsive implementation

  if abs(f(x0)) < tol:
    return x0
  else:
    return my_newton(f, df, x0 - f(x0)/df(x0), tol)

    estimate_quiz2 = my_newton(f_quiz2, f_prime_quiz2, 1, 0.001)

    print("Quiz 2 Newton Raphson")
    print("estimate =", estimate_quiz2)
    print("f(estimate) =", f_quiz2(estimate_quiz2))
    print("sqrt(2) =", np.sqrt(2))