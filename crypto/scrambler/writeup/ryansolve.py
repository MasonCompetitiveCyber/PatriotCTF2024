import random
import os

# Encrypted file name: encryptedFlag.txt
# Encyrption completed at 2024/08/23 08:45:32


# 20240823084500

time_start = 20240823084532

#while time_start < 20240823084540:

height = 11

print(time_start)
random.seed(time_start)

path = os.path.dirname(os.path.realpath(__file__))
end = f"/encryptedFlag.txt"
path += end
encrypted_file = open(path, "r")

things = list(encrypted_file.read())

#print(len(encrypt))
#print(encrypt)

"""
for i in range(1, 16):
    print(f'{i}: {len(encrypt)/i}')
"""

#newlines remove
encrypt = []
for i in things:
    if i != '\n':
        encrypt.append(i)
    else:
        encrypt.append("l")

#print(len(encrypt))
#print(encrypt)

lines = []
for i in range(0, len(encrypt), 210):
    #print(i)
    lines.append("".join(encrypt[i:i+210]))

#print(lines)

#Org line height
#--------------------------
line_height = []
for i in range(height):
    line_height.append(i)

random.shuffle(line_height)
#print(line_height)


lines_undone = []
for i in range(height):
    #print(lines[line_height.index(i)])
    lines_undone.append(lines[line_height.index(i)])

#print(lines_undone)


#Org line itself
#----------------------------------------------------
for n in range(height):
    
    line_fixy = []

    for i in range(210):
        line_fixy.append(i)

    random.shuffle(line_fixy)
    temp_holder = []
    for x in range(210):
        temp_holder.append(lines_undone[n][line_fixy.index(x)])

    lines_undone[n] = "".join(temp_holder)
    

print(lines_undone)

with open("pls_crack.txt", "a") as helpMe:
    helpMe.write(str(time_start) + "\n")
    for p in lines_undone:
        helpMe.write(p + "\n")
    helpMe.write("\n\n\n")

#input()
encrypted_file.close()

time_start += 1    
