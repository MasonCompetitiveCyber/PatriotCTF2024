# This is not for players to have !!


import itertools
import string

fnames = list(itertools.chain([f"_{i}" for i in range(0, 10)], ['underscore', 'left_curly', 'right_curly'], string.ascii_letters))

signatures = [f"unsigned char {name}(unsigned char c, unsigned char i)" for name in fnames]

# for each function
# generate 2 2x2 matrix consisting of c and i
# mat mul
# det
# return
import random
random.seed(1337)

mat_choices = list(range(0, 256)) + (["c"] * 128) + (["i"] * 128)

l_curl = "{"
r_curl = "}"
for s in signatures:
    lines = ["unsigned char m1[2][2];", "unsigned char m2[2][2];", "unsigned int res[2][2];"]
    for i in range(2):
        for j in range(2):
            lines.append(f"m1[{i}][{j}] = {random.choice(mat_choices)};")
            lines.append(f"m2[{i}][{j}] = {random.choice(mat_choices)};")
    lines.append("mat_mul(m1, m2, res);")
    lines.append("return det_scalar_mod(res);")
    lines = '\n'.join([f"\t{l}" for l in lines])

    print(f"{s}{l_curl}\n{lines}\n{r_curl}")

array ="""
// Array of functions that take a char and int argument
// Only these chars we care about, the rest can be thrown in a default
// _, [0-9a-zA-Z], {, }, 
unsigned char (*schedule[])(unsigned char, unsigned char) = {
"""
# array += ", ".join(fnames)

array += ", ".join("def" for _ in range(0, 48)) + ", "
array += ", ".join([f"_{i}" for i in range(0, 10)])  + ", "
array += ", ".join("def" for _ in range(58, 65)) + ", "
array += ", ".join(string.ascii_uppercase) + ", "
array += ", ".join("def" for _ in range(91, 95)) + ", "
array += "underscore, def, "
array += ", ".join(string.ascii_lowercase) + ", "
array += "left_curly, def, right_curly, def, def"
array += "\n};"

print(array)