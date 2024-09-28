import collections

def solve_challenge(output_file):
    with open(output_file, 'r') as f:
        hex_lines = f.readlines()

    num_samples = len(hex_lines)

    bit_length = (len(hex_lines[0].strip()) * 4)
    bias_counts = [0] * bit_length
    #print(bit_length)


    for hex_line in hex_lines:
        binary_line = bin(int(hex_line.strip(), 16))[2:].zfill(8 * len(hex_line.strip()) // 2)
        #print(binary_line)
        first_bit = binary_line[0] == '1'
        for i, bit in enumerate(binary_line):
            bias_counts[i] += 1 if (bit == '0' and not first_bit) or (bit == '1' and first_bit) else 0
    bias_counts[0] = 0
    #print(bias_counts)
    flag_bits = ['0' if count < num_samples // 2 else '1' for count in bias_counts]

    flag_binary_0 = ''.join(flag_bits)
    flag_binary_1 = ''.join('1' if bit == '0' else '0' for bit in flag_bits)
    #print(flag_binary_0)
    #print(flag_binary_1)
    flag_0 = ''.join(chr(int(flag_binary_0[i:i+8], 2)) for i in range(0, len(flag_binary_0), 8))
    flag_1 = ''.join(chr(int(flag_binary_1[i:i+8], 2)) for i in range(0, len(flag_binary_1), 8))

    return flag_0, flag_1

if __name__ == "__main__":
    output_file = 'output.txt'
    flag_0, flag_1 = solve_challenge(output_file)
    print(f"Recovered FLAG assuming first bit is 0: {flag_0}")
    #print(f"Recovered FLAG assuming first bit is 1: {flag_1}")
