import struct

# Define VM instruction opcodes
OP_PUSH = 0x01
OP_POP = 0x02
OP_ADD = 0x03
OP_SUB = 0x04
OP_CMP = 0x05
OP_JMP = 0x06
OP_PRINT = 0x07
OP_HALT = 0x08
OP_READ = 0x09
OP_FUNK = 0x0a
OP_WIN = 0x0b


# 9 - random.randint(1,7)
# 8 - random.randint(1,6)
# 7 - random.randint(1,5)

import random
def funky(flag_byte):
    # for flag_byte in flag:
    a = ord(flag_byte)
    byte_0 = random.randint(1,7)
    byte_7 = 9 - byte_0

    byte_1 = random.randint(1,6)
    byte_6 = 8 - byte_1

    byte_2 = random.randint(1,5)
    byte_5 = 7 - byte_2

    byte_3 = 0
    byte_4 = a - 9 - 8 - 7

    packed_data = struct.pack('<BBBBBBBB', byte_0, byte_1, byte_2, byte_3, byte_4, byte_5, byte_6, byte_7)
    print(repr(packed_data))
    return packed_data

def create_vm_program(flag):
    # Convert flag into a list of integers (8-byte chunks)
    flag_bytes = flag.encode('utf-8')
    if len(flag_bytes) % 8 != 0:
        # Pad the flag with zero bytes to make its length a multiple of 8
        flag_bytes = flag_bytes.ljust(len(flag_bytes) + (8 - len(flag_bytes) % 8), b'\x00')
    
    program = bytearray()

    # PUSH flag chunks to the VM
    # for chunk in flag_chunks:
    for flag_byte in flag:
        program.extend(struct.pack('<B', OP_PUSH))
        packed_byte = funky(flag_byte)
        program.extend(packed_byte)
        program.extend(struct.pack('<B', OP_READ))
        program.extend(struct.pack('<B', OP_FUNK))

    # Print the flag if comparison is successful
    program.extend(struct.pack('<Q', OP_PRINT))
    
    # Halt the VM
    program.extend(struct.pack('<Q', OP_WIN))
    program.extend(struct.pack('<Q', OP_HALT))

    return bytes(program)

def write_program_to_file(filename, flag):
    program = create_vm_program(flag)
    with open(filename, 'wb') as f:
        f.write(program)

if __name__ == "__main__":
    flag = "pctf{nest3d_vm_s3cr3ts}"
    filename = "vm_program.bin"
    write_program_to_file(filename, flag)
    print(f"VM program written to {filename}")
