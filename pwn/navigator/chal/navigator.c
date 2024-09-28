#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void banner(){
    puts("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=");
    puts("Welcome to navigator!");
    puts("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=");
    puts("We're here for all of your navigation needs");
    for(int i = 0; i < 320; i++){
        if(i % 32 == 0){
            printf("\n");
        }
        printf("X");
    }
    printf("\n");
}

void menu(){
    puts("1. Set a pin");
    puts("2. View a pin");
    puts("3. Quit");
    printf(">> ");
}

void viewPin(char * map){
    char buf[16];
    int index;

    printf("Pin index >> ");
    fgets(buf, sizeof(buf), stdin);
    index = atoi(buf);

    if(index > (320-1)){
        index = (320-1);
    }

    printf("Pin:\n%c\n",map[index]);
    for(int i = 0; i < 320; i++){
        if(i % 32 == 0){
            printf("\n");
        }
        printf(" %c ",map[i]);
    }
    printf("\n");
}

void setPin(char * map){
    char buf[16];
    int index;

    printf("Pin index >> ");
    fgets(buf, sizeof(buf), stdin);
    index = atoi(buf);

    if(index > 0x320){
        puts("Stop!");
        return;
    }else{
        printf("Pin character >> ");
        fgets(buf, sizeof(buf), stdin);
        map[index] = buf[0];
    }
}

int main(){
    char map[320];
    char buf[16];
    int option;

    banner();
    for(int i = 0; i < 320; i++){
        map[i] = 'X';
    }

    while(1){
        menu();
        fgets(buf, sizeof(buf), stdin);
        option = atoi(buf);
        switch(option){
            case 1:
                setPin(map);
                break;
            case 2:
                viewPin(map);
                break;
            case 3:
                return 0;
        }
    }
}
