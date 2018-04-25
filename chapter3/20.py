#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def read(file_path, title):
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            wiki = json.loads(line, encoding='utf-8')
            if wiki['title'] == title:
                return wiki

    raise RuntimeError('specified title is not found. {0}'.format(title))


def main():
    wiki = read('./jawiki-country.json', 'イギリス')
    print(wiki['text'])


if __name__ == "__main__":
    main()
