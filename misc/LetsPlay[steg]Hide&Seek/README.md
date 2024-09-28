# Let's Play [steg]Hide & Seek

## Description
Not much of a backstory here... there is an embedded flag in here somewhere, your job is to find it.

### Difficulty
7/10

### Hints
1. I mean, the title literally says 'steghide'
2. Perhaps there is more than one layer to the stego?

### Flag
PCTF{QR_M0s41c_St3g0_M4st3r}

### Author
David Morgan (r0m)

### Tester


### Writeup
0. Download the BMP file
1. Create custom script to extract all 1000 QR codes
- Tested on a few major GPTs, none will autosolve
- Each QR code is 290x290px
- Figure out there are 40 QR codes across and 25 down
- Need to build a loop within a loop in the script to carve and save each of the 40 squares before moving to the next line
2. Add to script capability to read each QR and write contents to a dictionary
3. Use steghide to extract next layer (another BMP file)
4. Create script to dictionary attack (one created earlier) against the next layer - the patriotCTF.bmp image has the embedded flag, but must use steghide with password to decrypt and extract it
5. Decode final QR code BMP for the flag
