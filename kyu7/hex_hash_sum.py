import re

def hex_hash(code):
    val_encoded = code.encode("utf-8")
    val_hex = val_encoded.hex()
    score = sum(map(int, re.findall("\d", val_hex)))
    return score


def hex_hash(code):
    return sum(int(d) for c in code for d in hex(ord(c)) if d.isdigit())

print(hex_hash("Hello, World!"))