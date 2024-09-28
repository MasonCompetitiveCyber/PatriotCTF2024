import socketserver

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass

def getflag():
	return "pctf{0nly_g00d_r3spons3_1s_n0ne!!}"
