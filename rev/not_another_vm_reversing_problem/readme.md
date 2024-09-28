# Not another vm reversing problem

You find yourself locked out of a mysterious terminal in an underground lair that’s rumored to hold the key to a treasure of unimaginable value: the flag. The terminal is powered by an ancient, quirky virtual machine that hasn't been updated since the days of dial-up internet. Your task is simple... on the surface.

This VM is no ordinary one. It’s got an arcane stack-based architecture, four registers that feel like they've seen better days, and 16KB of memory that’s probably still running on hopes and dreams. But here’s the twist: the terminal was built by a paranoid genius who coded a secret message—hidden deep within the memory—wrapped in layers of logic more convoluted than the plot of a sci-fi novel.


# Difficulty

4/10 

# Author

Christopher Roberts (caffix)

# Challenge provided files

* not_another_vm.program
* vm

# Flag
pctf{th1s_vm_pr0blem_was_e4sy}

# Write up

It's a VM reversing problem, which is most of the difficulty.

The program is a very simple stack based VM that pushes characters to a stack and compares them to values read in the from the user onto the stack.

The algorithm is:
```
for character in flag:
    push(character + random_number)
    push(random_number)
    sub(character - random_number)
    read_char_to_stack()
    compare(pop(), pop())
```
it's a one-way add for the actual algo, so it's not too bad.