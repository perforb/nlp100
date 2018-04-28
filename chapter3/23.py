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
    # 国名 1
    # 歴史 1
    # 地理 1
    # 気候 2
    # 政治 1
    # 外交と軍事 1
    # 地方行政区分 1
    # 主要都市 2
    # 科学技術 1
    # 経済 1
    # 鉱業 2
    # 農業 2
    # 貿易 2
    # 通貨 2
    # 企業 2
    # 交通 1
    # 道路 2
    # 鉄道 2
    # 海運 2
    # 航空 2
    # 通信 1
    # 国民 1
    # 言語 2
    # 宗教 2
    # 婚姻 2
    # 教育 2
    # 文化 1
    # 食文化 2
    # 文学 2
    # 哲学 2
    # 音楽 2
    # イギリスのポピュラー音楽 3
    # 映画 2
    # コメディ 2
    # 国花 2
    # 世界遺産 2
    # 祝祭日 2
    # スポーツ 1
    # サッカー 2
    # 競馬 2
    # モータースポーツ 2
    # 脚注 1
    # 関連項目 1
    # 外部リンク 1
