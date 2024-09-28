Challenge Name
Textbook Schnorr right??

Description
Forge your way through cryptographic deception and impersonate with precision in this challenge!

Difficulty
8/10

Flag
```PCTF{F33l_th3_d1ff3r3nc3_b3tw33n_c0nc@t_||_b1tw1s3_OR_|_1n_Pyth0n}```

Hints
None

Author
C15C01337

Tester
Biplav

Writeup

Problem Overview:
The provided Schnorr signature implementation mistakenly uses the bitwise OR (|) operator instead of concatenation (||) when computing the hash of the r value and the message. This introduces a vulnerability that allows for existential forgery, enabling us to bypass signature verification by crafting a specific message.

Key Vulnerability:
In the function:

```h = compute_hash(Ri | message)```
The | operator performs a bitwise OR instead of concatenating the Ri and message. By exploiting this, we can craft a message where all the bits are set to 1 when combined with Ri via the OR operation.

Steps for Exploiting the Flaw:
1. Target the OR Operation:
The goal is to craft a message such that ```Ri | message``` results in all bits being set to 1. This can be achieved by carefully constructing a message in such a way that the OR operation yields the desired result (i.e., all 255 bits set to 1).

2. Message Crafting:
Construct a message where, when combined with Ri via the OR operation, it forces all bits to 1. But, there is strict ascii check while adding a every 3 byte. Can used the DEL ``` 0x7F```  can be done by ensuring that the message contains ascii characters that align with Ri in the right bit positions.

3.Generate a Forged Signature:
Use the faulty ```Ri | message``` hash function to sign this custom message, which will allow you to generate a valid signature.

4. Bypass Verification:
Use the valid signature and forged message to bypass the Schnorr verification mechanism, which fails due to the flawed hashing logic.

5. Conclusion:
By exploiting the improper use of the OR operator, we can successfully forge a valid signature for any message, resultant got a flag.


Running the challenge
```docker build -t Schnorr .```
```docker run -it -dp 6003:1337 Schnorr```
