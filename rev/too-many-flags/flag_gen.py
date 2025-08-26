from hashlib import sha256
import random

FLAG = "[REDACTED]"

def gen_flags(flag):
    flag_bytes = flag.encode()
    seed = len(flag_bytes) ** 3
    random.seed(seed)
    
    flags = []
    for i in range(seed):
        result = sha256(flag_bytes + bytes(i)).digest()
        result = bytearray(result)
        result[random.randint(0, seed) % len(result)] = flag_bytes[random.randint(0, seed) % len(flag_bytes)]
        flags.append(result.hex())
    return flags

with open("flags.txt", "w") as file:
    file.writelines(', '.join([("pecan{" + f + "}") for f in gen_flags(FLAG)]))
