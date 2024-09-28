#!/usr/bin/python3

from external import *
import socketserver, signal

listen = 1337
flag = getflag()

def checkanswer(req, correct):
	ans = req.recv(4096).strip(b'\n').decode().lower()
	if ans == correct.lower():
		req.sendall(b"That makes sense.\n")
		return True
	else:
		req.sendall(b"That can't be right...\n")
		return False

def serve(req):
	req.sendall(b"Welcome analyst.\nWe recently had to terminate an employee due to a department-cut.\nOne of our most dramatic terminations was that of a C-suite executive, Jack Stoneturf.\nWe believe he may have maliciously infected his workstation to maintain persistence on the corporate network.\nPlease view the provided event logs and help us conduct our investigation.\n\n\nAnswer the following questions for the flag:")

	req.sendall(b"\nQ1. Forensics found post exploitation activity present on system, network and security event logs. What post-exploitation script did the attacker run to conduct this activity?")
	req.sendall(b"\n	Example answer: PowerView.ps1\n>> ")
	if not checkanswer(req,"Invoke-P0wnedshell.ps1"):
		return

	req.sendall(b"\nQ2. Forensics could not find any malicious processes on the system. However, network traffic indicates a callback was still made from his system to a device outside the network. We believe jack used process injection to facilitate this. What script helped him accomplish this?")
	req.sendall(b"\n        Example answer: Inject.ps1\n>> ")
	if not checkanswer(req,"Invoke-UrbanBishop.ps1"):
		return

	req.sendall(b"\nQ3. We believe Jack attempted to establish multiple methods of persistence. What windows protocol did Jack attempt to abuse to create persistence?")
	req.sendall(b"\n        Example answer: ProtoName\n>> ")
	if not checkanswer(req,"WinRM"):
		return

	req.sendall(b"\nQ4. Network evidence suggest Jack established connection to a C2 server. What C2 framework is jack using?")
	req.sendall(b"\n        Example answer: C2Name\n>> ")
	if not checkanswer(req,"Covenant"):
		return

	req.sendall(b"\nThat'll do. Thanks for your help, here's a flag for your troubles.\n")
	req.sendall(flag)
	req.sendall(b"\n")

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		signal.alarm(1500)
		self.request.settimeout(400)
		req = self.request
		serve(req)

def main():
	socketserver.TCPServer.allow_reuse_address = True
	server = ReusableTCPServer(("0.0.0.0", listen), incoming)
	server.serve_forever()

if __name__ == "__main__":
	main()
