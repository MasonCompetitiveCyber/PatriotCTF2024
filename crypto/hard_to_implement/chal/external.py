import socketserver

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass

def getflag():
	return "pctf{ab8zf58}"
