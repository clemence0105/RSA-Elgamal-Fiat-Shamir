#!/usr/bin/env python
#coding: UTF-8

import argparse
import sys
import primes
import random
import bInt.bInt as bInt


def generate_keys(n):
    p = primes.getPrime(n) # Генерируется случайное простое число p длины n битов
    g = bInt.RandomRange(p) # Выбирается случайный элемент g поля Zp.
    x = bInt.RandomRange(p-2) + 1 # Выбирается случайное целое число x такое, что 1 < x < p-1
    y = bInt.Pow(g, x, p) # Вычисляется y = g^x (mod p)
    
    # Открытым ключом является тройка (p,g,y), закрытым ключом — число x
    return (p, g, y), (p, x)


def decrypt(p, x, a, b):
    return (b * bInt.Pow(a, p - 1 - x, p)) % p


def encrypt(p, g, y, m):
    if m >= p:
        raise Exception('Choose longer key')

    # Выбирается сессионный ключ — случайное целое число k такое, что 1 < k < p - 1
    k = bInt.RandomRange(p-2) + 1
    a = bInt.Pow(g, k, p) # Вычисляются числа a = g^k (mod p) и b = y^k * M (mod p)
    b = bInt.Pow(y, k, p)
    b = (b * m) % p
    return a, b # Пара чисел (a, b) является шифротекстом
    

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('key_name')
    parser.add_argument('mode', choices=['e', 'd'], help="e - encrypt, d - decrypt")
    return parser.parse_args()     


if __name__ == "__main__":
    args = get_args()

    if args.mode == 'e':
        with open(args.key_name + '_public') as key_file:
            (p, g, y) = key_file.read().split("\n")
            
        p = bInt.bInt(p)
        g = bInt.bInt(g)
        y = bInt.bInt(y)
        m = primes.readBinFile(args.input)
        a, b = encrypt(p, g, y, m)

        with open(args.output, 'w') as out_file:
            out_file.write(str(a) + "\n")
            out_file.write(str(b))

    else:
        with open(args.key_name + '_private') as key_file:
            (p, x) = key_file.read().split("\n")
            
        with open(args.input) as in_file:
            (a, b) = in_file.read().split("\n")

        p = bInt.bInt(p)
        x = bInt.bInt(x)
        a = bInt.bInt(a)
        b = bInt.bInt(b)

        m = decrypt(p, x, a, b)
        primes.writeBinFile(args.output, m)
