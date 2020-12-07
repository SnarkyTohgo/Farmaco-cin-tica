"""
    Diferential Equations
"""


"""
Exemple:

def y_l(x,y):
    return x*x+y*y

"""


def runga_kutta_2(x, y, a, b, h, fn):
    while (x < b - 0.01):
        prev_x = x
        x = prev_x + h
        y = y + h*fn(prev_x + h/2, y + h / 2*fn(prev_x, y))

    print(x, y)
    return y


"""
Usage:

runga_kutta_2(0, 0, 0, 1.4, 1, y_1)

r1 = runga_kutta_2(0, 0, 0, 1.4, 0.1, y_l)
r2 = runga_kutta_2(0, 0, 0, 1.4, 0.1/2, y_l)
r3 = runga_kutta_2(0, 0, 0, 1.4, 0.1/4, y_l)

qc = (r2 - r1)/(r3 - r2)
print("quociente = ", qc)
err = (r3 - r2)/3
print("erro", err)

"""