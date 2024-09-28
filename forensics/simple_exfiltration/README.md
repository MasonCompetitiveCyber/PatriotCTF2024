# Data Extraction

### Description
We've got some reports about information being sent out of our network. Can you figure out what message was sent out.

### Difficulty
2/10

### Flag
pctf{time_to_live_exfiltration}

### Hints
None

### Author
Ryan Wong (ShadowBringer)

### Tester
- Txnner

### Writeup
1. Filter for only icmp request
2. Extract only the time_to_live
3. After extracting convert from decimal to ascii
