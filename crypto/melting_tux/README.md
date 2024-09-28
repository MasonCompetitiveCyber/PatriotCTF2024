# 
Melting Tux

### Description
We found this image that was partially encrypted. We were able to recover the script used to encrypt it, but it was partially encrypted too. We have given you the image and the intelligible part of the script. Please decrypt the image. Note: Forensic evidence indicates that the image was created on August 26th, 2024 at 21:43:20 UTC. 

### Difficulty
7/10

### Flag
PCTF{NO_PLEASE_DONT_ECB_ME_AGAIN}

### Hints
The file is not split at an index between 1000 and 2000. On a completely unrelated note(wink) we're using a 32-character key here. 

### Author
James Crowley (@zephyrone3956)

### Tester
- Txnner

### Writeup
1. First, identify the offset. The offset defines where we slice the image to encrypt the second half. When provided with the time from the prompt and the script half_script.py, we can read the original function to determine that we must take the time, turn it into the UTC timestamp, then seed python's random function with it. From there we generate the random number used as the offset. 
2. It doesn't end there, as the solver will need to intuit (or bruteforce) that we multiply the offset by 256. This was done for padding, but I'm not 100% sure it's necessary. It can be intuited by noticing that if you use an offset between 1000 and 2000, that only a small portion of the file is encrypted. The hints help with this. I susect that the challenge this was inspired by did not do this, but maybe I was just bad. 
3. We then open the image melting.png as bytes, and split the data into two parts using the offset. The ciphertext(the second half) is decrypted with the provided decrypt function. We write an outfile, combining the first half of the data (which is plaintext) with the second half of the data (decrypted ciphertext). This creates flag_decrypted.py.  
