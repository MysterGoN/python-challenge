# Start page: http://www.pythonchallenge.com/pc/def/274877906944.html

# See https://en.wikipedia.org/wiki/Caesar_cipher

# 1. Caesar cipher decryption

import re

TASK_STEP = 2


def decrypt_caesar_cipher(char: str, step: int):
    res_code = ord(char.lower()) + step

    while True:
        if ord('a') <= res_code <= ord('z'):
            return chr(res_code)
        elif res_code < ord('a'):
            res_code = ord('z') - (ord('a') - res_code) + 1
        elif res_code > ord('z'):
            res_code = res_code - ord('z') + ord('a') - 1

def is_letter(char: str):
    return re.search(r'^[a-zA-z]$', char)


cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decryption = ''
for char in cipher:
    if is_letter(char):
        char = decrypt_caesar_cipher(char, TASK_STEP)
    decryption += char

print(decryption)
