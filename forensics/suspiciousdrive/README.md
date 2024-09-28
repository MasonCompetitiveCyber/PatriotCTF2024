# Suspicious Drive

### Description
An overseas branch of our company was almost hit by an attack from a well-known ransomeware group, but it seemed their final payload failed. We found a suspicious drive on premises, as well as a common string in our logs: PCTF{d)zn+d$+zqbb!bt+h)!#+if+y)u+z!!!}. Can you help us figure out what this payload might have been?

### Difficulty
2/10

### Flag
PCTF{d0wn_d4_wabb1t_h013_if_y0u_w111}

### Author
Shiloh Smiles (arcticx)

### Tester
- Txnner

### Writeup
0. unzip the file
1. identify the drive as a BashBunny. They have a distinctive structure.
2. Notice the custom language set in the "config.txt" file-- in this case "be" and correlate it to be.json in the languages folder.
3. Correlate the foreign keyboard keypresses to what was pressed on an English keyboard.
4. Associate the characters with the correct character from the English keyboard. You do so by going to be.json, finding the letter in the encoded flag, seeing its corresponding keyboard code, and then seeing what key on the english keyboard would produce that.
5. Profit!
