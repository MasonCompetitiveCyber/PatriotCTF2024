#!/bin/bash

timeout --foreground 180 /usr/bin/qemu-system-x86_64 \
	-m 64M \
	-cpu kvm64,+smep,+smap \
	-kernel /src/bzImage \
	-initrd /src/initramfs.cpio.gz \
	-nographic \
	-monitor none \
	-append "console=ttyS0 kaslr quiet panic=1" \
	-no-reboot
