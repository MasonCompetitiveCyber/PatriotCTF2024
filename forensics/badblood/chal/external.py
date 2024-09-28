import socketserver

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass

def getflag():
	return b"pctf{3v3nt_l0gs_reve4l_al1_a981eb}"
