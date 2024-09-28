# GO To Sleep

### Description
My friend always sends me random messages before I go to sleep at night. He got tired of me asking what they meant, so he sent me the program used to make them. 

Flag Format: PCTF{}

### Difficulty
8/10

### Flag
PCTF{whY_4rE_y0U_$t1LL_Aw4k3?!}

### Author
Txnner

### Tester
None

### Writeup
- Search for known strings from running the program (may have to search for hex patterns or encoded strings if the disassembler doesn't detect the strings correctly)
- Follow string traces back until you find a "main" function (no more references). 
- Trace through function calls until you begin to locate encryption. Location can be confirmed with 32 byte hex values (keys) or with strings related to cipher types. (Can also search for "cipher" or "encryption" for similar results, but may be more annoying to find these references)
- Map the data around the encryption function. You will notice two distinct xors being applied to the data before and after encryption.
- Recreate the xor & encryption functions to decode the flag given.
- Nonce size can always be assumed to be 12 bytes due to the way GCM encoding works in GO. ("Randomness" does not matter for this value, other than for obfuscation)
- The first 12 bytes of the message.txt data will be the nonce. This can also be seen in memory while debugging.

For the encryption key values, it is easiest to step through a debugger to see how these values change in memory, as the global offset values make static analysis of this part painful.

- Solver: solve.go
