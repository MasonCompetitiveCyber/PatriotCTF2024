import socketserver

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass
