with open("TLSB", "rb") as image:
    data = image.read()
    header_data = data[:54] # The data on file info, but that cant have encrypted data in it
    image_body = data[54:]
    
    hidden_data = ""

    for char in image_body:
        hidden_data += str(bin(char))[-3]

    for i in range(0, len(hidden_data), 8):
        print(hidden_data[i:i + 8], end=" ")


