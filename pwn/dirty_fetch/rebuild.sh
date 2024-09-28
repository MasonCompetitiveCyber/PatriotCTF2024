#!/bin/sh

cd chal/helper_scripts
./clean_all.sh
./build_kernel.sh

cd ..
./helper_scripts/rebuild-fs.sh

cd ../dist
./build_dist.sh

cd ../writeup
rm initramfs initramfs.cpio.gz bzImage gadgets.txt vmlinux -r
./build_env.sh


