#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cut(file_path, index=0):
    selected_columns = []
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            if not line:
                selected_columns.append('')
                continue
            columns = line.split()
            if len(columns) <= index:
                selected_columns.append('')
                continue
            selected_columns.append(columns[index])

    return selected_columns


def main():
    col1 = cut('./hightemp.txt', 0)
    print(sorted(set(col1)))


if __name__ == "__main__":
    main()
    # ['千葉県', '和歌山県', '埼玉県', '大阪府', '山形県', '山梨県', '岐阜県', '愛媛県', '愛知県', '群馬県', '静岡県', '高知県']
