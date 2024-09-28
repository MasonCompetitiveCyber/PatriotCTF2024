import subprocess
from PIL import Image

tshark = ["C:\\Program Files\\Wireshark\\tshark.exe", "-r", "capture.pcapng", "-Y", "usbhid.data", "-T", "fields", "-e", "usbhid.data"]

output = subprocess.run(tshark, stdout=subprocess.PIPE).stdout.splitlines()

img = Image.new('RGB', (5000, 5000), color='white')
canvas = img.load()

write = False

for i in output:
    a = i.decode()
    if a == '0100000000000000':
        write = True
    elif a == '0000000000000000':
        write = False
    # //10 helps file size stay smaller (not necessary, but may have to increase image size if removed)
    x = int(bytearray.fromhex(a[4:8])[::-1].hex(), 16)//10
    y = int(bytearray.fromhex(a[8:12])[::-1].hex(), 16)//10

    if write:
        # loops to make flag easier to read (not necessary)
        for i in range(5):
            for j in range(5):
                canvas[x + i, y + j] = (255, 0, 0)

img.save("flag.png")

exit()
