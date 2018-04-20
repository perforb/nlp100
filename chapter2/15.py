#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tail(input_file, n=10):
    with open(input_file, encoding='utf-8') as fh:
        lines = fh.readlines()
        return ''.join(lines[-n:])


def main():
    result = tail('./hightemp.txt', 3)
    print(result)


if __name__ == "__main__":
    main()
    # 山梨県  大月    39.9    1990-07-19
    # 山形県  鶴岡    39.9    1978-08-03
    # 愛知県  名古屋  39.9    1942-08-02
