#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

MAGIC_NUMBER = 219


def cipher(letters):
    '''
    Atbash - https://en.wikipedia.org/wiki/Atbash
    '''
    return re.sub(r'[a-z]',
                  lambda m: chr(MAGIC_NUMBER - ord(m.group(0))),
                  letters)


# def cipher(letters):
#     '''
#     Atbash - https://en.wikipedia.org/wiki/Atbash
#     '''
#     begin_code_point = ord('a')
#     end_code_point = ord('z')
#     encrypted_letters = []
#     for letter in letters:
#         code_point = ord(letter)
#         if code_point >= begin_code_point and code_point <= end_code_point:
#             letter = chr(MAGIC_NUMBER - code_point)
#         encrypted_letters.append(letter)
#     return ''.join(encrypted_letters)


def main():
    letters = 'Python is awesome!'
    encrypted_letters = cipher(letters)
    decrypted_letters = cipher(encrypted_letters)

    print(letters)
    print(encrypted_letters)
    print(decrypted_letters)


if __name__ == "__main__":
    main()
    # Python is awesome!
    # Pbgslm rh zdvhlnv!
    # Python is awesome!
