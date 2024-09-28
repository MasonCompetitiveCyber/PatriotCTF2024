# idk cipher

### Description

I spent a couple of hours with ???; now I am the world's best cryptographer!!!

Cipher Text: `REYDBFtaERNSAEZFCF1RXUhJEEoGUgBSRxEGXBUVWlo=`

Please wrap the flag with `pctf{}`.

Hashes for `encode.py`:
sha256 `5e70e43cfd28d703baf431fe54caf5c24e830a2805083f720e18f807652e5e9d`
md5 `11d6a9cd1838490d9b857ba049f10f8e`

### Difficulty
1/10 (Easy)

### Flag
pctf{7f8c72c41ccc5ca11a9c1790861ea9a5}

### Hints

### Author
sans

### Tester


### Writeup

```py
import base64
# Given key
key = 'secretkey'
# Cipher Text (given in the challenge)
encoded_cipher_text = "REYDBFtaERNSAEZFCF1RXUhJEEoGUgBSRxEGXBUVWlo=="
# Remove the base64 encoding
decoded_cipher = base64.b64decode(encoded_cipher_text).decode()
# store first half and the last half of the cipher
f_result = []
b_result = []
for i in range(int(len(decoded_cipher) / 2)):
    c1 = ord(decoded_cipher[2*i])
    c2 = ord(decoded_cipher[2*i + 1])
    decrypted_char_p1 = chr(c1 ^ ord(key[i % len(key)]))
    decrypted_char_p2 = chr(c2 ^ ord(key[i % len(key)]))
    f_result.append(decrypted_char_p1)
    b_result.append(decrypted_char_p2)
b_result.reverse()
original_pt = ''.join(f_result) + ''.join(b_result)
print("Decoded Original Plaintext:", original_pt)
```