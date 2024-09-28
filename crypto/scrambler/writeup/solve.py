import random as r
import os

key = 20240823084532
r.seed(key)

### NOTE DO NOT DISTRIBUTE
"""DO NOT DISTRIBUTE"""

# path = os.path.dirname(os.path.realpath(__file__))
# end = f"\\testin.txt"
# path += end
# with open(path, "r", encoding="utf=8") as file:
#     lines = file.readlines()
#     for index, char in enumerate(lines):
#         origin[index] = char

#     r.shuffle(lines)
#     for index, line in enumerate(lines):
#             l = list(line)
#             r.shuffle(l)
#             lines[index] = "".join(l)
    
#     path = os.path.dirname(os.path.realpath(__file__))
#     end = f"\\originScrambled.txt"
#     path += end
#     with open(path, "r", encoding="utf=8") as file:
#         #  file.writelines(lines)
#         lines = file.readlines()

#         for index, char in enumerate(lines):
#               originScrambled[index] = char

# path = os.path.dirname(os.path.realpath(__file__))
# end = f"\\encryptedFlag.txt"
# path += end
# with open(path, "r", encoding="utf=8") as file:
#     lines = file.readlines()
#     for index, char in enumerate(lines):
#         flag[index] = char


path = os.path.dirname(os.path.realpath(__file__))
end = f"/flagfix.txt"
path += end
with open(path, "r", encoding="utf=8") as flagscramble:
    flaglines = flagscramble.readlines()

    path = os.path.dirname(os.path.realpath(__file__))
    end = f"/testin.txt"
    path += end
    with open(path, "r", encoding="utf=8") as original:
        originallines = original.readlines()

        path = os.path.dirname(os.path.realpath(__file__))
        end = f"/scramblein.txt"
        path += end
        with open(path, "r", encoding="utf=8") as origscramble:
            scramblelines = origscramble.readlines()

            reconstructed = ""
            for ind, line in enumerate(originallines):
                print(f"ind: {ind}, line: {line}")
                for index, char in enumerate(line):
                    moved = scramblelines[ind].index(char)
                    shouldBe = flaglines[ind][moved]
                    reconstructed += shouldBe
                    print(f"Index: {index}, was originally: {char}, moved to {moved}, should be {shouldBe}")

print(reconstructed)
