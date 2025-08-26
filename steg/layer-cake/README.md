This challenge involves the use of five cryptographic methods (Base64, Hex, Caesar cipher, Steganography, and Hexahue cipher).

The user will be provided with a zip folder containing 2 files. A word file called "Colour Palette" and an JPG named "Juius Caesar."
The word file contains this image:

![Image](https://github.com/user-attachments/assets/82343323-149c-47ca-97c0-e74b6cdf34b6)

Essentially this is a cryptography technique known as Hexahue cipher which encodes characters through a series of colours.

![Image](https://github.com/user-attachments/assets/9ceb55d5-6e32-4f2c-8238-2d6adfa299d5)

Users can easily find this technique by searching the web.

![Image](https://github.com/user-attachments/assets/5cb101be-aeb2-4ee2-8cfd-9105b5674187)

Decrypting the Hexahue cipher will give you this text encoded via Caesar cipher "TIHwcYXu6973707265747479636H6H6E"

To decode this text the user will need to either manually or use a website to decode the cipher.
Unfortunately they will realise that the Caesar cipher requires a special key to encode the provided text.

![Image](https://github.com/user-attachments/assets/356fbe6e-9ae8-459e-a541-3cae2c8e00ca)

The key will be hidden within the Juilius Caesar image via a technique known as Steganography. Basically, do some research to figure out how data can be hidden within an image, go to a website like this to upload and decode it.

![Image](https://github.com/user-attachments/assets/08f94f9d-ee46-4bca-a01e-79dda4f369e1)

You'll end up getting the key:

![Image](https://github.com/user-attachments/assets/94af4d9f-2c9e-4292-a0f3-08b1247a7b75)

Head to a website, enter the text and key, and you'll get this:

![Image](https://github.com/user-attachments/assets/865af3ca-ab75-4dda-9b41-4ee8dbda7f37)

This is the final stretch of the challenge, the user will be provided this text "RGFuaWVs6973707265747479636F6F6C" which is a combination of Base64 and Hex. The "RGFuaWVs" section is base 64, while "6973707265747479636F6F6C" is Hex.
Decoding both algorithms will provide the flag "Danielisprettycool"
