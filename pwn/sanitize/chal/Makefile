CC=mipsel-linux-gnueabi-gcc
CC=mipsel-linux-gnu-gcc

all:
	${CC} urltools.c -o urltools -fno-stack-protector

host: all
	docker build .
	./host.sh

clean:
	rm urltools
