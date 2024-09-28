#define _GNU_SOURCE
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 8

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

char * scripts[MAX];
int tag_index = 0;
char * savedTags[MAX];
int loglen = 256;

long readnum(){
    char buf[100];
    read(0,buf,50);
    if(strstr(buf,"x") != NULL){
	    return strtol(buf, NULL, 16);
    }
    fflush(stdin);
    return strtol(buf, NULL, 10);;
}

void banner(){
	puts("            ____");
	puts("  |        | ___\          /~~~|");
	puts(" _:_______|/'(..)`\_______/  | |");
	puts("<_|``````  \__~~__/       ___|_|");
	puts("  :\_____(=========,   ,--\__|_/");
	puts("  |       \       /---'");
	puts("            |     /");
	puts("            |____/");
	puts("\n        Welcome to flightscript!				");
	puts("Configure your autonomous flight here!		");
	puts("            (Now leakless!)						");
}

void menu(){
	puts("\n1) Create flight log");
	puts("2) New flightscript");
	puts("3) Re-label flightscript");
	puts("4) Delete flightscript");
	puts("5) Exit console");
	printf(">> ");
}

void editTag(){
	int index;
	char * tag;
	printf("Label index >> ");
	index = readnum();
	if(savedTags[index] != 0 && index >= 0 && index <= MAX){
		tag = savedTags[index];
		printf("Enter a label (8) >> ");
		fgets(tag,8,stdin);
		puts("Saved label!");
	}else{
		puts("Invalid index specified!");
	}
}

int newFS(){
	char option[16];
	int script = -1;
	long size = 0;

	for(int i = 0; i < MAX; i++){
		if(scripts[i] == 0){
			script = i;
			break;
		}
	}
	if(script == -1){
		puts("No more flightscripts allowed!");
		return 1;
	}else{
		printf("Size of flightlog >> ");
		size = readnum();
		scripts[script] = malloc(size);
		printf("Label flightscript >> ");
		fgets(scripts[script]+24,8,stdin);
		printf("Save label? (y/n) >> ");
		fgets(option, sizeof(option), stdin);
		if(strcmp(option,"y")){
			savedTags[tag_index++] = scripts[script]+24;
			puts("Label saved!");
		}
	}
}

int delFS(){
	int index;
	printf("Index to delete >> ");
	index = (int) readnum();
	if(scripts[index] != 0 && index >= 0 && index <= MAX){
		free(scripts[index]);
		scripts[index] = 0;
		puts("Deleted flightscript!");
	}else{
		puts("Invalid index specified!");
	}
}


int main(){
	banner();
	char buff[8];
	char log[256];
	long option;

	while(1){
		menu();
		memset(buff,0,sizeof(buff));
		option = readnum();
		switch(option){
			case 1:
				printf("Please enter your flightlog.\n>> ");
				fgets(log, loglen-1, stdin);
				puts("Flight log saved!");
				break;
			case 2:
				newFS();
				break;
			case 3:
				editTag();
				break;
			case 4:
				delFS();
				break;
			case 5:
				puts("Have a nice day!");
				return 0;
			default:
				printf("\nInvalid option!\n");
		}
	}
}
