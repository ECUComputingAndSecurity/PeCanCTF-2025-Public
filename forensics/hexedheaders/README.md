Provided with a corrupted jpg file.

hexdump the file shows that the signiture is a partually completed PNG header with alterations:
50 89 47 4e 0a 0d 0a 1a 10 00 46 4a 46 49 01 00

Using a hex editor like hexedit to change the signiture to FF D8 FF E0 00 10 4A 46 49 46 00 01
makes the file readable and shows the flag: pecan{h3x_and_hea43r2}.