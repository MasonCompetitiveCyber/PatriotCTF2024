import os
import secrets
from base64 import *

### Learn the good and powerful things in python :) 

def promptGen():
    flipFlops = lambda x: chr(ord(x) + 1)

    with open("topsneaky.txt", "rb" ) as f:
        first = f.read()

    bittys = secrets.token_bytes(len(first))

    onePointFive = int.from_bytes(first) ^ int.from_bytes(bittys)
    second = onePointFive.to_bytes(len(first))

    third = b64encode(second).decode('utf-8')
    bittysEnc = b64encode(bittys).decode('utf-8')

    fourth = ""
    for each in third:
        fourth += flipFlops(each)

    ### God i love fstrings they're so nice
    fifth = f'Mwahahaha you will n{fourth[0:10]}ever crack into my pass{fourth[10:]}word, i\'ll even give you the key and the executable:::: {bittysEnc}'

    return(fifth)

def main():
    print(promptGen())

if __name__ == '__main__':
  main()
  