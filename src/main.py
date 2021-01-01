import math
import matplotlib.pyplot as plt


'''
Cálculo do Ka - Constante de Absorção:

A constante de absorção é calculada através da equação não linear
    
        Ka*e^(Ka*tmax) - Ke*e^(-Ke*tmax) = 0
        
Assim, usando o método de newton atualiza-se o valor de x(Ka) segundo o valor anterior que 
é guardado na variável x0 e os seus valores da função e da sua derivada, isto até se atingir 
uma precisão pretendida(estar muito perto do 0).
'''

def f(x):
     return x*math.exp(-x*3) - 0.0693*math.exp(-3*0.0693)

def df(x):
    return -3*math.exp(-3*x) + math.exp(-3*x)

def newtonPrecision(x0, precision):
    x = x0
    i = 0
    while abs(f(x)) > precision:
        x = x0 - f(x0)/df(x0)
        x0 = x
        i += 1

        # print(str(i) + " : " + str(x))

    return x



'''

Modelo numérico do comportamento temporal da concentração de Lercanidipina no plasma sanguíneo:

Primeiramente achou-se uma função de administraçao, dente de serra, D(t), correspondente a uma 
toma de 1 comprimido de 20mg de 12 em 12 horas.

De seguida usou-se os métodos de Euler e Runge-Kutta para estudar a variação da massa de fármaco
no sangue, mediante as equações fornecidas pelo sistema de equações diferenciais do modelo 
bicompartimental: 

     • dmidt = D(t) - Ka*Mi
     • dmpdt = Ka*Mi - Ket*mp 

Ka = 0.93758889
Ket = 0.0693

'''


def D(t):
    return (20/12*t) % 20

def dmidt(t, mi):
    return D(t) - 0.93758889*mi

def dmidt_after(t, mi):
    return -0.93758889*mi

def dmpdt(mi,mp):
    return 0.93758889*mi - 0.0693*mp


def euler(t0, mi0, mp0, h, n):
    t = t0
    mi = mi0
    mp = mp0
    tlist = []
    mplist = []
    i = 0

    while t < n:
        i += 1

        if i % 1000000 == 0:
            print("Euler: " + str(math.trunc((t/n)*100)) + "% complete")

        mi += dmidt(t, mi)*h
        mp += dmpdt(mi, mp)*h
        t += h

        tlist.append(t)
        mplist.append(mp)

        print("i: " + str(i) + "  mi: " + str(mi) + " mp: " + str(mp))

    while mp > 0.1:
        mi += (-0.93758889*mi)*h
        mp += dmpdt(mi, mp)*h
        t += h

        tlist.append(t)
        mplist.append(mp)

        print("i: " + str(i) + "  mi: " + str(mi)+" mp: " + str(mp))

    print("Euler: 100% complete")
    plt.plot(tlist, mplist)
    plt.show()


def runge_kutta(t0, mi0, mp0, h, tf):
    t = t0
    mi = mi0
    mp = mp0
    T = []
    MP = []

    # h = (xf - x0)/N
    mil = 0
    mpl = 0
    mia = 0
    mpa = 0

    i = 0
    err = 0

    while t < tf:
        i += 1

        if i % 1000000 == 0:
            print("RK2: " + str(math.trunc((t/tf)*100)) + "% complete")

        T.append(t)
        MP.append(mp)

        mil = dmidt(t, mi)
        mpl = dmpdt(mi, mp)
        mia = dmidt(t + h/2, mi + mil * h/2)
        mpa = dmpdt(mi + h/2, mp + mpl * h/2)

        mi += mia * h
        mp += mpa * h
        t += h

        print("i: " + str(i) + "  mi: " + str(mi) + " mp: " + str(mp))


    while t < tf + 200:
        T.append(t)
        MP.append(mp)

        mil = dmidt_after(t,mi)
        mia = dmidt_after(t + h/2, mi + mil * h/2)
        mpl = dmpdt(mi,mp)
        mpa = dmpdt(mi + h/2, mp + mpl * h/2)

        mi += mia * h
        mp += mpa * h
        t += h

        print("i: " + str(i) + "  mi: " + str(mi) + " mp: " + str(mp))


    T.append(t)
    MP.append(mp)

    print("RK2: 100% complete")
    plt.plot(T, MP)
    plt.show()


