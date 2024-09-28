#!/usr/bin/python3

ciphertext_amt = 4

enc = ''
with open("out","r") as file:
	for line in file:
		enc += line
ct = [line[i:i+32] for i in range(0, len(line), 32)]
ct.pop()

ct_paired = []

n = 0
while True:
	if int(len(ct_paired)/2) == ciphertext_amt:
		n = 9999
	try:
		ct_paired.append(ct[n])
		ct_paired.append(ct[n+255])
	except:
		print("{} multi-pads!".format(int(len(ct_paired)/2)))
		break
	n += 1

with open("ciphertexts.txt","w") as file:
	for ct in ct_paired:
		file.write(ct+'\n')
