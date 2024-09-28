import os
import time
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random

# Load public key
with open("public_key.pem", "rb") as f:
    key = RSA.import_key(f.read())

# Grab public key creation time
ctime = int(os.stat("public_key.pem").st_mtime)

# Load encrypted file
with open("flag.enc", "rb") as f:
    ct = bytes_to_long(f.read())

# Brute force p and q from surrounding time values
delta = 10
for i in range(ctime - delta, ctime + delta):
    random.seed(i)
    p, q = getPrime(512, random.randbytes), getPrime(512, random.randbytes)
    e = key.e
    d = pow(e, -1, (p-1)*(q-1))
    m = long_to_bytes(pow(ct, d, p*q))
    if b"CACI" in m:
        print(m[m.index(b"CACI"):].decode())
        break
