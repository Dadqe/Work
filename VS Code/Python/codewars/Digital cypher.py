# https://www.codewars.com/kata/592e830e043b99888600002d/train/python
from string import ascii_lowercase

def encode(message, key):
    key_encode = []
    key = str(key)
    key2 = [int(k) for k in key * (len(message) // len(key) + 1)]
    for ch in message:
        first_index = key_encode.append(ascii_lowercase.index(ch) + 1)

    list_encode = [x + y for x, y in zip(key_encode, key2)]
    return list_encode

print(encode('masterpiece', 1939))
