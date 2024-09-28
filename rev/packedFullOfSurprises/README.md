
# Packed Full Of Surprises

### Description
I encrypted a file with a secret flag, but now I can't seem to figure out how to decrypt it, can you help?

Flag Format: PCTF{}

### Difficulty
3/10

### Flag
PCTF{UPX_15_2_3A$y_t0_uNp4cK}

### Author
Txnner

### Tester
None

### Writeup
- Determine packing type either with DIE or just looking through `strings`
- unpack with `upx -d encrypt`
- run solve.py 
