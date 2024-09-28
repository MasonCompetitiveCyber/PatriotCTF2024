# Transformation used is relative to the byte
# each byte does not depend on other bytes
# it is dependent on the position though

import os
import string
import pickle
import itertools

# pip install binocular
# pip install unicorn

# I hope i dont get too much heat for using a package I developed
# to write this solve script
# All im doing is getting the address and bytes of all the functions I'm interested in.
# You could use pwntools + some code and do the same thing
from binocular import Ghidra

from unicorn import *
from unicorn.x86_const import *

if not Ghidra.is_installed():
    Ghidra.install()

bin_path = "../dist/ai_rnd"

# We are going to emulate each function for each position
def generate_mappings():
    trans_names = ["def", "underscore", "left_curly", "right_curly"] + [f"_{i}" for i in range(0, 10)] + list(string.ascii_letters)
    transformers = dict()
    data2transformer = dict()
    mu = Uc(UC_ARCH_X86, UC_MODE_64)

    # setup stack space
    stack_base = 0x7fffffffd000
    mu.mem_map(stack_base, 1024*1024*4)

    # debug
    # mu.hook_add(UC_HOOK_CODE, lambda *a: print(hex(mu.reg_read(UC_X86_REG_RIP))))

    # calling convention
    arg1 = UC_X86_REG_RDI
    arg2 = UC_X86_REG_RSI

    # load up binary in Ghidra

    with Ghidra(save_on_close=True) as g:
        g.load(bin_path)
        b = g.binary

        # mem map instructions
        # round the size of the elf up to the nearest 4KB
        # This for sure has enough space
        space_size = len(b)//4096
        space_size += 1
        space_size *= 4096
        mu.mem_map(b.base_addr, space_size)
        

        # Map each function we care about in memory
        mat_mul = g.function_sym("mat_mul")
        mu.mem_write(mat_mul.address, bytes(mat_mul))

        det_scalar_mod = g.function_sym("det_scalar_mod")
        mu.mem_write(det_scalar_mod.address, bytes(det_scalar_mod))

        for fname in trans_names:
            f = g.function_sym(fname)
            
            print(f"Write {fname} to {hex(f.address)}")
            mu.mem_write(f.address, bytes(f))
            transformers[fname] = f

            if fname.startswith('_'):
                data2transformer[ord(fname[1])] = f
            elif fname == "underscore":
                data2transformer[ord("_")] = f
            elif fname == "left_curly":
                data2transformer[ord("{")] = f
            elif fname == "right_curly":
                data2transformer[ord("}")] = f
            elif fname == "def":
                continue
            else:
                data2transformer[ord(fname)] = f


    # For each position
    # For each ascii byte
    # emulate the transformation and save it (4096 combinations)
    inverse = dict()

    for i in range(32):
        for c in range(128):
            print(c, i)

            # function we want to execute
            transformer = data2transformer.get(c, transformers['def'])

            # Address to execute at
            start = transformer.address

            # Address to stop execution. i.e. the address of RET
            end = None
            for bb in transformer.end:
                if bb.instructions[-1].asm == "RET":
                    end = bb.instructions[-1].address
            if end is None:
                raise Exception("could not find RET in function")
            print(f"Excuting {transformer.names[0]}: {hex(start)} -> {hex(end)}")

            # Reset the stack
            mu.reg_write(UC_X86_REG_RSP, stack_base + 1024)

            # Set the Parameters
            # ascii byte is the first param
            # index is the second param
            mu.reg_write(arg1, c)
            mu.reg_write(arg2, i)

            mu.emu_start(start, end)
         

            # return value (return type is a char)
            ret = mu.reg_read(UC_X86_REG_RAX) & 0xFF

            preimages = inverse.get(ret, None)
            if preimages is None:
                inverse[ret] = set()
                preimages = inverse[ret]
            preimages.add((c, i))
            
    
    with open("inverse.pickle", 'wb') as f:
        pickle.dump(inverse, f)
    
    return inverse


if not os.path.exists("inverse.pickle"):
    inverse = generate_mappings()
else:
    with open("inverse.pickle", 'rb') as f:
        inverse = pickle.load(f)

# Reconstruct the input was based on the output
with open("../dist/random_numbers.txt", 'r') as f:
    numbers = f.read().strip()
numbers = [int(n, 16) for n in numbers.split()]

# Do a reverse lookup based on each n in numbers and filter out by the index
# also filter out by printable
combos = list()
for i in range(len(numbers)):
    possibles = [c for c, j in inverse[numbers[i]] if j == i and c > 31 and c < 127]
    # uncomment this to see the possible chars for each position
    # print(" ".join([chr(c) for c in possibles]))
    combos.append(possibles)


# since it starts with pctf{ we can skip the first 5
# right curly brace } is present at the 19th index (when we print out combos) so we chop it off there
combos = combos[5:18]
for candidate in itertools.product(*combos):
    flag = "".join([chr(f) for f in candidate])
    print(flag)
    
# Only 120 possible flags to go through manually