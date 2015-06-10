#!/usr/bin/env python
#coding: UTF-8

import rsa
import elgamal
import f_s

def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=['rsa', 'elgamal', 'f_s'])
    parser.add_argument('bit_lenght', choices=['128', '256', '512', '1024', '2048'])
    parser.add_argument('key_name')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    bitLen = int(args.bit_lenght)
    if args.type == 'rsa':
        (e, n), (d, n) = rsa.generate_keys(bitLen)
        with open(args.key_name + '_public', 'w') as p:
            p.write(str(e) + "\n")
            p.write(str(n))
        with open(args.key_name + '_private', 'w') as p:
            p.write(str(d) + "\n")
            p.write(str(n))
        print "keys {0}_public and {0}_private {1} succesfully generated".format(args.key_name, bitLen)

    if args.type == 'elgamal':
        (p, g, y), (p, x) = elgamal.generate_keys(bitLen)
        with open(args.key_name + '_public', 'w') as f:
            f.write(str(p) + "\n")
            f.write(str(g) + "\n")
            f.write(str(y))
        with open(args.key_name + '_private', 'w') as f:
            f.write(str(p) + "\n")
            f.write(str(x))
        print "keys {0}_public and {0}_private {1} succesfully generated".format(args.key_name, bitLen)

    if args.type == 'f_s':
        (n, v), (n, s) = f_s.generate_keys(bitLen)
        with open(args.key_name + '_public', 'w') as f:
            f.write(str(n) + "\n")
            f.write(str(v))
        with open(args.key_name + '_private', 'w') as f:
            f.write(str(n) + "\n")
            f.write(str(s))
        print "keys {0}_public and {0}_private {1} succesfully generated".format(args.key_name, bitLen)
        
