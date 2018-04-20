#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def number_of_lines(file_path):
    with open(file_path, 'rt', encoding='utf-8') as fh:
        return sum(1 for i in fh)


def main():
    print(number_of_lines('./hightemp.txt'))


if __name__ == "__main__":
    main()
    # 24
