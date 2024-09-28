# really_only_echo

### Description
Hey, I have made a terminal that only uses echo, can you find the flag? 

### Difficulty
5/10 

### Flag
pctf{echo_is_such_a_versatile_command}

### Hints
No hints

# Author
Ryan Wong (ShadowBringer)

### Tester


### Writeup
First you need to understand how to create and execute commands with echo. 
1. echo $($(echo l)$(echo s)) -> This is list the directory
2. echo $($(echo c)$(echo a)$(echo t)$(echo " ")$(echo f)$(echo l)$(echo a)$(echo g)$(echo .)$(echo t)$(echo x)$(echo t)) -> This allows the printing of the flag
3. or, echo $($(echo c)at flag.txt