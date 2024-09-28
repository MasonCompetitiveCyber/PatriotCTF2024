#! /usr/bin/python3.10
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random
import time

random.seed(int(time.time()))
p, q = getPrime(512, random.randbytes), getPrime(512, random.randbytes)
n = p*q
e = getPrime(512)
phi = (p-1)*(q-1)

assert GCD(e, phi) == 1
d = pow(e, -1, phi)

key = RSA.construct((n, e, d, p, q))
with open("public_key.pem", "wb") as f:
    f.write(key.publickey().export_key("PEM"))

with open("private_key.pem", "wb") as f:
    f.write(key.export_key("PEM"))