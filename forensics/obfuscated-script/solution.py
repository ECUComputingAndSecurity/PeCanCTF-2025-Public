with open('encrypted_flag.txt', 'r') as file:
    encrypted_flag_bytes = file.read()
    print(encrypted_flag_bytes)
flag = ""
key_XOR = 73
for i in encrypted_flag_bytes:
    print(str(ord(i)) + "---" + str(i))
    flag += chr(ord(i) ^ key_XOR)

print(flag)
            