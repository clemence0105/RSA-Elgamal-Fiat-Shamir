#!/usr/bin/env python
#coding: UTF-8

import bInt.bInt as bInt
bInt.initRandom() # инициализация генератора больших случайных чисел

# Один шаг теста Миллера-Рабина
def MRstep(a, s, t, n):
    x = bInt.Pow(a, t, n)
    if x == 1:
        return True

    i = 0
    while i < s - 1:
        x = (x * x) % n
        if x == n - 1:
            return True
        i = i + 1

    return x == n - 1

# Тест Миллера-Рабина на простоту числа
def MillerRabin(m):
    t = m - 1
    s = 0
    while t % 2 == 0:
        t /= 2
        s += 1
        
    for repeat in range(20):
        a = 0
        while a == 0:
            a = bInt.RandomRange(m-2)
        if not MRstep(a, s, t, m):
            return False
    return True


# Генерация простого числа заданной длины в битах
def getPrime(bitLen):
    P = bInt.RandomLen(bitLen)
    while not MillerRabin(P):
        P += 1
    return P


# чтение файла как числа
def readBinFile(filename):
    res = bInt.RandomLen(0)
    res.GetNumberFromBinFile(filename)
    return res


# запись числа как бинарный файл
def writeBinFile(filename, n):
   n.SaveNumberInBinFile(filename)
