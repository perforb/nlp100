#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def head(input_file, n=10):
    with open(input_file, encoding='utf-8') as fh:
        lines = []
        for index, line in enumerate(fh):
            if index > (n - 1):
                break
            lines.append(line)
        return ''.join(lines)


def main():
    result = head('../hightemp.txt', 3)
    print(result)


if __name__ == "__main__":
    main()
    # 高知県  江川崎  41      2013-08-12
    # 埼玉県  熊谷    40.9    2007-08-16
    # 岐阜県  多治見  40.9    2007-08-16
