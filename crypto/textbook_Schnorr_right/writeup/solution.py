from sage.all import *
import secrets
import hashlib
from pwn import *
import os
from tqdm import tqdm

# context.log_level = 'debug'
io = connect("127.0.0.1", 1338)

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
r = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
K = GF(p)
a = K(0x0000000000000000000000000000000000000000000000000000000000000000)
b = K(0x0000000000000000000000000000000000000000000000000000000000000007)
E = EllipticCurve(K, (a, b))
G = E(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
E.set_order(r)

io.recvuntil("Public Key: (", timeout=5)
Px = io.recvuntil(" :", timeout=5, drop=True).strip().decode()
Py = io.recvuntil(" : 1)", timeout=5, drop=True).strip().decode()

print("Px:", Px)
print("Py:", Py)

#public keys
P = E(Px,Py)
print(f"P: {P}")

separator = "FF"
payload = "7F7F7F"

io.sendlineafter("Enter separator as a hex value (2 digits):",separator.encode().strip())
io.sendlineafter("Enter 3-letter word 1 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 2 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 3 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 4 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 5 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 6 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 7 as a hex value (6 digits): ",payload.encode().strip())
io.sendlineafter("Enter 3-letter word 8 as a hex value (6 digits): ",payload.encode().strip())


TARGET = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
MESSAGE_OR_MASK = int("7F7F7FFF" * 8, 16)

def compute_hash(target):
    return int(hashlib.sha256(str(target).encode()).hexdigest(), 16) % r  # mod r directly

def verify_sign(s,R_test):
    R_test_str = str(R_test).strip("()")  # Remove the parentheses
    R_test_parts = [part.strip() for part in R_test_str.split(':')]  # Split by ":" and strip any whitespace

    # Convert the extracted parts to integers
    x_R = int(R_test_parts[0])
    y_R = int(R_test_parts[1])
    z_R = int(R_test_parts[2])
    send_x_R = hex(x_R)[2:]
    send_y_R = hex(y_R)[2:]
    send_s = hex(s)[2:]
    
    # Print the extracted x_R and y_R values
    print("x_R:", hex(x_R)[2:])
    print("y_R:", hex(y_R)[2:])
    print("send_s:", hex(s)[2:])

    io.sendlineafter("Enter the x-coordinate of signature R (in hex): ", send_x_R.encode())
    io.sendlineafter("Enter the y-coordinate of signature R (in hex): ", send_y_R.encode())
    io.sendlineafter("Enter signature s (in hex): ", send_s.encode())
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    io.interactive()

def brute_force_signature(P, G):
    print("Brute-forcing to find a valid signature...")
    h = compute_hash(TARGET)
    print(f"h: {h}")
    hP = h * P
    s = secrets.randbelow(r)
    sG = s * G
    
    with tqdm(total=0, unit=' iterations', unit_scale=True) as pbar:
        while True:
            R_test = sG - hP
            # R_test_binary = int(R_test.xy()[0])
            R_test_binary = int(R_test.xy()[0] + R_test.xy()[1])

            if (R_test_binary | MESSAGE_OR_MASK) == TARGET:
                assert s*G - h*P == R_test
                print("Success! Found a valid signature.")
                print(f"s: {s}")
                print(f"R_test: {R_test}")
                verify_sign(s, R_test)
                break
            s = (2*s) % r
            sG = 2*sG
            pbar.update(int(1))

brute_force_signature(P, G)
