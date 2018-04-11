#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def readlines(file_path):
    with open(file_path, mode='rt', encoding='utf-8') as fh:
        return fh.readlines()


def write_on(dest_path, contents):
    with open(dest_path, mode='wt', encoding='utf-8') as fh:
        fh.write(contents)


def cut(lines, index=0):
    selected_columns = []
    for line in lines:
        if not line:
            continue
        columns = line.split()
        if len(columns) <= index:
            continue
        selected_columns.append(columns[index])
    return '\n'.join(selected_columns)


def main():
    lines = readlines('../hightemp.txt')
    col1 = cut(lines, 0)
    col2 = cut(lines, 1)
    write_on('col1.txt', col1)
    write_on('col2.txt', col2)


if __name__ == "__main__":
    main()
