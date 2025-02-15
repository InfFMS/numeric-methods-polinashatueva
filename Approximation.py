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

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x ** 3 - x + 1', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График уравнения x ** 3 - x + 1 = 0', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()


def f1(x):
    y1 = x** 3 -x**2 - 9*x + 9
    return y1
y1 = x** 3 -x**2 - 9*x + 9
x1 = np.linspace(-2, 3, 400)
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label='f(x) = x**3 – x**2 – 9x + 9', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f1(x)', fontsize=12)
plt.title('График уравнения  x**3 – x**2 – 9x + 9 = 0', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()


def f2(x):
    y2 = x** 3 -x**2 - 9*x + 9
    return y2
 y2 = x** 3 -x**2 - 9*x + 9
plt.figure(figsize=(10, 6))
plt.plot(x2, y2, label='f(x) = x^2 - exp(x)', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График уравнения x^2 - exp(x) = 0', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()
import math
def f3(x):
    y3 = 5*x - 6*math.log(x,10) - 7
    return y3
y3 = 5*x - 6*math.log(x,10) - 7
plt.figure(figsize=(10, 6))
plt.plot(x3, y3, label='f(x) = 5x – 6ln(x) – 7 ', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График уравнения 5x – 6ln(x) – 7  = 0', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()


def f4(x):
    y4 = math.cos(x) + 2*x - 3
    return y4
y4 = math.cos(x) + 2*x - 3
plt.figure(figsize=(10, 6))
plt.plot(x4, y4, label='f(x) = cos(x) + 2x – 3 ', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График уравнения cos(x) + 2x – 3  = 0', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()