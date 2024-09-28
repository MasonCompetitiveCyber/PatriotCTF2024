# Abnomal Maybe Illegal

### Description
We have recently discovered tons of traffic leaving our network. We have reason to believe they are using an abnormal method. Can you figure out what data they are exfiltrating?

### Difficulty
7/10

### Flag
pctf{abnormal_flags_are_illegal}

### Hints
Do you know the http packet structure and its rules

### Author
Ryan Wong (ShadowBringer)

### Writeup
1. Identify the packets with illegal flags.
2. Filter for only SYN and FIN flags (this is an illegal flag combination)
3. Export those packets and look at the PSH and RST flags
4. Take the 2 bits from each packet and from the PSH and RST flags (left to right)
5. Combime the bits and encode to ascii for Flag
6. In solve folder python script called solve.py has it all scripted out
