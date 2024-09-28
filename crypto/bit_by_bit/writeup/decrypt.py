#!/usr/bin/python3
from pwn import make_packer

key = 0xaecd4b13904523ea69bafe00

p = make_packer(128,endianness='Big')
enc = ''
with open("out","r") as file:
	for line in file:
		enc += line
ct = [line[i:i+32] for i in range(0, len(line), 32)]
pt = []

iv=0
for c in ct:
	iv = (iv+1)%255
	k = key+iv
	try:
		pt.append(p(int("0x"+c,16)^k))
	except Exception as e:
		print(e)
		pass

print(b''.join(pt))
