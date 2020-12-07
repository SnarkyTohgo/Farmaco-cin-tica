"""
    REAl Zeros
"""


"""
Example

# funcoes
def f1(x, y):
    return 2 * x * x - x * y - 5 * x + 1


def f2(x, y):
    return x + 3 * m.log10(x) - y * y


def gx(x, y):  # achando a funcao de x, com f1
    return m.pow((x * y + 5 * x - 1) / 2, 1 / 2)


def gy(x, y):  # achando a funcao y, com f2
    return m.pow(x + 3 * m.log(x), 1 / 2)

"""

import math as m

# Gauss Seil
# Metodo de paragem: erro absoluto
def picard_peano_2_err(x, y, err, gx, gy):
    x = 1
    y = 1

    prev_x = 2
    prev_y = 2

    while (abs(prev_x - x) >= err or abs(prev_y - y) >= err):
        prev_x = x
        prev_y = y
        x = gx(x, y)
        y = gy(prev_x, y)
        print('x: %1.7f\t y:%1.7f\t' % (x, y))


# Metodo de paragem: numero de iterações
def picard_peano_2(x, y, max_iter, gx, gy):
    for i in range(max_iter):
        prev_x = x
        x = gx(x, y)
        y = gy(prev_x, y)
        print('x: %1.7f\t y:%1.7f\t ' % (x, y))


# picard_peano_2(10, 0, 20, gx, gy)
# picard_peano_2_err(10, 0, m.pow(10, -5), gx, gy)