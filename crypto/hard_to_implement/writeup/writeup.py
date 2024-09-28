#!/usr/bin/python3
from pwn import *
import collections,time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

r = remote("chal.competitivecyber.club",6001)

def send(r,data):
	r.readuntil("/1500) Send challenge > ")
	r.sendline(data)
	r.readuntil("Response > ")
	response = r.readuntil('\n')
	response = [(response[i:i+32]) for i in range(0, len(response), 32)]
	return response[:-1]

# Find padding to make last block == '}padding'
index = 0
data = pad(b'}',16)+(index*b'\x00')
blocks = send(r,data)
while blocks[0] != blocks[-1]:
	index += 1
	data = (pad(b'}',16)+(index*b'\x00'))
	blocks = send(r,data)
log.success("Offset padding of "+str(index))

flag = b''

compareindex = -1
sizesofar = 0
log.info("Starting bruteforce, please wait")
log.info("This will take a while...")
while True:
	if b"pctf{" in flag:
		break
	for i in range(32,127):
		time.sleep(1)
		tmp = chr(i).encode()+flag
		tmp = pad(tmp, 16)+(index*b'\x00')
		blocks = send(r,tmp)
		if blocks[0] == blocks[compareindex]:
			flag = chr(i).encode() + flag
			index += 1
			log.success(flag)
			if len(flag) // 15 > sizesofar:
				compareindex -= 1
				sizesofar = len(flag) // 15
			break

n = r.readuntil("/1500)")
log.success(flag)
log.info(n)
r.close()
