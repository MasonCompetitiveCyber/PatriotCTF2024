# Green Eggs and Ham

### Description
A disgruntled timekeeper here at Bell Labs recently exfiltrated some data from our network. The crappy network down there might have caused enough errors to make it useless... right?

### Difficulty
6.5/10 (TBD)

### Flag
PCTF{ALL_H4M_NO_CH33$3!}

### Hints
TBD

### Author
Shiloh Smiles (arcticx)

### Tester

### Writeup
1. Extract "greeneggsand.zip" using NetworkMiner (or other tool from the pcap)
2. Extract all following calls to /<two hex digits> into one big string of binary (of note, the binary string is also already present in the data, so this can help make this conversion step a bit easier to guess)
3. You should now have a string of text:
```00001111
01000001
10001111
11000011
01100110
00100101
11000110
10100101
01100110
01000011
11100110
11000011
00001111
00100101
10001111
10100111
00001111
00101010
10001111
10101010
01100110
00100101
11100110
10100101
00101010
01010101
10101010
11010101
00001101
00010000
10001111
10000000
01100110
01101001
11100110
11101001
00001111
01000011
11001111
11000011
00001111
01000011
10001111
11000011
00001111
00001111
10001111
10001111
01100110
01111111
11100110
11111111
00001111
00101010
10001111
10101010
01100110
01001100
11100110
11001100
00101010
01010101
10101010
11010101
01100110
01011010
11010011
11001110
01100011
00010101
11101110
10010010
00011111
01100111
10001010
11111001
01001100
00100000
11001100
10111000
01100100
01101010
11101110
10001110
01001011
01110000
11000111
10000101
01000011
01011111
10100001
10001000
01100100
01100111
11001100
11000011
00100111
01011100
10101101
11101100
01101110
01000111
11011100
11000110
00101101
00000100
11100011
10000111
00001010
01101011
10111010
11101101
01010011
00101110
11100100
11011101
00100110
01101010
11110110
11010111
00100100
01011001
11001011
11000011
```
4. Separate the first digit from the last seven. The seven LSBs are the actual data, the MSB determines if it belongs to password1 or password2.
5. Create a script that does basic Hamming(7,4) code reversal. This is a relatively well-known encoding scheme. There are intentionally errors in the data transmission ensuring that this will need to be implemented correctly.
6. Using the two password, unzip greeneggsand.zip and then ham.zip to reveal flag.jpg
