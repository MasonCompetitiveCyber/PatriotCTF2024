#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <signal.h>
#include <pthread.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/syscall.h>

#if HAVE_STROPTS_H
#include <stropts.h>
#endif

int fd;
typedef struct data{
	char * content;
    size_t length;
};
struct data storage;

void open_device(void) {
    puts("[*] Opening vuln");
    fd = open("/proc/vuln", O_RDWR);
    if (fd < 0) {
        puts("[!] Failed to open device");
        exit(-1);
    }
    printf("[+] Device opened successfully, fd: %d\n", fd);
} 

void close_device(void) {
    if(close(fd) == -1) {
        puts("[!] Error closing the device");
        exit(-1);
    }
    puts("[+] Device closed");
}

void change_max(unsigned long max) {
    if (ioctl(fd, 0x10, max) == -1) {
        puts("[!] Error calling ioctl");
        exit(-1);
    }
    printf("[+] Max changed to %lu\n", max);
}

void read_device(void){
    char * buf;
    read(fd,buf,sizeof(buf));
}

void write_device(void){
    char * buf;
    write(fd,buf,sizeof(buf));
}

void send_data(void){
    char * test_string = malloc(0x18);
    char s1[20] = "Hello world!";
    strcpy(test_string,s1);
    storage.content = test_string;
    storage.length = 15;
    printf("Storage @ %p and storage.content @ %p and storage.content contains %s\n",&storage,storage.content,storage.content);
    if(ioctl(fd,0x20,&storage) == -1){
        puts("[!] Error calling ioctl");
        exit(-1);
    }
    free(test_string);
}

void save_data(void){
    if(ioctl(fd,0x30,0) == -1){
        puts("[!] Error calling ioctl");
        exit(-1);
    }
}

void read_data(void){
    char stuff[storage.length];
    stuff[0] = storage.length;
    puts("[*] Calling read");
    ioctl(fd, 0x40, stuff);
    printf("Returned data: %s\n",stuff);
}

int main(){
    open_device();
    send_data();
    save_data();
    read_data();
    close_device();
    return 0;
}
