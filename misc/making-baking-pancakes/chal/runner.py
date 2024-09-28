#!/usr/bin/python3

from Crypto.Random import get_random_bytes
from external import *
import socketserver, signal, base64, time, random


listen = 1337
quota = 1000
flag = "pctf{store_bought_pancake_batter_fa82370}"

def genchall():
	a = get_random_bytes(16).hex().encode('ascii')
	p = a
	r = random.randint(1,15)
	for i in range(0,r):
		p = base64.b64encode(p)
	return (base64.b64encode(p+b'|'+str(r).encode()),a)

def serve(req):
	req.sendall(b"Welcome to the pancake shop!\nPancakes have layers, we need you to get through them all to get our secret pancake mix formula.\nThis server will require you to complete "+str(quota).encode()+b" challenge-responses.\nA response can be created by doing the following:\n1. Base64 decoding the challenge once (will output (encoded|n))\n2. Decoding the challenge n more times.\n3. Send (decoded|current challenge iteration)\nExample response for challenge 485/1000: e9208047e544312e6eac685e4e1f7e20|485\nGood luck!\n\n")
	n = 0
	while n < quota:
		cr = genchall()
		req.sendall(b'Challenge: '+cr[0]+b'\n('+str.encode(str(n))+b'/'+str.encode(str(quota))+b') >> ')
		now = time.time()
		ans = req.recv(4096).strip(b'\n')
		if int(time.time()-now) > 5:
			req.sendall(b"Sorry, you took too long to respond!\nNo recipe for you!!\n")
			return
		elif ans==(cr[1]+b'|'+str(n).encode()):
			pass
		else:
			req.sendall(b"Incorrect response!\nNo recipe for you!!\n")
			return
		n += 1
	req.sendall(b"Wow you did it, you've earned our formula!\nDO NOT SHARE:\n")
	req.sendall(flag.encode()+b"\n")

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		signal.alarm(1500)
		self.request.settimeout(60)
		req = self.request
		serve(req)

def main():
	socketserver.TCPServer.allow_reuse_address = True
	server = ReusableTCPServer(("0.0.0.0", listen), incoming)
	server.serve_forever()

if __name__ == "__main__":
	main()
