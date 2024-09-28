#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#define MAX_C 11

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

int i_chunks;
char * strings[MAX_C];
int sizes[MAX_C];

void menu(){
    printf("(%d/%d)\n",i_chunks,MAX_C);
    puts("1. malloc");
    puts("2. write");
    puts("3. read");
    puts("4. free");
    puts("5. print flag");
    printf("> ");
}

ssize_t read(int fd, void * buf, size_t nbytes){
        return syscall(0, fd, buf, nbytes);
}

long readnum(){
    char buf[100];
    read(0,buf,50);
    if(strstr(buf,"x") != NULL){
	    return strtol(buf, NULL, 16);
    }
    fflush(stdin);
    return strtol(buf, NULL, 10);;
}

void add(){
    int size;
    printf("Size > ");
    size = readnum();
    strings[i_chunks] = calloc(sizeof(char),size);
    if(strings[i_chunks] == NULL){
        puts("Error allocating");
        return;
    }
    sizes[i_chunks] = size;
    i_chunks++;
    puts("Allocated!");
}

void edit(){
    int index;
    int size;
    printf("Index > ");
    index = (int) readnum();
    if(index > i_chunks || index < 0 || strings[index] == NULL){
        puts("Invalid index");
        return;
    }
    size = sizes[index];
    char buf[size+1];
    printf("String > ");
    fgets(&buf, size+1, stdin);
    buf[size] = 0;
    printf("%s\nThat better have been a string!!\n",&buf);
    strcpy(strings[index],buf);
}

void delete(){
    int index;
    printf("Index > ");
    index = (int) readnum();
    if(index > i_chunks || index < 0 || strings[index] == NULL){
        puts("Invalid index");
        return;
    }
    free(strings[index]);
    strings[index] = NULL;
    sizes[index] = 0;
    puts("Freed");
}

void flag(){
    char* argv[3] = {"/bin/cat", "/flag.txt", NULL};
    execve("/bin/cat", argv, NULL);
}

int main(){
    int key;
    int option;
    long index;
    i_chunks = 0;
    puts("Strings only please!!");
    while(1){
        menu();
        option = (int) readnum();
        switch(option){
            case 1:
                add();
                break;
            case 2:
                edit();
                break;
            case 3:
                printf("Index > ");
                index = (long) readnum();
                if(index > i_chunks || index < 0){
                    puts("Invalid index");
                    break;
                }
                printf(strings[index]);
                break;
            case 4:
                delete();
                break;
            case 5:
                if(key != 0xcafebabe){
                    puts("no lol\n");
                    break;
                }
                flag();
                break;
        }
    }
}