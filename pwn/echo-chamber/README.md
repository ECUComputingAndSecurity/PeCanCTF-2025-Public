# Echo Chamber

### Note
If the challenges can't have ghidra be neccessary, then give them `backup_file.c`, instead of the binary

## Writeup

Connecting to the challenge through nc, gets you:

![image](https://github.com/user-attachments/assets/fc0caa63-be82-4034-b682-0389eea5df54)

This is a screen, where you can type whatever text you want, and then a copy of that text is replied.

Now lets open up the binary in `ghidra`. There is a single function, in C this is:
```c
void main(void)

{
  int iVar1;
  char local_28 [32];

  builtin_strncpy(local_28 + 0x10,"ccccccccccccccc",0x10);
  builtin_strncpy(local_28,"bbbbbbbbbbbbbbb",0x10);
  puts("Welcome to the Echo Chamber");
  do {
    while( true ) {
      gets(local_28);
      iVar1 = strcmp(local_28 + 0x10,"givemeflag");
      if (iVar1 != 0) break;
      system("cat flag.txt");
    }
    puts(local_28);
  } while( true );
}
```

This appears to set a memory address to `bbbbbbbbbbbbbbb`, and then after skipping one memory address, sets the next one to `ccccccccccccccc`.
If prints out `Welcome to the Echo Chamber`, and then saves user input into the memory adress full of `b`s. Afterwards teh memeory address full of `c`s is checked to see if it equals `givemeflag`. If it does, then the contents of `flag.txt` is outputed.

As there is no conventional way to alter the memory address after `local_28` (the one full of `b`s), and given that this is a binary exploitation challenge, it is likely that the user it to do a buffer overflow to rewrite the `c`s memory address. This can only be done as `gets` does not take the maximum length of the input as a paramater.

As such merely inputing 16 of any character, and then the string `givemeflag` should return the flag.
Inputing `aaaaaaaaaaaaaaaagivemeflag`, returns the flag `pecan{533_buff3r_0v3rf70w_c4n_b3_345y!}`

![image](https://github.com/user-attachments/assets/3dbd6492-f8a1-4cff-898a-fdbf4e71973c)
