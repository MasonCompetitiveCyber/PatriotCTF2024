#include <stdio.h>
#include <string.h>

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void shrimp(){
	FILE *fptr;
	fptr = fopen("/flag.txt", "r");
	if(fptr == NULL){
		printf("Flag file not found, contact an admin!\n");
		return;
	}
	char c = fgetc(fptr);
	while(c != EOF){
		printf ("%c", c);
		c = fgetc(fptr);
	}
	fclose(fptr);
}

int i;
void main(){
	char final[50];
	char buff[50];
	puts("Welcome to the shrimplest challenge! It is so shrimple, we'll give you 3 shots.");
	for(i = 0; i < 3; i++){
		printf("Remember to just keep it shrimple!\n>> ");
		fgets(buff,sizeof(buff),stdin);
		printf("Adding shrimp...\n");
		strcpy(final,"so easy and so shrimple, have fun!");
		strncat(final,buff,50);
		printf("You shrimped the following: %s\n",final);
	}
	puts("That's it, hope you did something cool...");
}
