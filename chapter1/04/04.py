#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def main():
    sentence = '''
    Hi He Lied Because Boron Could Not Oxidize Fluorine.
    New Nations Might Also Sign Peace Security Clause.
    Arthur King Can.
    '''
    sentence = re.sub('[,¥.]', '', sentence)
    words = sentence.split()
    indexes = (0, 4, 5, 6, 7, 8, 14, 15, 18)
    elements = {}
    for i in range(len(words)):
        end = 1 if i in indexes else 2
        elements[words[i][:end]] = (i + 1)

    print(elements)


if __name__ == "__main__":
    main()
    # http://www.gadgety.net/shin/trivia/ptable/
    # {
    #   'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8,
    #   'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15,
    #   'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20
    # }
