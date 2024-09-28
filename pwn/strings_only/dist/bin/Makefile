strings_only: strings_only.c
	zig cc -Wall -target x86_64-linux-gnu -no-pie -Wl,-rpath=../glibc/glibc_2.25 -Wl,--dynamic-linker=../glibc/glibc_2.25/ld.so.2 -o strings_only strings_only.c
clean:
	rm ./strings_only
