#!/usr/bin/env python
#coding: UTF-8

import argparse
import sys
import primes
import bInt.bInt as bInt

# расширеный алгоритм Евклида
def EuclidExtend(a, b):            
    x1 = bInt.bInt(0)
    x2 = bInt.bInt(1)
    y1 = bInt.bInt(1)
    y2 = bInt.bInt(0)
    
    while b != 0:
        q = a / b
        r = a % b
        a = b
        b = r
        
        xx = x2 - x1 * q
        yy = y2 - y1 * q
        x2 = x1
        x1 = xx
        y2 = y1
        y1 = yy
    x = x2
    y = y2

    return a, x, y

# Решение линейного сравнения ax = 1 mod m
def inverse (a, m):
    d1, x, y = EuclidExtend(a, m)    
    return (x + m) % m


def generate_keys(bitLen):
    p = primes.getPrime(bitLen)
    q = primes.getPrime(bitLen)
    while p == q:
        q = primes.getPrime(bitLen)
        
    n = p * q
    Fi = (p-1) * (q-1)
    e = bInt.bInt(65537)
    d = inverse(e, Fi)

    return (e, n), (d, n)
    

def decrypt(d, n, c):
    return bInt.Pow(c, d, n)


def encrypt(e, n, m):
    if m >= n:
        raise Exception('Choose longer key')
    return bInt.Pow(m, e, n)


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
        try:
            with open(args.key_name + '_public') as key_file:
                (e, n) = key_file.read().split("\n")
        except:
            print "Generate rsa_public!"
            sys.exit(1)
            
        e = bInt.bInt(e)
        n = bInt.bInt(n)
        m = primes.readBinFile(args.input)
        c = encrypt(e, n, m)

        result = str(c)
        with open(args.output, 'w') as out_file:
            out_file.write(result)

    else:
        try:
            with open(args.key_name + '_private') as key_file:
                (d, n) = key_file.read().split("\n")
        except:
            print "Generate rsa_private!"
            sys.exit(1)
            
        with open(args.input) as in_file:
            c = in_file.read()

        d = bInt.bInt(d)
        n = bInt.bInt(n)
        c = bInt.bInt(c)

        m = decrypt(d, n, c,)
        primes.writeBinFile(args.output, m)
