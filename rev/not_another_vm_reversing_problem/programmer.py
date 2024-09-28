import struct
import random

# Opcodes from the C VM
NOP = 0
PUSH = 1
POP = 2
ADD = 3
SUB = 4
MUL = 5
DIV = 6
MOV = 7
PRINT = 8
READ = 9
HALT = 11
COMPARE = 12  # New COMPARE opcode

def encode_instruction(opcode, reg=0, value=0):
    """Encodes an instruction as a 4-byte little-endian value"""
    instruction = (opcode << 24) | (reg << 16) | (value & 0xFFFF)
    return struct.pack('<I', instruction)  # 4-byte instruction in little-endian format

def generate_program():
    """Generates a program buffer that can be parsed by the C VM"""
    buffer = b''
    
    # Push each character of the user input onto the stack
    # for i in range(30):
    flag = "pctf{th1s_vm_pr0blem_was_e4sy}"
    for i in range(len(flag)):
        rand_num = random.randint(0,128)
        flag_byte = ord(flag[i]) + rand_num
        buffer += encode_instruction(PUSH, value=rand_num)  # Push each character to the stack
        buffer += encode_instruction(PUSH, value=flag_byte)  # Push each character to the stack
        buffer += encode_instruction(SUB)
        buffer += encode_instruction(READ, value=30)
    
    # Compare each character
    for i in range(len(flag)):
        buffer += encode_instruction(COMPARE)  # Compare each byte
    
    # If all comparisons pass, print congratulations message
    buffer += encode_instruction(PRINT, value=1000)  # Print "Congratulations!"
    
    # Halt the VM
    buffer += encode_instruction(HALT)
    
    return buffer

def save_program_to_file(filename, program_buffer):
    """Saves the generated program buffer to a binary file"""
    with open(filename, 'wb') as f:
        f.write(program_buffer)

# Generate the program buffer
program_buffer = generate_program()

# Save the buffer to a binary file
save_program_to_file('not_another_vm.prog', program_buffer)

print(f"Program saved to 'not_another_vm.prog', {len(program_buffer)} bytes.")
