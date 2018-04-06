#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def format(x, y, z):
    return '{0}時の{1}は{2}'.format(x, y, z)


def main():
    forecast = format(12, '気温', 22.4)
    print(forecast)


if __name__ == "__main__":
    main()
    # 12時の気温は22.4
