#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/err.h>

#define AES_KEY_LENGTH 256
#define AES_BLOCK_SIZE 16
#define BUFFER_SIZE 1024

void handleErrors(const char *msg) {
    fprintf(stderr, "%s\n", msg);
    ERR_print_errors_fp(stderr);
    exit(EXIT_FAILURE);
}

int main() {
    FILE *inputFile = fopen("flag.txt", "rb");
    FILE *outputFile = fopen("flag.txt.enc", "wb");
    if (inputFile == NULL || outputFile == NULL) {
        handleErrors("Error opening file");
    }

    unsigned char staticKey[] = {
        0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
        0x10, 0x32, 0x54, 0x76, 0x98, 0xba, 0xdc, 0xfe,
        0xf0, 0xe1, 0xd2, 0xc3, 0xb4, 0xa5, 0x96, 0x87,
        0x78, 0x69, 0x5a, 0x4b, 0x3c, 0x2d, 0x1e, 0x0f
    };

    unsigned char staticIV[AES_BLOCK_SIZE] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f
    };

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    EVP_EncryptInit_ex(ctx, EVP_aes_256_cfb(), NULL, staticKey, staticIV);

    unsigned char buffer[BUFFER_SIZE];
    unsigned char encryptedBuffer[BUFFER_SIZE + AES_BLOCK_SIZE];
    int bytesRead, encryptedBytes;

    while ((bytesRead = fread(buffer, 1, BUFFER_SIZE, inputFile)) > 0) {
        EVP_EncryptUpdate(ctx, encryptedBuffer, &encryptedBytes, buffer, bytesRead);
	fwrite(encryptedBuffer, 1, encryptedBytes, outputFile);
    }

    EVP_EncryptFinal_ex(ctx, encryptedBuffer, &encryptedBytes);
    fwrite(encryptedBuffer, 1, encryptedBytes, outputFile);

    EVP_CIPHER_CTX_free(ctx);
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
