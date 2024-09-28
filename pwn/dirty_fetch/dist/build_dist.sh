#!/bin/bash

# DO NOT DISTRIBUTE THIS FILE

rm dirty_fetch -rf
mkdir dirty_fetch
cp ../chal/helper_scripts/linux-5.4/arch/x86_64/boot/bzImage dirty_fetch/bzImage
cp ../chal/initramfs-dist.cpio.gz dirty_fetch/initramfs.cpio.gz
cp ../chal/start.sh dirty_fetch/start.sh
cp ../chal/initramfs/vuln.ko dirty_fetch/vuln.ko
cp ../chal/src/vuln.c dirty_fetch/vuln.c
tar -czvf dirty_fetch.tar.gz dirty_fetch
rm dirty_fetch -rf
