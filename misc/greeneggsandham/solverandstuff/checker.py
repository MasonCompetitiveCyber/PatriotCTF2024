def conv(num):
    flipped_dict = {
        '0000000': '0000',
        '1101001': '0001',
        '0101010': '0010',
        '1000011': '0011',
        '1001100': '0100',
        '0100101': '0101',
        '1100110': '0110',
        '0001111': '0111',
        '1110000': '1000',
        '0011001': '1001',
        '1011010': '1010',
        '0110011': '1011',
        '0111100': '1100',
        '1010101': '1101',
        '0010110': '1110',
        '1111111': '1111'
    }

    return flipped_dict[num]


def check_hamming_7_4(binary_str):
    # Ensure the input is a 7-bit binary string
    if len(binary_str) != 7 or not all(bit in '01' for bit in binary_str):
        raise ValueError("Input must be a 7-bit binary string")

    # Convert the binary string to a list of integers
    bits = [int(bit) for bit in binary_str]

    # Calculate the parity bits
    p1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
    p2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
    p3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]

    # Calculate the error position
    error_position = p1 * 1 + p2 * 2 + p3 * 4

    # Output the result
    if error_position == 0:
        return -1
    else:
        print("found an error!")
        return error_position

file = open('testoutput.txt', 'r')

one = ""
two = ""

for line in file:
    error = check_hamming_7_4(line[1:].rstrip())

    if error == -1:
        pass
    else:
        binlist = list(line)
        if binlist[error] == '0':
            binlist[error] = '1'
        else:
            binlist[error] = '0'

        line = ''.join(binlist)

    if line[0] == "0":
        #print(hex(int(conv(line[1:].rstrip()),2)))
        one += str(hex(int(conv(line[1:].rstrip()),2)))[2:]
    else:
        two += str(hex(int(conv(line[1:].rstrip()), 2)))[2:]
print("Password 1: secure-password-j=v@b8?fTcP!2bY")
print("Password 1: ", end='')
for x in range(0, len(one) -1, 2):
    digit = one[x:x+2]
    print(chr(int(digit,16)),end='')
print("\nPassword 2: secure-password-4n!Lg5PCTF7!mm3")
print("Password 2: ", end='')
for x in range(0, len(two) -1, 2):
    digit = two[x:x+2]
    print(chr(int(digit,16)),end='')
