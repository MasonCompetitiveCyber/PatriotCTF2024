array = ""
inter = ""

with open("input.txt", "rb") as f:
    initial = f.read().decode()

index = 0
for each in initial:
    match each:
        case "🔁":
            to_append = initial[index-1] * int(initial[index+1:index+3], 16)
            inter += to_append
        case _:
            inter += each

    index += 1

index = 0
for each in inter:
    match each:
        case "👍":
            array += "+"
        case "👈":
            array += "<"
        case "👉":
            array += ">"
        case "💬":
            array += "."
        case "🔁":
            to_append = initial[index-1] * int(initial[index+1:index+3], 16)
            array += to_append
        case _:
            pass

    index += 1


print(array)

