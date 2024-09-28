#include <stdio.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

bool check(unsigned char* shellcode, size_t len) {
    for (int i = 0; i < len; i++) {
	if (shellcode[i] == 0x3b || shellcode[i] == '/' ||
	        shellcode[i] == 'b' ||
		shellcode[i] == 'i' ||
		shellcode[i] == 'n' ||
		shellcode[i] == 's' ||
		shellcode[i] == 'h' ||
		shellcode[i] == '\0')
	    return false;
    }
    return true;
}

void alter(unsigned char* shellcode, size_t len) {
    for (int i = 0; i < len - 1; i += 4) {
	shellcode[i] ^= shellcode[i + 1];
    }
    for (int i = 2; i < len; i += 12) {
	if (i + 3 < len) {
	    shellcode[i] = '\xf4';
	    shellcode[i + 1] = '\xf4';
	    shellcode[i + 2] = '\xf4';
	    shellcode[i + 3] = '\xf4';
	}
    }
}

int main() {
    unsigned char* shellcode = mmap(NULL, 160, PROT_EXEC|PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);

    printf("Enter shellcode:\n");
    int len = read(0, shellcode, 160);

    if (!check(shellcode, len)) {
	printf("HACKER ALERT!!!\n");
	exit(1);
    }

    alter(shellcode, len); 

    ((void (*)())(shellcode))();

    return 1;
}
