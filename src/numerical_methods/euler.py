"""
    Diferential Equations
"""

"""
Example: 

def (x,y):
    return x**2 + y**2
    
"""

def Euler(x, y, a, b, h, fn):
    while (x < b - 0.001):
        prev_x = x
        x = prev_x + h
        y = y + h*fn(prev_x, y)

    print("x:", x)
    return y

"""
Usage: 

# Calculando o erro
h = 0.1

r1 = Euler(0, 0, 0, 1.4, 0.1, y_l)
r2 = Euler(0, 0, 0, 1.4, 0.1/2, y_l)
r3 = Euler(0, 0, 0, 1.4, 0.1/4, y_l)
r4 = Euler(0, 0, 0, 1.4, 0.1/8, y_l)

print("y1:", r1)
print("y2:", r2)
print("y3:", r3)

qc = (r3 - r2)/(r4 - r3)                # o passo é adequado, quociente igual a 2(ou quase)
err = (r4 - r3)
print("quociente", qc)
print("erro:", err)

"""