def runge_kutta_4(t, mi, mp, h, tf):
    T = []
    MP = []

    pre_mp = 0
    k = 0

    i = 0
    while t < tf:
        i += 1

        if i % 1000000 == 0:
            print("RK4: " + str(math.trunc((t/tf)*100)) + "% complete")

        T.append(t)
        MP.append(mp)

        d1mi = h* dmidt(t,mi)
        d1mp = h* dmpdt(mi,mp)
        d2mi = h*dmidt(t + h/2, mi + d1mi/2)
        d2mp = h*dmpdt(mi + h/2, mp + d1mp/2)
        d3mi = h*dmidt(t + h/2, mi + d2mi/2)
        d3mp = h*dmpdt(mi + h/2, mp + d2mp/2)
        d4mi = h*dmidt(t + h, mi + d3mi)
        d4mp = h*dmpdt(mi + h, mp + d3mp)

        deltay_mi = d1mi/6 + d2mi/3 + d3mi/3 + d4mi/6
        deltay_mp = d1mp/6 + d2mp/3 + d3mp/3 + d4mp/6

        # codigo de calculo de maximos e minimos locais
        if (pre_mp < mp) and (mp > mp + deltay_mp) or (pre_mp > mp) and (mp < mp + deltay_mp):
            if mp > mp + deltay_mp:
                k += 1

            print(f'Toma: {k:d}\nhora: {t:f}, \nconcentracao plasmatica: {mp:f}')
            # print(k, t, mp)

        pre_mp = mp

        mi += deltay_mi
        mp += deltay_mp
        t += h

        print("i: " + str(i) + "  mi: " + str(mi) + " mp: " + str(mp))


    while t < tf + 100:
        T.append(t)
        MP.append(mp)

        d1mi = h* dmidt_after(t,mi)
        d1mp = h* dmpdt(mi,mp)
        d2mi = h*dmidt_after(t + h/2, mi + d1mi/2)
        d2mp = h*dmpdt(mi + h/2, mp + d1mp/2)
        d3mi = h*dmidt_after(t + h/2, mi + d2mi/2)
        d3mp = h*dmpdt(mi + h/2, mp + d2mp/2)
        d4mi = h*dmidt_after(t + h, mi + d3mi)
        d4mp = h*dmpdt(mi + h, mp + d3mp)

        deltay_mi = d1mi/6 + d2mi/3 + d3mi/3 + d4mi/6
        deltay_mp = d1mp/6 + d2mp/3 + d3mp/3 + d4mp/6

        mi += deltay_mi
        mp += deltay_mp
        t += h

        print("i: " + str(i) + "  mi: " + str(mi) + " mp: " + str(mp))


    T.append(t)
    MP.append(mp)

    print("RK4: 100% complete")
    plt.plot(T, MP)
    plt.show()



# Main ---------

def main():
    Ka = newtonPrecision(1, 0.000000000000001)
    print("Ka: ", Ka)

    '''
    Simulação de 365 dias:
        tf = 24*365
        
    Simulação de 15 dias: 
        tf = 24*15
    
    Simulação de 7 dias:
        tf = 24*7
        
    Simulação de 1 dia: 
        tf = 24 
    '''

    print("\nEULER: \n")
    euler (0, 0, 0, 0.1, 24 * 365)
    print("-"*100+"\n")

    print("RK2: \n")
    runge_kutta (0, 0, 0, 0.1, 24 * 365)
    print("-"*100+"\n")

    print("RK4: \n")
    runge_kutta_4 (0, 0, 0, 0.1, 24 * 365)
    print("-"*100+"\n")


main()