#!/usr/bin/env python



import os


# tshark filter for only packets with syn and fin flags are they are illegal
# Grep is to pull out the flags
# Then the flags are stored in a file to be read and processed later
os.system("tshark -r abnormal_illegal.pcapng -Y 'tcp.flags.syn == True && tcp.flags.fin == True' | grep -o -E '\[FIN, SYN.*+\]' > psh_rst.txt")


# Key is setup like this because look at both wireshark and http packet structure
# The bits are calculated from left to right [PSH, RST, SYN, FIN]
key_2_2bits = {
	"[FIN, SYN]" 			: "00",
	"[FIN, SYN, RST]" 		: "01",
	"[FIN, SYN, PSH]"		: "10",
	"[FIN, SYN, RST, PSH]"	: "11",
}


# Reads the file holding the flags
with open("psh_rst.txt", "r") as bits:
	together = ""

	# Maps to the 2 bits
	for i in bits:
		together += key_2_2bits[i.strip()]

		print(key_2_2bits[i.strip()], end="")
	print()

	# Translate from binary to ascii
	binary_int = int(together, 2)
	byte_number = binary_int.bit_length() + 7 // 8
	binary_array = binary_int.to_bytes(byte_number, "big")
	ascii_text = binary_array.decode()
	print(ascii_text)