input `n` into [factordb](https://factordb.com) to get the factors of N.

recompute the private key used to encrypt the message. Ideally using python etc.
`private_key = pow(e, -1, (p-1)*(q-1))`

now we've recovered the private key, we can decrypt the message.
`message = pow(cipher_text, private_key, n)`

The message has been converted to an integer so it could be encrypted, we reverse it with a function in python like `long_to_bytes(message)` which should retrieve the flag.

This is a nice and simple introduction into RSA encryption, using primes that are just large enough to contain the message and enforces the importance of using large primes in the private key generation.
