# High Roller - CACI
## Description
We recieved word that a criminal APT had developed their own method for generating secure asymmetric encryption keys. We were able to intercept emails between the group including encrypted comms, and a 7zip file. All we managed to find in the 7zip file they sent out was their public key, and the key generator. Can you decrypt the comms?

## Difficulty
6/10

## Author
Matthew Johnson (meatball5201)

## Flag
CACI{T!ME_T0_S33D}

## Solution
MUST BE DONE UNDER LINUX, WINDOWS CTIME IS BROKEN AND INCLUDES DST

In the generator script, we can see that the random function used by the getPrime function is seeded with the time in seconds that the script is run. Alone, this wouldn't be enough, but because the APT provided a 7zip file, which preserves modification time stamp, we are able to brute force a range of time stamps around the output creation date. Python3 also changed its random function part way through 3, so the /usr/python3.10 is a hint that it uses the updated random generator function.
An example is found in solve.py
Solve instructions:

`7z x gen_setup.7z`
`python3 solve.py`
