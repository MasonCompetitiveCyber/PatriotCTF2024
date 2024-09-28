from pwn import *
import base64

r = remote("localhost",9001)

for i in range(0,1000):
	r.readuntil("Challenge: ")

	# Extract challenge info
	challenge = base64.b64decode(r.readuntil("\n").strip(b'\n')).decode()
	enc = challenge.split('|')[0]
	n = int(challenge.split('|')[1])

	# Create response
	for j in range(0,n):
		enc = base64.b64decode(enc)
	response = enc.decode()+"|"+str(i)

	# Send
	r.readuntil(">> ")
	r.sendline(response)
	log.success(f"Responded to challenge {i}")

r.interactive()
