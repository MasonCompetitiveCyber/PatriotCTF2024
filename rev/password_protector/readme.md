

# Password Protector

### Description
We've been after a notorious skiddie who took the "Is it possible to have a completely secure computer system" question a little too literally.

After he found out we were looking for them, they moved to live at the bottom of the ocean in a concrete box to hide from the law.

They sent us this message and executable. Please get their password so we can move forward with our mission.

This pyc was created in python3.11, but you don't need a specific version of python 3 to solve this...

### Attachments

```__pycache__/passwordProtector.cpython-311.pyc```

```message.txt```

### Difficulty
4/10

### Flag

    PCTF{I_<3_$3CUR1TY_THR0UGH_0B5CUR1TY!!}

### Hints
Decompile the pyc, then reverse each step to find what was in the file...

### Author
James Crowley @zephyrone3956

### Tester
- Txnner

### Writeup

#### Decompile pyc: 
This is a pyc file, what amounts to an executable for python. Fortunately, they're easy to decompile. Take the pyc, go to https://pylingual.io/ and decompile it.  

The user will get something like the decompiled.py file in the repo.

Note: This will have errors if you use other sites because it was made with python3.11, and they don't handle it well.

 #### Create a solve script: 
 Reverse each of the obfuscation steps one by one. They're listed below in the order needed to solve.
 1. Remove the fluff, seperate the key and the flag  
 2. Reverse the lambda function: Shift each character down 1
 3. Un-base64 flag
 4. Un-XOR it


