from base64 import *
import passwordProtector

### import
prompt = passwordProtector.promptGen()
print("==========================")
print(f'Prompt Generated: {prompt}')
prompt = prompt.replace("Mwahahaha you will n","")
prompt = prompt.replace("ever crack into my pass","")
prompt = prompt.replace("word, i'll even give you the key and the executable", "")
prompt = prompt.replace(" ", "")
print("==========================")
print(f'Fluff removed: {prompt}')

### clean up
parts = prompt.split("::::")
password = parts[0]
key = parts[1]

print("==========================")
print(f'Obscured password: {password}')
print(f'Obscured key: {key}')

### solve starts
# Reverse of simple lambda function
flipFlops = lambda x: chr(ord(x) - 1)

# Reverse using the string
unFourth = ""
for each in password:
    unFourth += flipFlops(each)
print("==========================")
print(f'Un-Lambda\'d string: {unFourth}')

# Un-base64
unThird = b64decode(unFourth)
bittysUnEnc = b64decode(key)
print("==========================")
print(f'Un-base64\'d password: {unThird}')
print(f'Un-base64\'d key: {bittysUnEnc}')

# Un-XOR
unOnePointFive = int.from_bytes(unThird) ^ int.from_bytes(bittysUnEnc)
unSecond = unOnePointFive.to_bytes(len(unThird))
print("==========================")
print(f'Un-XOR\'d: {unSecond}')

unFirst = unSecond.decode('utf-8')

print("==========================")
print(f'Flag: {unFirst}')
print("==========================")