from Crypto.Cipher import AES

def decrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f_input, open(output_file, 'wb') as f_output:
        cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
        encrypted_data = f_input.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        f_output.write(decrypted_data)

def main():
    key = bytes.fromhex('0123456789abcdef1032547698badcfef0e1d2c3b4a5968778695a4b3c2d1e0f')
    iv = bytes.fromhex('000102030405060708090a0b0c0d0e0f')

    input_file = 'flag.txt.enc'
    output_file = 'flag_decrypted.txt'
    
    decrypt_file(input_file, output_file, key, iv)

if __name__ == '__main__':
    main()

