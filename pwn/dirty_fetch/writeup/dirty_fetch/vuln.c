#include <linux/module.h>
#include <linux/proc_fs.h>
#include <linux/slab.h>
#include <linux/uaccess.h>
#define MAX_SIZE 240

MODULE_LICENSE("GPL");

unsigned long max;
typedef struct data{
	char * content;
    size_t length;
}data;
data * storage;

static int device_open(struct inode* inode, struct file* filp) {
    printk(KERN_ALERT "Opened.\n");
    return 0;
}

static int device_release(struct inode* inode, struct file* filp) {
    if(storage != 0){
        kfree(storage->content);
        kfree(storage);
    }
    printk(KERN_ALERT "Closed.\n");
    return 0;
}

static ssize_t device_read(struct file* filp, char* buf, size_t len, loff_t* off) {
    printk(KERN_ALERT "Unimplemented!");
    return -EINVAL;
}

static ssize_t device_write(struct file* filp, const char* buf, size_t len, loff_t* off) {
    printk(KERN_ALERT "Unimplemented!");
    return -EINVAL;
}

data * get_storage_contents(unsigned long buf){
    data * request = (data *)kmalloc(sizeof(data),GFP_KERNEL);
    if(request == NULL){
        return NULL;
    }
    copy_from_user(request, (data *)buf, sizeof(data));
    char * content = (char *)kmalloc((request->length),GFP_KERNEL);
    if(content == NULL){
        return NULL;
    }
    copy_from_user(content,request->content,request->length);
    memcpy(request, &content, 8);
    return request;
}

int validate_buf(unsigned long buf){
    data * request = get_storage_contents(buf);
    if(request == NULL){
        printk(KERN_ALERT "Error fetching storage from userspace!");
        return -ENOMEM;
    }
    int ret = request->length < MAX_SIZE;
    kfree(request->content);
    kfree(request);
    return ret;
}

static ssize_t edit_storage(unsigned long buf) {
    data * request;
    int ret;
    if(validate_buf(buf)){
        request = get_storage_contents(buf);
        storage = request;
        ret = request->length;
    }else{
        request = NULL;
        printk(KERN_ALERT "Specified size goes out of bounds.");
        ret = -EFAULT;
    }
    return ret;
}

static long device_ioctl(struct file* filp, unsigned int ioctl_num, unsigned long ioctl_param) {
    long ret = -EINVAL;
    char content[MAX_SIZE];

    switch(ioctl_num){
        case 0x10:
            if(ioctl_param > 0){
                max = ioctl_param;
                ret = ioctl_param;
            }else{
                printk(KERN_ALERT "Invalid max");
                ret = -EINVAL;
            }
            break;
        case 0x20:
            if(storage != 0){
                kfree(storage->content);
                kfree(storage);
                storage = 0;
            }
            ssize_t request = edit_storage(ioctl_param);
            if(request == -EFAULT){
                printk(KERN_ALERT "Error copying userspace data!");
            }else{
                printk(KERN_ALERT "Data copied!");
            }
            ret = (long) request;
            break;
        case 0x30:
            if(storage == 0){
                printk(KERN_ALERT "Nothing to save!");
                ret = -EINVAL;
            }else{
                memcpy(content,storage->content,storage->length);
                ret = storage->length;
                printk(KERN_ALERT "Data saved!");
            }
            break;
        case 0x40:
            unsigned long len;
            if(get_user(len, (unsigned long *)ioctl_param) == -EFAULT){
                printk(KERN_ALERT "Error fetching length!");
                ret = -EFAULT;
            }
            if(copy_to_user((char *)ioctl_param, content, len % max) != 0){
                printk(KERN_ALERT "Error reading data!");
                ret = -EFAULT;
            }
            if(ret != -EFAULT){
                ret = len % max;
            }
            break;
        default:
            printk(KERN_ALERT "Invalid command");
    }
    return ret;
}

static struct file_operations fops = {
    .read = device_read,
    .write = device_write,
    .unlocked_ioctl = device_ioctl,
    .open = device_open,
    .release = device_release};

struct proc_dir_entry* proc_entry = NULL;

int init_module(void) {
    max = (unsigned long)MAX_SIZE;
    storage = 0;
    proc_entry = proc_create("vuln", 0666, NULL, &fops);
    printk(KERN_ALERT "Challenge loaded at /proc/vuln, good luck!!\n");
    return 0;
}

void cleanup_module(void) {
    if (proc_entry) {
        proc_remove(proc_entry);
    }
}
