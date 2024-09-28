## KIRAN SAU PROBLEM  

### Description
Kiran Ghimire feigned ignorance and said he had no idea what the flag was.

### Difficulty
7/10

### Flag
PCTF{Kiran_SAU_Manifested}

### Hints
CVE

### Author
Kiran Ghimire (sau)

### Tester

### Writeup
1. Try to access the path `/challenge.php`, we are restricted to access the page.
2. The following configuration is found in the `.htaccess` file:
```
<Files "challenge.php">
    AuthType Basic 
    AuthName "Admin Panel"
    AuthUserFile "/etc/apache2/.htpasswd"
    Require valid-user
</Files>
```
3. When Files directive is used to restrict a single file, it can be bypassed directly under the default PHP-FPM installation.
More information can be foud here: https://blog.orange.tw/2024/08/confusion-attacks-en.html?m=1#%E2%9A%94%EF%B8%8F-Primitive-1-2-ACL-Bypass

4. We can simply bypass the authentication by appending the URL-encoded '?' character (%3F) to the end of the PHP file extension.
Ensure to put `.php` after the `?` character.
Bypassed:
`http://127.0.0.1:8090/challenge.php%3Fa.php`
5. If we can make the `$cc` variable false within the run function, then we can control the `$url` variable and read the flag executed by the system command.
6. YAML treats `NO` as `false`. So, we can set the value of `$cc` to NO by passing the value of the country parameter as Norway.
Read more about `The Norway Problem` here: https://hitchdev.com/strictyaml/why/implicit-typing-removed/

Final Payload to read the flag:
`http://127.0.0.1:8090/challenge.php%3Fa.php?country=Norway&url=-o /var/www/html/flag.txt file:///get-here/flag.txt`
`http://127.0.0.1:8090/flag.txt`

Getting the flag from the `get-here` directory and writing it to the user-reachable directory.
