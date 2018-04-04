#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def normalize(sentence):
    return re.sub(r'[,\.]', '', sentence)


def n_gram(sentence, n):
    words = normalize(sentence).split()
    word_n_gram = [words[i:(i + n)] for i in range(0, len(words), n)]
    letter_n_gram = [sentence[i:(i + n)] for i in range(0, len(sentence), n)]
    return word_n_gram, letter_n_gram


def main():
    sentence = 'I am an NLPer'
    word_bi_gram, letter_n_gram = n_gram(sentence, 2)

    print(word_bi_gram)
    print(letter_n_gram)


if __name__ == "__main__":
    main()
    # [['I', 'am'], ['an', 'NLPer']]
    # ['I ', 'am', ' a', 'n ', 'NL', 'Pe', 'r']
