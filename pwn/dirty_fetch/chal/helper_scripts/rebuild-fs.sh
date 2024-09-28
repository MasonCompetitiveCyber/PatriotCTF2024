#!/bin/bash

# LIFE SUCKS, DO NOT DISTRIBUTE!

rm initramfs/flag.txt
pushd initramfs
find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../initramfs-dist.cpio.gz
popd

cp flag.txt initramfs/flag.txt
pushd initramfs
find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../initramfs.cpio.gz
popd
