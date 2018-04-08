#!/usr/bin/env python3
# -*- coding: utf-8 -*-

MAGIC_NUMBER = 219
BEGIN_CODE_POINT = ord('a')
END_CODE_POINT = ord('z')


def cipher(letters):
    '''
    Atbash - https://en.wikipedia.org/wiki/Atbash
    '''
    encrypted_letters = []
    for letter in letters:
        code_point = ord(letter)
        if code_point >= BEGIN_CODE_POINT and code_point <= END_CODE_POINT:
            letter = chr(MAGIC_NUMBER - code_point)
        encrypted_letters.append(letter)
    return ''.join(encrypted_letters)


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
