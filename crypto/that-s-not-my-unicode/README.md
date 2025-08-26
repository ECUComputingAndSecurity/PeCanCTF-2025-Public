The challenge supplies the below image, and the description hints they are 'ancient symbols' which mean something 'modern'
![image](https://github.com/user-attachments/assets/bbc4fea8-b49d-4ab3-aee8-ddb6ce940cee)

As always when you get an image file, the first step is checking the exif data:
```
exiftool ThatsNotMyUnicode.png
ExifTool Version Number         : 13.10
File Name                       : ThatsNotMyUnicode.png
Directory                       : .
File Size                       : 54 kB
File Modification Date/Time     : 2025:04:12 03:43:42+08:00
File Access Date/Time           : 2025:05:13 19:41:41+08:00
File Inode Change Date/Time     : 2025:05:13 19:02:01+08:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1660
Image Height                    : 566
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 7559
Pixels Per Unit Y               : 7559
Pixel Units                     : meters
Comment                         : That's not Unicode is it?
Image Size                      : 1660x566
Megapixels                      : 0.940
```

This doesn't show anything suspicous, just the comment, `That's not Unicode is it?`.

Reverse image searching the image on google comes up with `Cistercian Cyphers`. Researching into these shows that they are a way to express 4 digit numbers as a single symbol. Here is a conversion image for it:

![image](https://github.com/user-attachments/assets/fed45cfa-ec4b-417e-9ef8-6f3764df8a67)

Converting the symbols into decimal numbers returns:
```
99 71 86 106 89 87 53 55 86 87 52 120 89 122 66 107 77 49 56 48 98 109 82 102 81 122 69 49 100 68 78 121 89 122 70 104 98 105 66 102 82 110 86 117 102 81 61 61
```

Notice that all these numbers are between `52` and `122`. With all the hints about Unicode, my first thought was to try to convert this numbers into characters using them as the index of each unicode character, with just a simple python script:
```
[print(chr(int(i)), end="") for i in "99 71 86 106 89 87 53 55 86 87 52 120 89 122 66 107 77 49 56 48 98 109 82 102 81 122 69 49 100 68 78 121 89 122 70 104 98 105 66 102 82 110 86 117 102 81 61 61".split(" ")]
```

This prints out the base64 code `cGVjYW57VW4xYzBkM180bmRfQzE1dDNyYzFhbiBfRnVufQ==`, decoding this returns the flag: `pecan{Un1c0d3_4nd_C15t3rc1an _Fun}`
