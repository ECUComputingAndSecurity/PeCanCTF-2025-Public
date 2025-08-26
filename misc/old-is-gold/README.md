The unreadable text in the end of the file is a sequence of Vi(m) commands that should be applied to the text with the cursor on the first character, starting in Normal mode. The sequence is encoded using ROT47 with 45 characters offset. With careful execution of those commands, which after decoding read

dtl . f' BB Fe 2h r 0 w dtA :s/less/s <ENTER> 0 f- vtg d 2e d$ daW yaW FT e p w d3W el c$} <ESC> 0 f. x :s/ /_/g <ENTER> i pecan{

, the flag is obtained.

Note that this is possible to bruteforce on Cyberchef using the crib "pecan" or "ENTER". The hint to use ROT47 is given in the challenge description.