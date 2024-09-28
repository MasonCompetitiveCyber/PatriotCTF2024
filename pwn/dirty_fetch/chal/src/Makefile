obj-m = vuln.o
KERNEL_VERSION=5.4

all:
	echo $(OBJECTS)
	make -C ../helper_scripts/linux-$(KERNEL_VERSION) M=$(PWD) modules

clean:
	make -C ../helper_scripts/linux-$(KERNEL_VERSION) M=$(PWD) clean
