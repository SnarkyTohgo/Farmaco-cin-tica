
"""
Exemplo:

# formulas de recorrência
def _x1 (x2, x3):
    return (7 - x2 - x3) / 3


def _x2 (x1, x3):
    return (4 - x1 - 2 * x3) / 4


def _x3 (x1, x2):
    return (5 - 2 * x2) / 5

"""


def gaussJacobi (x1, x2, x3, fn1, fn2, fn3):
    prev_x1 = x1
    prev_x2 = x2
    prev_x3 = x3

    # caso o criterio de paragem demore muito
    for i in range (20):
        x1 = fn1(prev_x2, prev_x3)
        x2 = fn2(prev_x1, prev_x3)
        x3 = fn3(prev_x1, prev_x2)

        print ("x1: %f\t x2: %f\t x3: %f\t" % (x1, x2, x3))

        # checar o criterio de paragem
        if (abs (x1 - prev_x1) < 10 ** (-3) and abs (x2 - prev_x2) < 10 ** (-3) and abs (x2 - prev_x2) < 10 ** (-3)):
            break

        # update dos valores anteriores
        prev_x1 = x1
        prev_x2 = x2
        prev_x3 = x3


# gaussJacobi(0, 0, 0, _x1, _x2, _x3)