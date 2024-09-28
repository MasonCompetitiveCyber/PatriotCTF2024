#Unintended solve, requires a bit of guesswork, but makes the challenge considerably easier than originally intended

import subprocess

hexflag = 'a5 39 24 90 a8 a5 88 77 26 e4 3c 14 03 1e ba 3c 7d bb dc d6 aa 90 50 c9 0f aa dd 57 33 e1 a4 c7'.split(' ')

flag = ''
for i in range(len(hexflag)):
    for x in range(51,126):
        result = subprocess.run(
            ['../dist/ai_rnd'],
            input=((flag+chr(x)).encode()),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        output = result.stdout.decode().split(" ")[:-1]
        if output[i] == hexflag[i]:
            flag += chr(x)
            break
    print(flag)

print("Done!")
