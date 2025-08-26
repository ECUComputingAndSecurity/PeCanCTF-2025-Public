# TLSB

## Description

You might have heard of Least Significant Bit (LSB) Steganography, but have you ever heard of Third Least Significant Bit (TLSB) Steganography? (Hopefully not considering I made it up for this challenge).

## Writeup

The description tells you that the steganography method to hide the flag is 'Third Least Significant Bit Encryption', which with how it also mentions LSB likely means that it is just a variation on LSB encryption.

Searching up 'Third Least Significant Bit Steganography' on google doesn't pop up with any premade tools to do this challenge with, so either you need to edit a premade tool, or make a small tool to do it for you. This writeup follows making a tool in python to read just the third least significant bit of each of the image's pixel's colour channels.

The first thing to do is to check the type of the file.

```bash
$ file TLSB

TLSB: PC bitmap, Windows 3.x format, 16 x 16 x 24, resolution 16 x 16 px/m, cbSize 822, bits offset 54
```

This displays that the image is a `BMP` file. A good website to get an idea of how BMP files are structured is [https://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm](https://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm)

As the table shows (on the linked website), the actual picture data only starts on the `0x36`th  byte (the `54`th byte in decimal). This means that as any changes to the header data could cause an error, the hidden data will only begin starting on the `54`th byte. Time to write a python program that reads the third least significant bit of every byte starting from the `54`th one.

```python
with open("TLSB", "rb") as image:
    data = image.read()
    header_data = data[:54] # The data on file info, but that cant have encrypted data in it
    image_body = data[54:]
    
    hidden_data = ""

    for char in image_body:
        hidden_data += str(bin(char))[-3]

    for i in range(0, len(hidden_data), 8):
        print(hidden_data[i:i + 8], end=" ")

``` 

Running this outputs

```text
01001000 01101111 01110000 01100101 00100000 01111001 01101111 01110101 00100000 01101000 01100001 01100100 00100000 01100110 01110101 01101110 00100000 00111010 00101001 00101110 00100000 01010100 01101000 01100101 00100000 01000110 01101100 01100001 01100111 00100000 01101001 01110011 00111010 00100000 01100000 01100011 01000111 01010110 01101010 01011001 01010111 00110101 00110111 01010110 01000111 01100111 00110000 01100100 01000100 01010110 01100110 01100010 01101010 01000010 00110000 01011000 00110000 01110111 01111010 01001110 01000100 01010110 00110000 01011000 00110001 01001101 01111000 01011010 00110010 00110100 01111000 01011010 01101010 01000110 01101010 01001110 01000111 00110101 00110000 01011000 00110010 01001001 01111000 01100100 01000110 00111000 00110001 01100100 01000100 01001110 01101110 01100110 01010001 00111101 00111101 00100111
```

Converting these bytes to unicode gets 

```text
Hope you had fun :). The Flag is: `cGVjYW57VGg0dDVfbjB0X0wzNDV0X1MxZ24xZjFjNG50X2IxdF81dDNnfQ=='
```

This flag is in `base64` and when decrypted becomes `pecan{Th4t5_n0t_L345t_S1gn1f1c4nt_b1t_5t3g}`
