# A Dire Situation

### Description
I really need help with my budget. Let's see if there's anything you can do with my current situation!

### Difficulty
4/10

### Flag
PCTF{alternate_data_streaming_and_chill}

### Hints
TBD

### Author
Shiloh Smiles (arcticx)

### Tester

### Writeup
0. extract the .wim
1. Open the file in Notepad. The text isn't important, but the punchline category being "streaming" should offer a hint to the ADS present.
2. Run "dir /R" to see the ADS. It will show as "budget:streaming"
3. Switch to powershell and run the following two commands: 
- `$output = Get-Content .\budget:streaming -Encoding Byte -ReadCount 0`
- `Set-Content .\streaming -Encoding Byte -Value $output`
4. The name of the file is "streamingjpegjfif", which indicates its type
5. Change the first bytes of the header to `FF D8 FF E0 xx xx 4A 46
49 46 00`, which is the header as indicated by Gary Kessler's file signatures.
6. profit.

