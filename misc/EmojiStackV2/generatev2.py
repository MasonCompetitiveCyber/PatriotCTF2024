import random
from PIL import Image
timesub = {"0": "🕛", "1": "🕐", "2": "🕑", "3": "🕒", "4": "🕓", "5": "🕔", "6": "🕕", "7": "🕖", "8": "🕗", "9": "🕘", "10": "🕙", "11": "🕚"}
flagstring = "👍👍🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👍👍👍👍👍👍👍💬👎👎👎👎👎👎👎🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉🫸👎👈👍👈👍👉👉🫷👈👈💬👉🫸👎👈👎👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👍👈🫷👉🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈👍💬👎💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍👍👍🫸👎👈👍👈👍👉👉🫷👈👈💬👉🫸👎👈👎👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👎👎👎👎👎👎👎💬👍👍👍👍👍👍👍👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈💬🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👉👍👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👍👈🫷👉👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👍👈🫷👉👍👍👍👍👍🫸👎👈👍👈👎👉👉🫷👈👈💬👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈👉👍👍👍👍👍👍👍👍👍👍🫸👎👉👍👈🫷👉👍👍👍👍🫸👎👈👍👈👍👉👉🫷👈👈💬👉🫸👎👈👎👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈🫸👎👎👉👍👈🫷👉🫸👎👈👍👉🫷👈👍👍💬👎👎"
def clocks_to_int(clock_string):
    output = ""
    for clock in clock_string:
        output += timesub[clock]

    return int(output, 12)

def int_to_clocks(i):
    out = ""
    while i != 0:
        out += timesub[str(i % 12)]
        i = i//12

    out += "🕛" * (3 - len(out))
    return out[::-1]

class StackGen:
    def __init__(self, state=None):
        self.curr_index = (0, 0)
        self.program = ""
        if state != None:
            self.state = state

        else:
            self.state = [[0 for x in range(256)] for x in range(256)]
        
    def goto(self, index):
        x_diff = self.curr_index[1]-index[1]
        y_diff = self.curr_index[0]-index[0]
        if x_diff > 0:
            self.program += "👈"
            if x_diff > 1:
                self.program += "🔁" + int_to_clocks(x_diff-1)

        elif x_diff < 0:
            x_diff = abs(x_diff)
            self.program += "👉"
            if x_diff > 1:
                self.program += "🔁" + int_to_clocks(x_diff-1)

        if y_diff > 0:
            self.program += "👇"
            if y_diff > 1:
                self.program += "🔁" + int_to_clocks(y_diff-1)

        elif y_diff < 0:
            y_diff = abs(y_diff)
            self.program += "👆"
            if y_diff > 1:
                self.program += "🔁" + int_to_clocks(y_diff-1)

        self.curr_index = index

    def set_cell(self, index, value):
        self.goto(index)
        diff = self.state[index[0]][index[1]] - value
        if diff > 0:
            if diff > 10:
                self.program += "👎"
                if diff > 0:
                    self.program += "🔁" + int_to_clocks(diff-1)
            else:
                self.program += "👎"*diff

        elif diff < 0:
            diff = abs(diff)
            if diff > 10:
                self.program += "👍"
                if diff > 0:
                    self.program += "🔁" + int_to_clocks(diff-1)
            else:
                self.program += "👍"*diff

    def print_cell(self, index):
        self.goto(index)
        self.program += "💬"
    
    def write_state(self, arr):
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                if arr[row][col] > 0:
                    self.set_cell((row, col), arr[row][col])
                
                if row == 125 and col == 120:
                    self.set_cell((0, 0), 0)
                    self.set_cell((0, 1), 0)
                    self.set_cell((0, 2), 0)
                    self.goto((0, 0))
                    self.program += flagstring


        return self.program



turing = Image.open("turing.png").convert('L')
flag = Image.open("flag.png").convert('L')

new_arr = []
for y in range(turing.height):
    tmp = []
    for x in range(turing.width):
        tmp.append(turing.getpixel((x, y)))

    new_arr.append(tmp)

stack = StackGen(new_arr)
new_arr = []
for y in range(flag.height):
    tmp = []
    for x in range(flag.width):
        tmp.append(flag.getpixel((x, y)))

    new_arr.append(tmp)

with open("program.txt", "w") as f:
    f.write(stack.write_state(new_arr))