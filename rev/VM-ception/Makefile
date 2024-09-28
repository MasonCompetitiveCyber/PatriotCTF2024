build:
	gcc main.c -o vm 
test: build
	python programmer.py
	echo "pctf{nest3d_vm_s3cr3ts}" | ./vm ./vm_program.bin
test_close:
	-echo "pctf{nest3d_vm_s3cr3tsQ}" | ./vm ./vm_program.bin
	-echo "pctf{nest3d_vm_s3cr3ts" | ./vm ./vm_program.bin
	-echo "tf{nest3d_vm_s3cr3ts}" | ./vm ./vm_program.bin
	-echo "pctf{nest3d_vm_s3cr3ts}_extra" | ./vm ./vm_program.bin
	-echo "pctf{0nest3d_vm_s3cr3ts}" | ./vm ./vm_program.bin
	-echo "pctf{nes0t3d_vm_s3cr3ts}" | ./vm ./vm_program.bin
	-echo "pctf{nest3d0_vm_s3cr3ts}" | ./vm ./vm_program.bin
	-echo "pctf{nest3d_vm_0s3cr3ts}" | ./vm ./vm_program.bin
	-echo "000" | ./vm ./vm_program.bin