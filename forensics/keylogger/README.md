1
Challenge name: Keylogger
Evidence:\
Capture.pcappng  -- MD5: F5C3951414AC5740692E1DF3F6A1F9B9
Solution:
Use wireshark to open the capture.pcappng

Attacker IP: 192.168.126.148
Victim IP: 192.168.126.129

Then Right click -> Follow -> TCP Stream
In TCP Stream 1, we can see that the victim machine (192.168.126.129) downloaded a file
called keylogger.py from the attacker machine (192.168.126.148).

To extract this file from wireshark, follow those steps:
File -> Export Objects -> Http

Save the file and open it in VSCode. Focus on the Encode() function:

As we can see in keylogger.py, it captures the victim's keystrokes and writes them to a file
called keystroke.txt. This file is then encoded, and the result is saved in
keystroke_encoded.txt. The keystroke_encoded.txt file is subsequently transferred to the
attacker's machine (192.168.126.148). We can observe this in TCP stream 2.