import argparse
from colorama import Fore, Style, init
init()
from modules.shell import generate_shell
from modules.encoder import encode_data
from modules.listener import start_listener
from modules.cheatsheet import show_cheatsheet


def show_banner():
    print(Fore.GREEN + r"""
  ____              ____                 
 |  _ \ ___  _ __  / ___|___  _ __   
 | |_) / _ \| '_ \| |   / _ \| '_ `  
 |  __/ (___| | | | |__| (_) | | | |
 |_|   \___/|_| |_|\____\___/|_| |_|

        PenCon - RCE Exploitation Toolkit

Made By - Arylide
Contributors - Mr. Pathi Aman Pal

Just a revershell generator.... but on you terminal....
    """ + Style.RESET_ALL)


def main():
    parser = argparse.ArgumentParser(
        description="PenCon - CLI exploitation toolkit",
        prog="pencon"
    )

    group = parser.add_mutually_exclusive_group()

    # Commands (short flags)
    group.add_argument("-s", action="store_true", help="Generate reverse shell")
    group.add_argument("-e", action="store_true", help="Encode payload")
    group.add_argument("-l", action="store_true", help="Start listener")
    group.add_argument("-c", action="store_true", help="Show cheatsheet")

    # Arguments
    parser.add_argument("-i", help="IP address")
    parser.add_argument("-p", help="Port")
    parser.add_argument("-t", help="Shell type: bash | python | php | php-rev")
    parser.add_argument("-d", help="Data")

    args = parser.parse_args()

    # No command → banner only
    if not any([args.s, args.e, args.l, args.c]):
        show_banner()
        return

    # Shell
    if args.s:
        if not (args.i and args.p and args.t):
            print("[-] Missing arguments for shell")
            return
        print(generate_shell(args.i, args.p, args.t))

    # Encode
    elif args.e:
        if not (args.t and args.d):
            print("[-] Missing arguments for encode")
            return
        print(encode_data(args.d, args.t))

    # Listener
    elif args.l:
        if not args.p:
            print("[-] Missing port")
            return
        start_listener(args.p)

    # Cheatsheet
    elif args.c:
        show_cheatsheet()
