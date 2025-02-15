# y1 = sin(2x) +1
#y2 = -0.2x**2 +0.5
# [0,3.14]

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, np.pi, 100)
y1 = np.sin(2*x1) + 1
y2 = -0.2*x1**2 +0.5
fig, axs = plt.subplots()
plt.plot(x1, y1, label="y1 = sin(2x) +1", color="blue")
plt.plot(x1, y2, label="y2 = -0.2*x**2 +0.5", color="green")
plt.grid(True)
plt.show()
a = 3.14/99
def f(x):
    y = np.sin(2*x) + 1
    return y
def f1(x):
    y = -0.2*x**2 +0.5
    return y

s1 = 0
w=0
for g in range(99):
    s1 = a * (f(g*a)+f((g+1)*a ))/2
    w = w +s1
print(w)
s2 = 0
q =0
for p in range(99):
    s2 = a * (f1(p*a) + f1((p+1)* a)) / 2
    q= q+s2
print(q)
print(w-q)
