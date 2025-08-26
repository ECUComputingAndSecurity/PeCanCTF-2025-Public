result = ""

with open("ascii_value.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        result += chr(number)

print("Decoded string:", result)