#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


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
    columns = cut('./hightemp.txt')
    counter = Counter(columns)
    for pref, count in counter.most_common():
        print(pref, count)


if __name__ == "__main__":
    main()
    # 埼玉県 3
    # 山形県 3
    # 山梨県 3
    # 群馬県 3
    # 岐阜県 2
    # 静岡県 2
    # 愛知県 2
    # 千葉県 2
    # 高知県 1
    # 和歌山県 1
    # 愛媛県 1
    # 大阪府 1
