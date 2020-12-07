"""
    Integrals
"""


"""
Example: 

import math as m

def f(x):
    return m.sin(x)/(x**2)
    
"""


def simpson(a, b, h, fn):
    total = 0
    n = round(abs((b - a)/h))

    # odd values
    for i in range(1, n, 2):
        total += 4*fn(a + i*h)

    # even values
    for i in range(2, n, 2):
        total += 2*fn(a + i*h)

    # get the first value and last value
    total += fn(a) + fn(a+n*h)
    total *= h/3

    return total


"""
Usage: 

# Calculo da convergencia
print(simpson(m.pi/2, m.pi, m.pi/8), f)

r1 = simpson(m.pi/2, m.pi, m.pi/8, f)
r2 = simpson(m.pi/2, m.pi, m.pi/16, f)
r3 = simpson(m.pi/2, m.pi, m.pi/32, f)
r4 = simpson(m.pi/2, m.pi, m.pi/64, f)

coeficiente = (r3 - r2)/(r4 - r3)

print("r1:", r1)
print("r2:", r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r4 - r3)/15
print("erro:", abs(erro))           # erros sempre em modulo

"""