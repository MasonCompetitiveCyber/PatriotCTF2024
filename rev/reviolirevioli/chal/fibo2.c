#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//fibonacci!!!
unsigned long long calc(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    unsigned long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

//gen fibonacci seq
void gen_correct_flag(char *flag) {
    unsigned long long fibs[15];
    for (int i = 0; i < 15; i++) {
        fibs[i] = calc(i);
    }

    char temp[256] = {0}; // Buffer to hold the formatted Fibonacci sequence
    for (int i = 0; i < 15; i++) {
        char buf[20];
        snprintf(buf, sizeof(buf), "%llu", fibs[i]);
        strcat(temp, buf);
    }
    snprintf(flag, 256, "ITALY_%s", temp);
}

// generate flag kinda
void assemble_flag(const char *prefix, char *flag) {
    snprintf(flag, 256, "PCTF{%s}", prefix);
}

int main() {
    char user_input[256];
    char correct_flag[256];
    char result_flag[256];

    gen_correct_flag(correct_flag);
    assemble_flag(correct_flag, result_flag);


    printf("Enter-a the password-a: ");
    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\n")] = '\0'; 

    if (strcmp(user_input, correct_flag) == 0) {
        printf("Congratulations! The flag is: %s\n", result_flag);
    } else {
        printf("No toucha my spaget!\n");
    }

    return 0;
}
