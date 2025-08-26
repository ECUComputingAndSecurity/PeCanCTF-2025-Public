As always, when you download a .png file, try checking the exif/meta data. For this I used `exiftool`. You can do this using a command like:

```sh
exiftool SheetMusicCipher.png
```

Once you run this you get an output along the lines of:

```
ExifTool Version Number         : 13.10
File Name                       : SheetMusicCipher.png
Directory                       : .
File Size                       : 162 kB
File Modification Date/Time     : 2025:04:12 03:43:42+08:00
File Access Date/Time           : 2025:04:25 21:06:34+08:00
File Inode Change Date/Time     : 2025:05:01 20:17:52+08:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1535
Image Height                    : 921
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 3777
Pixels Per Unit Y               : 3777
Pixel Units                     : meters
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Orientation                     : Horizontal (normal)
Software                        : Bucking Cipher Encrypter
Comment                         : Note: all the characters are lowercase, and you will need to input '{' after 'pecan' and '}' at the end of the flag as the cipher does not allow special characters
Image Size                      : 1535x921
Megapixels                      : 1.4
```

The comment says:

`Note: all the characters are lowercase, and you will need to input '{' after 'pecan' and '}' at the end of the flag as the cipher does not allow special characters`

This is a good hint, as it means that a non complete or old cipher was used rather than a new one.

Under software, the exifdata has:

`Bucking Cipher Encrypter`

This is a major clue, that the cipher could very well be the 'Bucking Cipher'. Here is a key for the cipher to letters
![image](https://github.com/user-attachments/assets/a79b2a1b-6d84-4150-9c18-10cd9c56e0f9)

By matching the music to the characters you get:
```
?pecanbuckingcipheriscooltoseeinaction??
```

The first bar, and the last two bars appear to be signature bars that define the start and end of the cipher, or they are just padding for the message which doesn't mean anything.

with the flag, you just need to as the exif data comment said, input the `{` and `}`, getting the final flag of:
`pecan{buckingcipheriscooltoseeinaction}`
