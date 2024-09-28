from scapy.all import *
import time
from random import randint
import urllib.request


flag = "pctf{time_to_live_exfiltration}"


living = []

for num in flag:
	living.append(ord(num))

#print(ttl)

print("Pinging localhost")


ip = "192.168.237.1"
#ip = "localhost"

#Write flag
for num in living:
	send(IP(dst=ip, ttl=(num) )/ICMP())
	#time.sleep(randint(0, 5))

	#Random Data requests
	for i in range(randint(0, 30)):
		urllib.request.urlopen('http://192.168.237.1:52301')


print("END")
