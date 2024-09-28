#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long, inverse
from random import getrandbits
from math import gcd

FLAG = b"pctf{fun_w1th_l4tt1c3s_f039ab9}"

m = bytes_to_long(FLAG)

def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = getrandbits(512)
        if (3*d)**4 > N and gcd(d,phi) == 1:
            e = inverse(d, phi)
            break
    return N,e


N, e = get_huge_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')

with open("dist.txt","w") as f:
    f.write(f'N = {hex(N)}\n')
    f.write(f'e = {hex(e)}\n')
    f.write(f'c = {hex(c)}\n')
