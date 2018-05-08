#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import requests


def read(file_path, title):
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            wiki = json.loads(line, encoding='utf-8')
            if wiki['title'] == title:
                return wiki

    raise RuntimeError('specified title is not found. {0}'.format(title))


def extract_basic_info(article):
    basic_info = {}
    m = re.search(r'{{基礎情報[^\|]+\|(.+?)\n}}', article, flags=re.DOTALL)
    if m:
        info_group = m.group(1).split('\n|')
        for info in info_group:
            key, value = re.split(r'\s+=\s+', info)
            value = remove_emphasis(value)
            value = remove_internal_link(value)
            value = remove_external_link(value)
            value = remove_html_tag(value)
            value = remove_stub(value)
            basic_info[key] = value

    return basic_info


def remove_emphasis(value):
    return re.sub(r"'{2,}", '', value)


def remove_internal_link(value):
    return re.sub(
        r'\[\[([^]]+)\]\]',
        lambda m: m.group(1).split('|')[-1],
        value
    )


def remove_external_link(value):
    return re.sub(r'\[([^[]+)\]', '', value)


def remove_html_tag(value):
    return re.sub(r'<.*>|<\/.*>|<(.*)\s+(.*)\/>', '', value)


def remove_stub(value):
    return re.sub(
        r'\*{0,}\{\{(.+?)\}\}',
        lambda m: m.group(1).split('|')[-1],
        value,
        flags=re.MULTILINE
    )


def get_imageinfo(file_name):
    payload = {
        'action': 'query',
        'titles': 'File:' + file_name,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    r = requests.get('https://www.mediawiki.org/w/api.php', params=payload)
    body = json.loads(r.text, encoding='utf-8')
    return body['query']['pages']['-1']['imageinfo'][0]


def main():
    wiki = read('./jawiki-country.json', 'イギリス')
    article = wiki['text']
    basic_info = extract_basic_info(article)
    file_name = basic_info['国旗画像']
    info = get_imageinfo(file_name)

    print(info['url'])


if __name__ == "__main__":
    main()
    # {   'continue': {'continue': '||', 'iistart': '2007-09-03T09:51:34Z'},
    #     'query': {   'pages': {   '-1': {   'imageinfo': [   {   'descriptionshorturl': 'https://commons.wikimedia.org/w/index.php?curid=347935',
    #                                                              'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Flag_of_the_United_Kingdom.svg',
    #                                                              'url': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg'}],
    #                                         'imagerepository': 'shared',
    #                                         'known': '',
    #                                         'missing': '',
    #                                         'ns': 6,
    #                                         'title': 'File:Flag of the United '
    #                                                  'Kingdom.svg'}}}}
    # https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg
