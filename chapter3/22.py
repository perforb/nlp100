#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

CATEGORY_PATTERN = re.compile(r'^\[\[Category:(.*?)(\|.*)*\]\]$')


def read(file_path, title):
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            wiki = json.loads(line, encoding='utf-8')
            if wiki['title'] == title:
                return wiki

    raise RuntimeError('specified title is not found. {0}'.format(title))


def find_categories(lines):
    category_lines = [line for line in lines if 'Category' in line]
    categories = []

    for line in category_lines:
        m = CATEGORY_PATTERN.match(line)
        if m:
            categories.append(m.group(1))

    return categories


def main():
    wiki = read('./jawiki-country.json', 'イギリス')
    lines = wiki['text'].split('\n')
    categories = find_categories(lines)
    print('\n'.join(categories))


if __name__ == "__main__":
    main()
