#!/usr/bin/python3

def hex_at(string, index, mode):
    if (mode == 0):
        r = string[index:2]
    else:
        r = string[index-2:index]
    return int(r, 16)

def decrypt(ciphertext):
    output = ""
    i = 2
    key = hex_at(ciphertext, 0, 0)
    while i < len(ciphertext):
        i += 2
        plaintext = hex_at(ciphertext, i, 1) ^ key
        output += chr(plaintext)
    return output;


print(decrypt("6e040b1d1d0b040b1d1d0b5f5c5d2e09030f0702400d0103"))
