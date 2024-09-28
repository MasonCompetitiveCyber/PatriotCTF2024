#!/bin/sh

# LIFE SUCKS, DO NOT DISTRIBUTE

mkdir initramfs
cd initramfs
cp ../initramfs.cpio.gz .
gunzip ./initramfs.cpio.gz
cpio -idm < ./initramfs.cpio
rm initramfs.cpio
