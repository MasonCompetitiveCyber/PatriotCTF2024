#####################################################
### Partial Source
#####################################################
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import os
from datetime import datetime
import random

# safe key, trust
key = '00000000000000000000000000000000' 

def gen_offset():
    super_safe_seed = int(datetime.utcnow().timestamp())
    random.seed(super_safe_seed)
    return random.randint(1000,2000)

def encrypt(raw):
    raw = pad(raw,16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return cipher.encrypt(raw)

def decrypt(enc):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc),16)

#####################################################
### Generate
#####################################################

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}\\flag_source.png", "rb") as f:
    data = f.read()

offset = 256 * gen_offset()

data1 = data[:offset]
data2 = data[offset:]

with open(f"{dir_path}\\melting.png", "wb") as f:
    f.write(data1 + encrypt(data2))

#####################################################
### Solve
#####################################################

with open(f"{dir_path}\\melting.png", "rb") as f:
    data_to_decrypt = f.read()

### reverse engineer the offset
data1_decrypt = data_to_decrypt[:offset]
data2_decrypt = data_to_decrypt[offset:]

with open(f"{dir_path}\\flag_decrypted.png", "wb") as f:
    f.write(data1_decrypt + decrypt(data2_decrypt))
