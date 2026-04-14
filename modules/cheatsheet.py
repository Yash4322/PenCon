def show_cheatsheet():
    print("""
Available Reverse Shell Types:

bash
python
php
php-rev

Examples:

pencon -s -i <IP> -p <PORT> -t bash
pencon -s -i <IP> -p <PORT> -t php-rev

Listener:
pencon -l -p <PORT>

Encoding:
pencon -e -t base64 -d "whoami"
""")
