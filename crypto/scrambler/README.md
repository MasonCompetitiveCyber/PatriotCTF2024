# title
Scrambler V2

# category
Crypto

# difficulity


# author
Salochi

# discord
salochi

# flag
pctf{n0t_s0_1mpo55ibl3}

# description
I got sick of people breaking our encryption, so I came up with this custom scrambler program. You have a 0% chance of cracking this one! I even encoded the log!

# Author
Salochi

# Writeup
Use Base64 to decode the encLog.txt file.
From here we can see the timestamp that was used as a seed to shuffle the flag file.
When doing the following steps below, make sure to set up random.seed using this timestamp integer.
You can see the exact format of how to use the timestamp by looking at the scrambler's code

Figure out the original length of each line before the newlines messed it up
This can be done by adding up the length of each line and dividing by number of line
2311 / 12 = 192.583, this does not make sense because you cant have .58 of a character
2311 / 11 = 210.09 this is the correct value, 210 characters per line

Erase the new lines and put in a new newline after each 210th character

Once you have done this, you should have 11 lines with 210 length per line in the flag file


Because there are so many duplicate characters, simply creating a file with all one character and shuffling it with the program wouldn't give away the pattern. Each line needs to have 210 unique characters, with one character being unique to each line

i.e. line 1 is as follows: ùbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./~!@#$%^&*()_+{}|:"<>? €‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²ΞϤϨ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷ø

The first character "ù" is unique to only line 1 and serves as a marker to track where this line gets shuffled to.
Duplicate this line 11 times to replicate the original flag file, but make sure to use a unique character on each line.
You should now have 11 lines of unique characters, where the first character is unique only to that line.

Run this new file through the scrambler and repeat the newline restructuring, now you should have a file that matches the format of the encrypted flag.


Now by comparing the three files (encrypted flag, unique chars, scrambled unique chars) we can see that, for example, the "ù" character was shuffled to line 5 and was moved somewhere in the middle of the line. This means that unencrypted line 1 maps to encrypted line 5. Repeat this for each of the lines and you can properly reorder each line. 
With the pattern, reorder the scrambled files as well so that all files have the correct line order. 

Now the only step left is to reorder the characters on each line. We know that "ù" starts in index 0, but when encrypted moves to index 129. By using this, we can look at the encrypted flag and find that index 0 of the decrypted flag should be "%". 

This can be done by scripting. Pseudocode is as follows:

Open and read the encrypted flag file (with lines in the correct order)
Open and read the file with the unique characters
Open and read the file with the unique characters scrambled (with lines in the correct order)

Loop over the index and line of the unique characters
Loop over the index and character of each line

The index the first character moved to is the index of that same character in the scrambled file
That character maps to a character in the flag file at the same line at the index of the moved character
Append what it maps to onto a string

Printing that string at the end should produce the original flag