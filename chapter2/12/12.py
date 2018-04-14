#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cut(file_path, index=0):
    selected_columns = []
    with open(file_path, mode='rt', encoding='utf-8') as fh:
        for line in fh:
            if not line:
                selected_columns.append('')
                continue
            columns = line.split()
            if len(columns) <= index:
                selected_columns.append('')
                continue
            selected_columns.append(columns[index])

    return '\n'.join(selected_columns)


def main():
    with open('../col1.txt', mode='wt', encoding='utf-8') as f1, \
         open('../col2.txt', mode='wt', encoding='utf-8') as f2:

        col1 = cut('../hightemp.txt', 0)
        col2 = cut('../hightemp.txt', 1)
        f1.write(col1)
        f2.write(col2)


if __name__ == "__main__":
    main()
    # cat ../hightemp.txt | cut -f1
    # cat ../hightemp.txt | cut -f2
