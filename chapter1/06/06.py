#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def n_gram(sentence, n):
    return [sentence[i:(i + n)] for i in range(0, len(sentence), n)]


def main():
    x = set(n_gram('paraparaparadise', 2))
    y = set(n_gram('paragraph', 2))

    union = x | y
    intersection = x & y
    difference = x - y

    print(x)
    print(y)
    print(union)
    print(intersection)
    print(difference)
    print("Is 'se' inclueded in x? {}".format('se' in x))
    print("Is 'se' inclueded in y? {}".format('se' in y))


if __name__ == "__main__":
    main()
    # {'di', 'se', 'ra', 'pa'}
    # {'ap', 'ra', 'gr', 'h', 'pa'}
    # {'ap', 'ra', 'di', 'se', 'gr', 'h', 'pa'}
    # {'ra', 'pa'}
    # {'se', 'di'}
    # Is 'se' inclueded in x? True
    # Is 'se' inclueded in y? False
