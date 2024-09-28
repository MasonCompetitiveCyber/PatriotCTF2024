# Challenge Name
Impersonate

### Description
One may not be the one they claim to be.

### Difficulty
5/10

### Flag
PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}

### Hints
None

### Author
__iAmPradeep


### Tester
Biplav

### Writeup

The challenge is to impersonate the admin user. The source code is given in the challenge.

App has no checks for username/password and can directly login with the any username and password.

After logging in, the session is saved with the uid and redirect to the user page.

The main thing is to do is get the flask session sigining key and the session cookie.

Forge the session cookie with the administrator's uuid matching uuid.uuid5(secret, 'administrator') and is_admin=True.

This can be generated locally and then set the cookie in the browser and go to admin page to get the flag.

### Running the challenge
```bash
docker build -t impersonate .
docker run -d -p 5000:5000 -e "FLAG=PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}" impersonate
```
