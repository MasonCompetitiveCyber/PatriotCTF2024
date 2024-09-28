#!/bin/bash

/usr/bin/qemu-system-x86_64 \
    -m 64M \
    -cpu kvm64,+smep,+smap \
    -kernel ./bzImage \
    -initrd ./initramfs.cpio.gz \
    -nographic \
    -monitor none \
    -append "console=ttyS0 kaslr quiet panic=1" \
    -no-reboot \
    -fsdev local,security_model=passthrough,id=fsdev0,path=./src -device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=hostshare \
    -s
