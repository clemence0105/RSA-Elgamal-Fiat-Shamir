#!/usr/bin/env python
#coding: UTF-8

import argparse
import sys
import primes
import random
import bInt.bInt as bInt


def generate_keys(bitlen):
    # 3-е лицо генерирует простые p,q и вычисляет n
    p = primes.getPrime(bitlen)
    q = primes.getPrime(bitlen)
    n = p * q
    # Алиса генерирует s и вычисляет v = s^2
    s = bInt.RandomRange(n-1)
    two = bInt.bInt(2)
    v = bInt.Pow(s, two, n) 

    return (n, v), (n, s)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('key_name')
    return parser.parse_args()     


if __name__ == "__main__":
    args = get_args()  
	
    with open(args.key_name + '_public') as key_file:
        (n, v) = key_file.read().split("\n")
    with open(args.key_name + '_private') as key_file:
        (n, s) = key_file.read().split("\n")
	
    n = bInt.bInt(n)
    s = bInt.bInt(s)
    v = bInt.bInt(v)
	
    t = 5 # 5 раундов аккредитации

    ok = True
    for i in range (t): 
        if ok:
            # Алиса-претендент выбирает случайное число r между 0, и n - 1
            r = bInt.RandomRange(n-1)
	
            # далее она вычисляет значение
            #x = r^2 mod n
            two = bInt.bInt("2")
            x = bInt.Pow(r, two, n)

            # Алиса передает x Бобу.
            # Боб-верификатор передает вызов e Алисе. Значение e равно 0 или 1
            e = bInt.RandomRange(bInt.bInt(2))

            # Алиса вычисляет свой ответ y = r * s^e.
            y = (r * (bInt.Pow(s, e, n))) % n

            # Алиса передает ответ Бобу, показывая что она знает значение 
            # своего секретного ключа s. Подтверждает себя

            # Боб вычисляет y^2 и x * v ^ e. 
            # Если эти два значения являются конгруэнтными, 
            # то для Алисы значение s означает "она честна"
            yy = bInt.Pow(y, two, n)
            xve = (x * (bInt.Pow(v, e, n)) % n)
	
            if yy != xve: 
                ok = False
    
    if ok:
        print "Key accepted" 
    else:
        print "Key rejected" 
