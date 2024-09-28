
#!/bin/bash

cp ../dist/dirty_fetch.tar.gz .
tar -xvzf dirty_fetch.tar.gz
mv dirty_fetch/initramfs.cpio.gz .
mv dirty_fetch/vuln.ko .
mv dirty_fetch/bzImage .
mv dirty_fetch/start.sh .
rmdir dirty_fetch
./extract-image.sh bzImage > vmlinux
ROPgadget --binary ./vmlinux > gadgets.txt
./decompress.sh
cd initramfs
sed -i 's/exec su -l ctf/# exec su -l ctf/g' init
cd ..
rm dirty_fetch.tar.gz
rm start.sh
