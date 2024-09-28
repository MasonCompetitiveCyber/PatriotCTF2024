# VM-ception: Layers of the Lost Byte

You’ve hacked into a mysterious system, only to find yourself inside a virtual machine, within another virtual machine, like stepping into a never-ending hall of mirrors. The first VM interprets the encrypted bytecode, but every instruction gets passed to a deeper layer. As you explore further, each action plunges you deeper into the abyss, where time and logic twist in ways you've never imagined.

Will you escape the infinite virtual prison or succumb to its endless loops? The only way out is through... all the layers.

# Difficulty

8/10 

# Author

Christopher Roberts (caffix)

# Challenge provided files

* vm_program.bin
* vm

# Flag
pctf{nest3d_vm_s3cr3ts}

# Write up

This is a virtual machine within a virtual machine, so the simpliest concept of nested virtualization.

The program processes 8-byte instructions, passing them through two layers of VMs. The first VM is set up as a linked-list containing the byte code of the second one. A lot of nested virtualization does this kind of concept of alternating between a data structure, interpretation, or JITing. (No jitting here.)


## Understanding the Nested VM Structure

Outer VM: This VM takes instructions from the user input file and parses them one by one. It passes each instruction to the inner VM.

Inner VM: The inner VM is responsible for executing the parsed instruction but further obfuscates the input by translating the instructions before performing any actual operations. This translation layer acts as the core complexity of the challenge.

The inner VM performs the majority of the push/pop/comparison interactions. It ends up acting as a stack to push a value and compare it with the user's value. it's super side-channellable and I don't really want to fix that.

## The algorithm

The part that really needs reverseing is the `funky` instruction

```python
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
```

I had fun implementing this part in c, both binja and ghidra give you a really long weird looking function, but the code gets bytes from the outside going in. Once it has all the bytes, every outside layer is added together. Once each layer has a sum, the center two bytes are subtracted by each layer.

I thought about misaligning instructions and doing numbers higher than 0xFF, but we can really escalate the challenge of the problem that way, so I'm trying to keep it to just understanding the two layers to the VM.

```c
    unsigned char byte0 = (a >> 0) & 0xFF;
    unsigned char byte7 = (a >> 56) & 0xFF;

    unsigned char byte1 = (a >> 8) & 0xFF;
    unsigned char byte6 = (a >> 48) & 0xFF;

    unsigned char byte2 = (a >> 0x10) & 0xFF;
    unsigned char byte5 = (a >> 40) & 0xFF;

    unsigned char byte3 = (a >> 0x18) & 0xFF;
    unsigned char byte4 = (a >> 32) & 0xFF;

    uint64_t value = (byte3 + byte4) + (byte0+byte7) + (byte1+byte6) + + (byte2+byte5);
```
