#Пусть горка имеет форму, которую можно описать формулами
#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1
#На отрезке от 0 до π.
#Найти длину этих горок.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.cos(x)
fig, axs = plt.subplots()
plt.plot(x, y, label="cos x", color="blue")
plt.grid(True)
plt.show()
n = 99
a = (3.14 -0)/n
def f(x):
    y = np.cos(x)
    return y
m = 0
for i in range(99):
    x = a * i + i
    b = ((f(i) - f(i + a))**2 + a **2)**0.5
    m = m +b
print(m)


