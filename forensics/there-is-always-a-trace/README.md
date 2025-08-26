## Overview

This challenge will help students to learn about RDP's bitmap caching system - which if they haven't heard of it, is definitely something very interesting. Just as a quick explanation of what a RDP bitmap cache is, in summary, images from RDP sessions are cached locally on the client machine to improve performance and reduce latency by avoiding the need to reload the same images repeatedly. This feature dates back to when internet connections were very slow (such as during the dial-up era) and RDP sessions often experienced significant lag.

## How to solve

Now getting into how to solve this challenge, it is actually very simple when you know what the file is. The challenger is provided with the file named "suspiciousfile32.bmc"; doing a quick google search on the .bmc file format, you can easily learn what it is, and there are countless tools that can help extract the 'images' from bitmap cache files.

![Image](https://github.com/user-attachments/assets/f1357389-d051-4634-ab6b-d53598aef989)

As shown in the screenshot, a tool such as "bmc-tools" can be used to extract the images from the given file. The syntax is very simple:

`./bmc-tools.py -s SRC -d DEST [-c COUNT] [-v] [-o] [-b] [-w WIDTH]`

Plugging in values:

`./bmc-tools.py -s suspiciousfile32.bmc -d destinationDirectory`

This will individually extract each image to the specified directory, which is great! However, this challenge was designed so that students would have to do some 'forensics' work and actually put the images together like a puzzle - that is why no singular image will contain the ENTIRE flag but rather a couple of the images will need to be pieced together to reveal a complete view of the flag.

Of course, the challenger can do this manually, or they can use a tool such as BMC-Viewer or `bmc-tools -b`

![Image](https://github.com/user-attachments/assets/9d8bfce2-63c5-4fbe-a0a4-2cbdc271ac89)

All you do is load the file into the tool and specify the correct bits per pixel (BPP) values, sometimes 8 or 16 - but in this case, by looking at the file name, it is 32.

![Image](https://github.com/user-attachments/assets/0bae179a-cade-4e1b-82d8-7f39247f07d1)

As shown, the tool automatically pieces together the images in a grid like format, showing the flag as some sort of name of a file.

## Note (extra visibility)

The challenger should be able to easily make out the flag but for extra visibility they can use the 'color' setting and set it to a solid color like black to get rid of the grids that might make seeing one letter in the flag a bit difficult.

![Image](https://github.com/user-attachments/assets/40ce6916-d5f9-41d2-b8cf-909c6da6ce16)
