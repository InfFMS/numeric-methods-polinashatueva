#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0
#C точностью до 0.01.

def s(a,b,f,eps):
    while b-a >= 2*eps:
        c = (a+b)/2
        if f(a)*f(b)<=0:
            b = c
        else:
            a = c
    return c

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 3, 400)
y = x**3 -x +1

# Создание подграфиков

fig, axs = plt.subplots()
plt.plot(x, y, label="график x3 – x +1 = y", color="blue")
plt.grid(True)
# Настройка расстояний
plt.tight_layout()
plt.show()
q = 0.01
def f(x):
    y = x ** 3 - x + 1
    return y
print(s(-2,0,f,q))





#x3 – x2 – 9x + 9 = 0
x1 = np.linspace(-5, 5, 400)
y1 = x**3 -x**2 - 9*x +9

# Создание подграфиков

fig1, axs1 = plt.subplots()
plt.plot(x1, y1, label="график x3 – x2 – 9x + 9 = y", color="blue")
plt.grid(True)
# Настройка расстояний
plt.tight_layout()
plt.show()
def s1(a,b,f,eps):
    while b-a >= 2*eps:
        
        c = (a+b)/2
        if f(a)*f(b)<=0:
            b = c
        else:
            a = c
    return c
def f1(x):
    y = x**3 -x**2 - 9*x +9
    return y1
print(s(-4,-2,f1,q))
print(s(0,2,f1,q))
print(s(2,4,f1,q))