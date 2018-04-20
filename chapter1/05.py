#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def n_gram(sentence, n):
    return [sentence[i:(i + n)] for i in range(0, len(sentence), n)]


def main():
    word_bi_gram = n_gram(['I', 'am', 'an', 'NLPer'], 2)
    letter_bi_gram = n_gram('I am an NLPer', 2)

    print(word_bi_gram)
    print(letter_bi_gram)


if __name__ == "__main__":
    main()
    # [['I', 'am'], ['an', 'NLPer']]
    # ['I ', 'am', ' a', 'n ', 'NL', 'Pe', 'r']
