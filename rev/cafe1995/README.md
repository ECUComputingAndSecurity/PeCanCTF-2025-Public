This challenge distributes a Java class file which can be ran by the students to crack a (poorly) encrypted password stored inside the binary.

The password is encrypted using a basic XOR cipher with the key being the numeric value of `0xDECAFBAD`.

This value came to mind about the various [coffee related Hexspeak phrases](https://en.wikipedia.org/wiki/Hexspeak), you can only imagine how popular this must have been with Java developers back in the day.

Running the program with no parameters gives the user a hint on how to provide it with 2 necessary command line arguments (password, and a method name). The method name is reflectively accessed and (intentionally) can try invoke methods that have a totally different than what objects the invocation is providing, causing an error.

The spectacular error handling scenario in the program is simple: most exceptions the user could see running the program as intended will just result in the program printing "MALFUNCTION" then terminating. Just tries to tie it in with the program's theme of the code being terrible inside.

Demo of running with no arguments:

As you can see there is already a hint about "getting the password", this might help the competitor in avoiding the use of the "flag" and/or "get" methods, which are both useless.

The **build1**, **main**, **get**, and **flag** methods are intentionally useless.

The **passwordHint** method is the first the competitors are expected to find their starting path to the solution. It narrows down the possible password argument values to Hexadecimal characters i.e., `0-9A-F`, but indicates one of the characters is not allowed in the actual password (in this case it is secretly `0`).

Then the competitor is expected to enumerate through other available methods and find more information within their outputs. They can use any password to view the hints they intend to provide. For instance, **build2** hints about a bad coffee with a red herring about 'cafe'.

After this, a skilled competitor will find the password is `DECAFBAD` or `0xDECAFBAD` ("decaf bad"), using the `set` method, yielding the flag `pecan{5um4tra-1nd0n3s1a}`.

Thus to solve the challenge just supply the parameters `0xDECAFBAD set` (case sensitive as per Java method reflection).

The challenge is manually brute forcible since the very poor security of an XOR cipher allows the user to just incrementally try changing parts of the key until they gradually reveal the flag.
