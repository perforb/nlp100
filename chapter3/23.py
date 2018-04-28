#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

SECTION_PATTERN = re.compile(r'^(?P<level>=+)(?P<name>.*?)\1$')


def read(file_path, title):
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            wiki = json.loads(line, encoding='utf-8')
            if wiki['title'] == title:
                return wiki

    raise RuntimeError('specified title is not found. {0}'.format(title))


def find_sections(article):
    sections = {}
    for line in article:
        m = SECTION_PATTERN.match(line)
        if m:
            section_name = m.group('name').strip()
            level = m.group('level').count('=') - 1
            sections[section_name] = level

    return sections


def main():
    wiki = read('./jawiki-country.json', 'イギリス')
    article = wiki['text'].split('\n')
    sections = find_sections(article)
    for name, level in sections.items():
        print('{0}: {1}'.format(level, name))


if __name__ == "__main__":
    main()
    # 1: 国名
    # 1: 歴史
    # 1: 地理
    # 2: 気候
    # 1: 政治
    # 1: 外交と軍事
    # 1: 地方行政区分
    # 2: 主要都市
    # 1: 科学技術
    # 1: 経済
    # 2: 鉱業
    # 2: 農業
    # 2: 貿易
    # 2: 通貨
    # 2: 企業
    # 1: 交通
    # 2: 道路
    # 2: 鉄道
    # 2: 海運
    # 2: 航空
    # 1: 通信
    # 1: 国民
    # 2: 言語
    # 2: 宗教
    # 2: 婚姻
    # 2: 教育
    # 1: 文化
    # 2: 食文化
    # 2: 文学
    # 2: 哲学
    # 2: 音楽
    # 3: イギリスのポピュラー音楽
    # 2: 映画
    # 2: コメディ
    # 2: 国花
    # 2: 世界遺産
    # 2: 祝祭日
    # 1: スポーツ
    # 2: サッカー
    # 2: 競馬
    # 2: モータースポーツ
    # 1: 脚注
    # 1: 関連項目
    # 1: 外部リンク
