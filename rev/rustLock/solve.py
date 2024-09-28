import subprocess

password = ""

baseline=""
for j in range(40):
	l = len(password)
	for i in range(0x19, 0x7F, 1):
		f = open('pass.txt', 'w')
		if len(password) < 31:
			f.write(password + chr(i) + (31-len(password))*"A")
		else:
			f.write(password + chr(i))
		f.close()
		
		p = subprocess.Popen(
			"valgrind --trace-children=yes --tool=callgrind ./rustLock < pass.txt 2>&1 | grep refs | cut -d ' ' -f11",
			stdout=subprocess.PIPE,
			shell=True,
		)
		output = p.communicate()[0].strip(b"\n").split(b"\n")[-1]
		output = int(output.decode().replace(",", ""))

		print(password, chr(i), output)
		if i == 0x19:
			baseline = output
		elif output-baseline > 250:
			password += chr(i)
			print(f"Found: {chr(i)} ({output})")
			print(f"Password: {password}")
			break
	if l == len(password):
		print("Error, try again")
		break
