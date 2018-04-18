#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def split(input_file, n=10, prefix='out', suffix='.txt'):
    with open(input_file, encoding='utf-8') as fin:
        lines = []
        seq = 1
        for i, line in enumerate(fin):
            lines.append(line)
            if (i + 1) % n == 0:
                file_name = prefix + str(seq) + suffix
                with open(file_name, mode='wt', encoding='utf-8') as fout:
                    fout.write(''.join(lines))
                    lines.clear()
                    seq += 1

        if lines:
            file_name = prefix + str(seq) + suffix
            with open(file_name, mode='wt', encoding='utf-8') as fout:
                fout.write(''.join(lines))


def main():
    n = int(sys.argv[1])
    split('../hightemp.txt', n)


if __name__ == "__main__":
    main()
