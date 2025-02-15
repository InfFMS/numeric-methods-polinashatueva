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


x1 = np.linspace(-20, 15, 400)
y1 = x1**3 - x1**2 - 9*x1 + 9


plt.plot(x1, y1, label="y1 = x**3 - x**2 - 9*x + 9 ", color="blue")
plt.grid(True)
# Настройка расстояний
plt.tight_layout()
plt.show()
q = 0.01
def f(x):
    y = x**3 - x**2 - 9*x + 9
    return y
print(s(-3,0,f,q))
print(s(0,3,f,q))

