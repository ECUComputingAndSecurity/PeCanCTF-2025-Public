# Sound Inversion

## Writeup
The challange gives you a photo of a LinkedIn post, and you need to find the post first off.
![image](https://github.com/user-attachments/assets/05feb31d-bcce-44d4-b576-12247b2c3ec9)

By searching up 'site:linkedin.com Xanarto', the posters account comes up on linkedin.

looking at their linkedin, they link their github:

Going to `all posts` gets you the encrypted message

After this, there seems to be nothing else of import to find on linkedin.

So time to look at that Github link:

![image](https://github.com/user-attachments/assets/0fa7af86-8a9e-46f9-a000-e1786abcb3e1)
Of the account's four repos, `HomemadeEncryptionAlgorithim` looks the most promising

The README.md file, mentions no one ever being able to break the ecnryption, which leads to more likely hood that this is teh encryption algorithim used. And, looking at the algorithim, it appears to do some math calcualtions on the Unicode values of characters, and then converts those back into unicode characters, which would explain why the encrypted message is made of weird unicode charcters.

The code for this encryption algorithim is:

With some deobfuscation this becomes:

Time to reverse:

Running this, prints out:

This would be extremely hard to take as an input and then intelligently de concatonat, based off length, so lets do it by hand.
We know that the flag is enrypted in base64, so the Unicode values each charcter can be range from 48, to 122.
With this knowledge, unconcating by hand is easy. We get:

just converting this into unicode and reversing the order gets `VGhlX09uZV9BbmRfT25seV9YYW5hcnRvIX0=`.
Converting this from base64, gets you `The_One_And_Only_Xanarto!}`.

This appears to be the second half to a flag. Back to OSINT.
Looking at the other Github Repos of this user reveals nothing, and the linkedin posts don't either. But, the `HomemadeEncryptionAlgorithim` repo has 8 commits, which is slightly suspicous. Looking at them reveals a `Removed confidential info` commit.
![image](https://github.com/user-attachments/assets/0558594e-6740-45dc-927c-a96552b199e3)

Looking at this commit, reveals what appears to be the first half of the flag `pecan{The_Xanarto`.
Making the final flag `pecan{The_XanartoThe_One_And_Only_Xanarto!}`
