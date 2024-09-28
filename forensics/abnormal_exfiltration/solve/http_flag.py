#!/usr/bin/env python

from scapy.all import *
import random
import sys
import requests
import time

flag = "pctf{abnormal_flags_are_illegal}"

######
'''
PRSF
'''
#######
bin_to_flags = {
	0 : "",
	1 : "R",
	2 : "P",
	3 :  "PR",


}



		

#load_layer("http")

dest = "192.168.237.1"
d_port = 7979
getStr = 'GET / HTTP/1.1'



for i in flag:
	things = format(ord(i), '08b')
	#rint(len(things))
	for x in range(0, len(things), 2):
		#print(things[x: x+2])
		#print(int(things[x: x+2], 2))
		#print(bin_to_flags[int(things[x: x+2], 2)])

		#send junk data to mask
		for t in range(random.randint(25, 51)):
			requests.get('http://192.168.237.1:7979')

		#send flag 2 bits as a time
		flag =  "FS"+ bin_to_flags[int(things[x: x+2], 2)]
		#time.sleep(1)
		syn = IP(dst=dest) / TCP(sport=random.randint(1025,65500), dport=d_port, flags=flag)

		send(syn)

# Send SYN
#syn = IP(dst=dest) / TCP(sport=random.randint(1025,65500), dport=d_port, flags='SF')
#send(syn)


#syn_ack = sr1(syn)


# Send ASK
#out_ack = send(IP(dst=dest) / TCP(dport=d_port, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
#sr1(IP(dst=dest) / TCP(dport=d_port, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='P''A') / getStr)