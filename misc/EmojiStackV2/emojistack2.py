from PIL import Image
import numpy as np
timesub = {"🕛": "0", "🕐": "1", "🕑": "2", "🕒": "3", "🕓": "4", "🕔": "5", "🕕": "6", "🕖": "7", "🕗": "8", "🕘": "9", "🕙": "A", "🕚": "B"}

def clock_to_int(clock_string):
    output = ""
    for clock in clock_string:
        output += timesub[clock]

    return int(output, 12)

def evaluate(code, init_state=None):
    right = "👉"
    left  = "👈"
    up    = "👆"
    down  = "👇"
    add   = "👍"
    sub   = "👎"
    out   = "💬"
    huh   = "👂"
    rep   = "🔁"
    start = "🫸"
    end   = "🫷"
    bracemap = buildbracemap(code)
    codeptr = 0
    cellptr = [0, 0]
    if init_state == None:
        cells = [[0 for x in range(256)] for x in range(256)]

    else:
        cells = init_state
        
    loopctr = 0
    loop = False
    while codeptr < len(code):
        command = code[codeptr]

        
        if command == right:
            cellptr[1] = min(cellptr[1] + 1, 255)
        elif command == left:
            cellptr[1] = max(cellptr[1] - 1, 0)
        elif command == up:
            cellptr[0] = min(cellptr[0] + 1, 255)
        elif command == down:
            cellptr[0] = max(cellptr[0] - 1, 0)
        elif command == add:
            cells[cellptr[0]][cellptr[1]] = min(cells[cellptr[0]][cellptr[1]] + 1, 255)
        elif command == sub:
            cells[cellptr[0]][cellptr[1]] = max(cells[cellptr[0]][cellptr[1]] - 1, 0)
        elif command == out:
            print(chr(cells[cellptr[0]][cellptr[1]]), end="")
        elif command == huh:
            cells[cellptr[0]][cellptr[1]] = ord(input()[0])
        elif command == start and cells[cellptr[0]][cellptr[1]] == 0:
            codeptr = bracemap[codeptr]
        elif command == end and cells[cellptr[0]][cellptr[1]] != 0: 
            codeptr = bracemap[codeptr]
        elif command == rep:
            if loopctr == 0 and not loop:
                loopctr = clock_to_int(code[codeptr+1:codeptr+4])
                loop = True
            if loop == True and loopctr == 0:
                loop = False
            if loop:
                codeptr -= 2
                loopctr -= 1


        codeptr += 1

    return cells

def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "🫸": temp_bracestack.append(position)
        if command == "🫷":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

state = Image.open("turing.png").convert('L')
state_array = []
for y in range(state.height):
    tmp = []
    for x in range(state.width):
        tmp.append(state.getpixel((x, y)))

    state_array.append(tmp)

with open("program.txt", "r") as f:
    out = evaluate(f.read(), state_array)
    Image.fromarray(np.asarray(out, np.uint8), "L").show()