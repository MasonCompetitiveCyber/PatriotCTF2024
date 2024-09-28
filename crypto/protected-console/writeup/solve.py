from pwn import *
from paddingoracle import BadPaddingException, PaddingOracle
import json
from Crypto.Cipher import AES

r = remote("chal.competitivecyber.club", 6002)

class PadBuster(PaddingOracle):
    def oracle(self, data):
        while True:
            try:
                r.recvuntil("): ")
                s = data.hex()
                r.sendline(s)
                log.info(s)
                out = r.recvuntil("10000")
                if b"Error!" in out:
                    raise BadPaddingException
                return
            except (socket.error, socket.gaierror, socket.herror, socket.timeout) as e:
                print(str(e))

def flip_to_flag():
    r.readuntil("Example: ")
    eg = r.readuntil(b'\n').strip(b'\n').decode()

    final = eg[:12]

    log.info(eg)

    # char 1
    c1 = eg[:12]
    r.readuntil(": ")
    for i in range(0,0xff):
        c1 = eg[:12] + hex(i).strip('0x') + eg[14:]
        r.sendline(c1)
        out = r.readuntil(": ")
        if b"is not defined" in out:
            key = out[6] ^ i
            log.success("Key for f is "+hex(key))
            final += hex(key ^ ord('f')).strip('0x')
            break
    eg = final+eg[14:]

    # char 2
    c2 = eg[:14]
    for i in range(0,0xff):
        c2 = eg[:14] + hex(i).strip('0x') + eg[16:]
        r.sendline(c2)
        out = r.readuntil(": ")
        if b"is not defined" in out:
            key = out[7] ^ i
            log.success("Key for l is "+hex(key))
            final += hex(key ^ ord('l')).strip('0x')
            break
    eg = final+eg[16:]

    # char 3
    c3 = eg[:16]
    for i in range(0,0xff):
        c3 = eg[:16] + hex(i).strip('0x') + eg[18:]
        r.sendline(c3)
        out = r.readuntil(": ")
        if b"is not defined" in out:
            key = out[8] ^ i
            log.success("Key for a is "+hex(key))
            final += hex(key ^ ord('a')).strip('0x')
            break
    eg = final+eg[18:]

    # char 4
    c4 = eg[:18]
    for i in range(0,0xff):
        c4 = eg[:18] + hex(i).strip('0x') + eg[20:]
        r.sendline(c4)
        out = r.readuntil(": ")
        if b"is not defined" in out:
            key = out[9] ^ i
            log.success("Key for g is "+hex(key))
            final += hex(key ^ ord('g')).strip('0x')
            break
    eg = final+eg[20:]

    log.success(eg)
    r.sendline(eg)
    r.interactive()

if __name__ == '__main__':
    d = {'username':'administrative_user','role':1}
    s = json.dumps(d)

    # Get IV
    r.readuntil("Guest: ")
    iv = bytes.fromhex(r.readuntil(b'\n')[:32].strip(b'\n').decode())

    padbuster = PadBuster()
    encrypted = padbuster.encrypt(s, block_size=AES.block_size, iv=iv)

    admin_token = encrypted.hex()
    log.success("Admin token found: "+admin_token)
    r.recvuntil("): ")
    r.sendline(admin_token)
    flip_to_flag()
