#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def main():
    sentence = '''
    Now I need a drink, alcoholic of course,
    after the heavy lectures involving quantum mechanics.
    '''
    sentence = re.sub('[,¥.]', '', sentence)
    pi = [len(word) for word in sentence.split()]
    print('{0}.{1}'.format(pi[0], ''.join(str(number) for number in pi[1:])))


if __name__ == "__main__":
    main()
    # 3.14159265358979
