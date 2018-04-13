#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def paste(out_file, input_file1, input_file2):
    with open(out_file, mode='wt', encoding='utf-8') as out, \
         open(input_file1, mode='rt', encoding='utf-8') as in1, \
         open(input_file2, mode='rt', encoding='utf-8') as in2:

        for a, b in zip(in1, in2):
            out.write(a.rstrip() + '\t' + b.rstrip() + '\n')


def main():
    paste('../merge.txt', '../col1.txt', '../col2.txt')


if __name__ == "__main__":
    main()
    # 高知県	江川崎
    # 埼玉県	熊谷
    # 岐阜県	多治見
    # 山形県	山形
    # 山梨県	甲府
    # 和歌山県	かつらぎ
    # 静岡県	天竜
    # 山梨県	勝沼
    # 埼玉県	越谷
    # 群馬県	館林
    # 群馬県	上里見
    # 愛知県	愛西
    # 千葉県	牛久
    # 静岡県	佐久間
    # 愛媛県	宇和島
    # 山形県	酒田
    # 岐阜県	美濃
    # 群馬県	前橋
    # 千葉県	茂原
    # 埼玉県	鳩山
    # 大阪府	豊中
    # 山梨県	大月
    # 山形県	鶴岡
    # 愛知県	名古屋
