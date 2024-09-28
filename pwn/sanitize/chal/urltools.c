#include <stdio.h>
#include <string.h>
#define MAX 40

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}


void menu(){
    puts("\n1. Sanitize URL");
    puts("2. Detect TLD");
    puts("3. Quit");
    printf(">> ");
}

void banner() {

    puts("Welcome to our URL utility program! The internet is wonderful and safe.");

}

void sanitize(char * dst){
    char buf[MAX];

    memset(dst,0,sizeof(dst));
    printf("Please enter your URL to be sanitized\n>> ");
    fgets(buf, sizeof(buf), stdin);

    // Escape
    int i = 0;
    while(buf[i] != '\0' && buf[i] != '\n' && i < MAX){
        if(buf[i] == '.' || buf[i] == '/'){
            char escaped[4];
            escaped[0] = '[';
            escaped[1] = buf[i];
            escaped[2] = ']';
            escaped[3] = '\0';
            strcat(dst,escaped);
        }else{
            char copy[2];
            copy[0] = buf[i];
            copy[1] = '\0';
            strcat(dst, copy);
        }
        i++;
    }
    printf("Your sanitized url is %s\n",dst);
}

void detect_tld(char * dst){
    char * ptr;
    char tld[64];
    int s_tld;
    char needle = '.';
    ptr = strrchr(dst, needle);
    if(ptr != NULL){
        printf("Your TLD is %s\n",ptr+2);
    }else{
        memset(tld,0,sizeof(tld));
        printf("No TLD detected, specify your TLD\n>> ");
        fgets(tld,sizeof(tld),stdin);
        s_tld = strlen(tld);
        printf("Your TLD is %s\n",dst+s_tld);
    }
}


int main(){
    char url[MAX];
    char buf[40];
    int option;
    banner();

    while(1){
        menu();
        fgets(buf, sizeof(buf), stdin);
        option = atoi(buf);
        switch(option){
            case 1:
                sanitize(url);
                break;
            case 2:
                detect_tld(url);
                break;
            case 3:
                return 0;
        }
    }
}

