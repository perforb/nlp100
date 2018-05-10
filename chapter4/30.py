#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read(file_path):
    with open(file_path, encoding='utf-8') as fh:
        return fh.read()


def parse(text):
    pass


def main():
    text = read('./neko.txt.mecab')
    print(text)


if __name__ == "__main__":
    main()
