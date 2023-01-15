#!/usr/bin/env python3

import math
import sys

data = [27.7, 31.0, 32.7, 34.7, 35.9, 37.4, 38.2, 39.5, 40.3, 42.2, 41.3, \
        40.4, 39.8, 38.7, 36.5, 35.7, 33.4, 29.8, 27.5, 25.2, 24.7, 23.1, \
        22.8, 22.7, 23.6, 24.3, 24.5, 26.7, 27.0, 27.4, 29.8, 29.4, 31.5, \
        29.6, 29.8, 28.9, 28.7, 27.2, 25.7, 26.0, 25.2, 21.6, 20.3, 21.1, \
        20.4, 19.8, 19.1, 19.6, 21.2, 21.0, 21.4, 24.0, 25.5, 25.5, 26.4, \
        29.4, 32.1, 31.4, 32.3, 35.2, 38.3, 36.6, 38.4, 39.9, 40.5, 39.4, \
        39.0, 40.5, 42.1, 38.7, 37.5, 38.1, 36.5, 35.4, -1000, "STOP"]

def helper():
    print("SYNOPSIS\n\t./groundhog period\n\nDESCRIPTION\n\tperiod\tthe number of days defining a period")
def error_gestur():
    print("Error: the number of aguments need to be 1.\nThe only argument need to be an integer or a float\n=> ./groundhog [period]", file=sys.stderr)
    exit(84)

def finalOutput(switch):
    tab = []
    print("Global tendency switched " + str(switch) + " times")
    print(str(switch) + " weirdest values are " + str(tab))

def average(x, periode):
    resMoy = float(0.00)
    for k in x:
        resMoy += float(k)
    return (resMoy / int(periode))

def increaseAverage(tab, i, periode):
    incrsAv = 0.00
    if (i >= int(periode)):
        incrsAv = 1
    else:
        return ("nan")
    return "{:.2f}".format(incrsAv / 2)

def relativeEvolution(tab, i, periode):
    dif = 0
    if (i >= int(periode)):
        x = int(tab[i])
        prevValue = int(tab[i - 1])
        dif = round((x * prevValue) / 100)
    else:
        dif = "nan"

    return str(dif)

def ecartType(tab, moyMobile, periode, i):
    res = 0
    for k in tab:
        k = float(k) - moyMobile
        if (k < 0):
            k * -1
        res += k * k
    res = res / float(periode)
    if (i >= int(periode) - 1):
        res = "{:.2f}".format(math.sqrt(res))
        return res
    else:
        return "nan"

def groundhog(periode):
    tabValue = []
    i = 0
    postValue = 0
    switch = 0
    while (True):
        postValue = data[i]
        tabValue.append(input())
        if (tabValue[i] == "STOP"):
            print(tabValue[i])
            finalOutput(switch)
            break
        display(i, tabValue, periode)
        i += 1

def display(i, tabValue, periode):
    r = relativeEvolution(tabValue, i, periode)
    s = ecartType(tabValue, average(tabValue, periode), periode, i)
    g = increaseAverage(s, i, periode)
    print("g=" + g + "\tr=" + r + "%" + "\ts=" + s)

def main():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == '-h'):
            helper()
            sys.exit(0)
        elif (sys.argv[1] >= '0' and sys.argv[1] <= '9'):
            groundhog(sys.argv[1])
            sys.exit(0)
        else:
            error_gestur()
    else:
        error_gestur()
main()