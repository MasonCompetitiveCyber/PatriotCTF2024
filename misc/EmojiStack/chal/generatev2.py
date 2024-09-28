import random

flag = "CACI{TUR!NG_!5_R011!NG_!N_H!5_GR@V3}"
current_index = 0

def goto_smart(index, curr_index):
    output = ""
    offset = curr_index - index
    if offset == 0:
        return output
    
    elif offset > 0:
        output += "👈"
        if offset > 1:
            output += "🔁" + hex(offset-1)[2:].zfill(2)

    elif offset < 0:
        offset = abs(offset)
        output += "👉"
        if offset > 1:
            output += "🔁" + hex(offset-1)[2:].zfill(2)

    return output

def goto_dumb(index, curr_index):
    output = ""
    offset = curr_index - index

    if offset == 0:
        return output
    
    elif offset > 0:
        output += "👈"*offset

    elif offset < 0:
        offset = abs(offset)
        output += "👉"*offset

    return output

def goto(index, curr_index):
    if random.random() > 0.25:
        return goto_smart(index, curr_index)
    else:
        return goto_dumb(index, curr_index)
    
def add_smart(amount):
    output = "👍"
    if amount > 1:
        output += "🔁" + hex(amount - 1)[2:].zfill(2)

    return output

def add_dumb(amount):
    return "👍" * amount

def add(amount):
    if random.random() > 0.25:
        return add_smart(amount)
    else:
        return add_dumb(amount)
    
def print_index(index, curr_index):
    output = ""
    output += goto(index, curr_index)
    output += "💬"
    output += goto(curr_index, index)
    return output

out = ""
printed = 0
remaining = list(range(len(flag)))
current_index = 0
for i in range(len(flag)):
    choice = random.choice(remaining)
    remaining.remove(choice)
    out += goto(choice, current_index)
    out += add(ord(flag[choice]))
    current_index = choice

for i in range(len(flag)):
    out += goto(i, current_index)
    current_index = i
    out += "💬"

print(out)