import random

with open("flags.txt", "r") as file:
    flags = []
    for line in file.readlines():
        for flag in line.split(', '):
            flags.append(bytearray(bytes.fromhex(flag.replace("pecan{", "").replace("}", ""))))

    seed = len(flags)
    flag_len = int(round(seed ** (1/3)))
    random.seed(seed)

    result = bytearray(b'*' * flag_len)
    for i in range(seed):
        # Setter random is generated first. Order needs to be reversed from generation.
        result_rand = random.randint(0, seed)
        result[result_rand % flag_len] = flags[i][random.randint(0, seed) % len(flags[i])]

    print(result.decode())
