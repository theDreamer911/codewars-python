import re

def hex_hash(code):
    val_encoded = code.encode("utf-8")
    val_hex = val_encoded.hex()
    score = sum(map(int, re.findall("\d", val_hex)))
    return score