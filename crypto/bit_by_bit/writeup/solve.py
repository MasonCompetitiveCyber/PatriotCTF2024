from pwn import *

r = remote("localhost",7777)

enc = r.recvall().decode()
chunks = [enc[i:i+6] for i in range(0,len(enc),6)]
commonword = 0x746865 # the

def trydecrypt(key):
    dec = ""
    i = 0
    try:
        while True:
            for chunk in chunks:
                i =(i+1)%255
                curr = int(key,16)+i
                d = hex(int("0x"+str(chunk),16)^curr)[2:].replace(' ','').replace('\n','')
                dec += bytes.fromhex(d).decode('utf-8')
            break
    except Exception as e:
        pass
    return dec

keys = []
i = 0

while True:
    try:
        for x in range(0,255):
            c1 = "0x"+str(chunks[i+x])
            c2 = "0x"+str(chunks[i+255+x])
            potential_pt = (int(c1,16)^int(c2,16))^commonword
            for c in (c1,c2):
                potential_key = hex(int(c,16)^potential_pt)[:-2]+"00"
                if potential_key not in keys:
                    keys.append(potential_key)
        i += 255
    except Exception as e:
        print(e)
        break
keys = list(set(keys))
log.success("Found {} potential keys".format(len(keys)))
for key in keys:
    d = trydecrypt(key)
    if "pctf" in d:
        log.success(d)
