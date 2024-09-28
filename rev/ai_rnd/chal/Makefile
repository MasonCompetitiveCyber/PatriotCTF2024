CC=gcc
CFLAGS=-fno-stack-protector

all: ai_rnd dbg

ai_rnd:
	$(CC) $(CFLAGS) rnd.c -o ai_rnd
	cp ai_rnd ../dist

dbg:
	$(CC) $(CFLAGS) rnd.c -g -o dbg

clean:
	rm -f ai_rnd dbg ../dist/ai_rnd