#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    letters1 = "パトカー"
    letters2 = "タクシー"
    print(''.join([a + b for a, b in zip(letters1, letters2)]))


# def main():
#     letters1 = "パトカー"
#     letters2 = "タクシー"
#     letters = ""
#     for a, b in zip(letters1, letters2):
#         letters += a + b
#     print(letters)


if __name__ == "__main__":
    main()
    # パタトクカシーー
