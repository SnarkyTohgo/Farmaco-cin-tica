"""
    Diferential Equations
"""


"""
Ecample: 

#RK4 Simples
def dfy(x,y):
    return x**2 + y**2

"""


def runga_kutta_4(x, y, b, h, fn):
    while(x < b-0.0001):
        print("X = %.5f || Y = %.5f" %(x, y))

        delta1 = h*fn(x,y)
        delta2 = h*fn(x + h/2, y + delta1/2)
        delta3 = h*fn(x + h/2, y + delta2/2)
        delta4 = h*fn(x + h, y + delta3)
        deltay = delta1/6 + delta2/3 + delta3/3 + delta4/6

        y += deltay
        x += h

    print("X = %.5f || Y = %.5f" %(x, y))
    return y


"""
Usage: 

runga_kutta_4(0, 0, 1.4, 0.1, dfy)

#Calculo do erro
h = 0.1

print("PARA r1")
r1 = runga_kutta_4(0, 0, 1.4, h/2, dfy)

print("PARA r2")
r2 = runga_kutta_4(0, 0, 1.4, h/4, dfy)

print("PARA r3")
r3 = runga_kutta_4(0, 0, 1.4, h/8, dfy)

qc = (r2 - r1)/(r3 - r2)
err = (r3 - r2)/15
print("ERRO = %.5f || QUOCIENTE = %.5f" %(err, qc))

"""