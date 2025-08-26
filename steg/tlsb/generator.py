with open("TLSB", "wb") as file:
    image_size_pixels = 16
    raw_data = "Hope you had fun :). The Flag is: `cGVjYW57VGg0dDVfbjB0X0wzNDV0X1MxZ24xZjFjNG50X2IxdF81dDNnfQ=='"
    

    #generate actual data to be encoded
    binary_data = ''
    for char in raw_data:
        binary_data += bin(ord(char))[2:].zfill(8)
    #padding so it fits the file size
    binary_data = binary_data.zfill(image_size_pixels ** 2 * 3)


    # header data
    file.write(b"\x42\x4d") # file signature "BM"
    file.write((14 + 40 + 3 * image_size_pixels ** 2).to_bytes(length=4, byteorder="little")) # file size
    file.write(b"\x00" * 4) # unused
    file.write(b"\x36"+ b"\x00" * 3) # the actual picture data offset


    # info header data
    file.write(b"\x28" + b"\x00" * 3) # constant size of the file header data
    file.write(chr(image_size_pixels).encode() + b"\x00" * 3) # width in pixels
    file.write(chr(image_size_pixels).encode() + b"\x00" * 3) # height in pixels
    file.write(b"\x01\x00") # number of planes (?)
    file.write(b"\x18\x00") # Bits per Pixel (\0x18 for RGB using a byte each (24 bits))
    file.write(b"\x00" * 4) # compression;  0 = no compression
    file.write(b"\x00" * 4) # compressed image size; set to 0 if no compression
    file.write(b"\x10" + b"\x00" * 3) # horizontal resolution: Pixels/meter
    file.write(b"\x10" + b"\x00" * 3) # vertical resolution: Pixels/meter
    file.write(b"\x00" * 8) # absolutely no idea what colours used and important colours means


    print("Encoded:", binary_data)
    #actual image data
    for i in range(image_size_pixels):
        for j in range(image_size_pixels):
            default_value = b"\x00" * 2 + b"\xff"
            edited_value = b''
            for k in range(3):
                edited_value += ((default_value[k] & 0b11111011) | 0b000000100 * int(binary_data[i * 48 + j * 3 + k])).to_bytes()
            file.write(edited_value) # write the pixel to the file
