#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import sample


def __shuffle(word):
    if len(word) <= 4:
        return word

    head = word[0]
    body = word[1:-1]
    tail = word[-1]
    return head + ''.join(sample(body, len(body))) + tail


def typoglycemia(sentence):
    return ' '.join(map(__shuffle, sentence.split()))


# def typoglycemia(sentence):
#     result = []
#     words = sentence.split()
#     for word in words:
#         if len(word) <= 4:
#             result.append(word)
#         else:
#             head = word[0]
#             body = word[1:-1]
#             tail = word[-1]
#             result.append(head + ''.join(sample(body, len(body))) + tail)
#     return ' '.join(result)


def main():
    sentence = "I couldn't believe that I could actually understand what " \
               "I was reading : the phenomenal power of the human mind ."

    print(sentence)
    print(typoglycemia(sentence))


if __name__ == "__main__":
    main()
    # I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .
    # I cd'ounlt bilevee that I could aatlulcy unnsrdtaed what I was rniedag : the pnaoemehnl poewr of the haumn mind .
