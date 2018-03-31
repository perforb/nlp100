#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def main():
    sentence = '''
    Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.
    '''
    sentence = re.sub('[,¥.]', '', sentence)
    counter = [len(word) for word in sentence.split()]
    print(counter)


if __name__ == "__main__":
    main()
