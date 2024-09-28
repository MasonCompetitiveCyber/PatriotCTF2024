#!/bin/bash
cd ../src
make clean
cd ../helper_scripts
rm ./linux* -rf
rm ./busybox* -rf
cd ../src
