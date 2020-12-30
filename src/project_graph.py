# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:15:00 2020

@author: Francisco
"""

import math
import matplotlib.pyplot as plt

def D(t):
    return (20/12*t)%20

#Ka = 0.93758889
#Ket = 0.0693

def dmidt(t,mi):
    return D(t)-0.93758889*mi

def dmidt_after(t,mi):
    return -0.93758889*mi

def dmpdt(mi,mp):
    return 0.93758889*mi-0.0693*mp


def euler(t0,mi0,mp0,h,n):
    t=t0
    mi=mi0
    mp=mp0
    tlist = []
    mplist = []
    i = 0
    while(t<n):
        i+=1
        if i%1000000 == 0:
            print("Euler: "+str(math.trunc((t/n)*100))+"% complete")
        mi+=dmidt(t,mi)*h
        mp+=dmpdt(mi,mp)*h
        t+=h
        tlist.append(t)
        mplist.append(mp)
#        print("i: " + str(i)+ "  mi: " + str(mi)+" mp: " + str(mp))
    while(mp>0.1):
        mi+=(-0.93758889*mi)*h
        mp+=dmpdt(mi,mp)*h
        t+=h
        tlist.append(t)
        mplist.append(mp)
#        print("i: " + str(i)+ "  mi: " + str(mi)+" mp: " + str(mp))
    print("Euler: 100% complete")
    plt.plot(tlist,mplist)


def rungaKuta(t0,mi0,mp0,h, tf):
    t = t0
    mi = mi0
    mp = mp0
    T = []
    MP = []
#    h = (xf-x0)/N
    mil = 0
    mpl = 0
    mia = 0
    mpa = 0

    i = 0
    err = 0
    while(t<tf):
        i+=1
        if i%1000000 == 0:
            print("RK2: "+str(math.trunc((t/tf)*100))+"% complete")
        T.append(t)
        MP.append(mp)
        mil = dmidt(t,mi)
        mpl = dmpdt(mi,mp)
        mia = dmidt(t + h/2, mi + mil * h/2)
        mpa = dmpdt(mi + h/2, mp + mpl * h/2)
        mi += mia * h
        mp += mpa * h
        t += h
    while(t<tf+200):
        T.append(t)
        MP.append(mp)
        mil = dmidt_after(t,mi)
        mia = dmidt_after(t + h/2, mi + mil * h/2)
        mpl = dmpdt(mi,mp)
        mpa = dmpdt(mi + h/2, mp + mpl * h/2)
        mi += mia * h
        mp += mpa * h
        t += h
    T.append(t)
    MP.append(mp)
    print("RK2: 100% complete")
    plt.plot(T,MP)


def runga_kutta_4(t, mi, mp, h, tf):
    T = []
    MP = []
    i=0
    while(t < tf):
        i+=1
        if i%1000000 == 0:
            print("RK4: "+str(math.trunc((t/tf)*100))+"% complete")
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

        mi += deltay_mi
        mp += deltay_mp
        t += h
    while(t < tf+100):
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
    T.append(t)
    MP.append(mp)
    print("RK4: 100% complete")
    plt.plot(T,MP)

#    print("X = %.5f || Y = %.5f" %(x, y))
    return y




rungaKuta(0,0,0,0.1,24*365)
euler(0,0,0,0.1,24*365)
runga_kutta_4(0,0,0,0.1,24*365)