

def conv(num):
    dict = {
        '0000': '0000000',
        '0001': '1101001',
        '0010': '0101010',
        '0011': '1000011',
        '0100': '1001100',
        '0101': '0100101',
        '0110': '1100110',
        '0111': '0001111',
        '1000': '1110000',
        '1001': '0011001',
        '1010': '1011010',
        '1011': '0110011',
        '1100': '0111100',
        '1101': '1010101',
        '1110': '0010110',
        '1111': '1111111'
    }

    return dict[num]

file = open('password1.txt', 'r')
file2 = open('password2.txt', 'r')

count = 0

while 1:

    char = ""
    prefix = ""

    # read by character
    if count%2 == 0:
        char = file.read(1)
        prefix = "0"
    else:
        char = file2.read(1)
        prefix = "1"
    if not char:
        break

    num1 = ""
    num2 = ""

    num = bin(int(hex(ord(char)),16))[2:]

    if len(num) == 7:
        num1 = "0" + num[0:3]
        num2 = num[3:]
    elif len(num) == 6:
        num1 = "00" + num[0:2]
        num2 = num[2:]

    print(prefix + conv(num1))
    print(prefix + conv(num2))


    count+=1


file.close()

