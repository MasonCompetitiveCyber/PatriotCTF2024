class EmojiStack:
    def __init__(self, commands):
        self.commands = commands
        self.stack_index = 0
        self.stack = [0] * 256

    def execute_command(self, command_index):
        right = "👉"
        left  = "👈"
        add   = "👍"
        sub   = "👎"
        out   = "💬"
        rep   = "🔁"
        command = self.commands[command_index]
        if command == right:
            self.stack_index = min(self.stack_index + 1, 255)
        elif command == left:
            self.stack_index = max(self.stack_index - 1, 0)

        elif command == add:
            self.stack[self.stack_index] += 1

        elif command == sub:
            self.stack[self.stack_index] -= 1

        elif command == out:
            print(chr(self.stack[self.stack_index]), end="")

        elif command == rep:
            repeat = int(self.commands[command_index+1:command_index+3], 16)
            for i in range(repeat):
                self.execute_command(command_index-1)

    def run(self):
        for i in range(len(self.commands)):
            self.execute_command(i)

EmojiStack("👍🔁47💬👉👍🔁68💬👉👍🔁20💬").run()

with open("input.txt", "r") as f:
    EmojiStack(f.read()).run()