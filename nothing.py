import numpy as np
import matplotlib.pyplot as plt

x = np.array ([0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25])
y = np.array([4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891, 8.1662, 9.0250, 9.9742, 11.0232, 12.1825,])

def function1(x, y, x0):
   amount = len(x)
   num = np.zeros((amount, amount))
   num[:, 0] = y
   for j in range(1, amount):
    for i in range(amount - j):
     num[i, j] = (num[i+1, j-1] - num[i, j-1]) / (x[i+j] - x[i])
   zero = 0
   for j in range(amount):
    new_zero = num[0, j]
    for i in range(j):
     new_zero *= (x0 - x[i])
    zero += new_zero
   return zero

def function2(x, y, x0):
   amount = len(x)
   num = np.zeros((amount, amount))
   num[:, 0] = y
   for j in range(1, amount):
    for i in range(amount - j):
     num[i, j] = (num[i+1, j-1] - num[i, j-1]) / (x[i+j] - x[i])
   zero = num[0, 0]
   for j in range(1, amount):
    new_zero = num[0, j]
    for i in range(j):
     new_zero *= (x0 - x[i])
    zero += new_zero
   return zero


x1 = 0.173
x2 = 0.242
y1 = function1(x, y, x1)
y2 = function2(x, y, x2)
print(f"f({x1}) = {y1}")
print(f"f({x2}) = {y2}")


one = np.linspace(np.min(x), np.max(x), 50)
two = np.zeros_like(one)
for i in range(len(one)):
 two[i] = function2(x, y, one[i])
plt.plot(x, y, 'o')
plt.plot(one, two)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()