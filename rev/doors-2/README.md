This is a continuation of Doors (1).
This challange takes a step into actual reverse engineering, users should start by understanding how the `GetObfuscatedSalt` and `IsValidKey` functions work. This should lead them to understanding that each key is unique to the username entered and is salted with some other text.

Next, they should decode the bytecode for the ObfuscatedSalt to get the salt phrase.
Finally the user can concatenate the salt onto their own username of choice and encode it in base64.
This base64 string, when entered into the program with their username will retrieve and decrypt the flag from memory.

More advanced users may skip the authorisation step entirely and patch out the licence check and print the flag directly. This is still in the spirit of the reversing challange but is more intended for part 3.