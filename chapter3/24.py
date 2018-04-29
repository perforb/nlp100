#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

MEDIA_PATTERN = \
    re.compile(r'.*(File|ファイル|画像)(:|\s*=\s*)(?P<media_file>.+?)(\|.*|\s*$)')


def read(file_path, title):
    with open(file_path, encoding='utf-8') as fh:
        for line in fh:
            wiki = json.loads(line, encoding='utf-8')
            if wiki['title'] == title:
                return wiki

    raise RuntimeError('specified title is not found. {0}'.format(title))


def find_media_files(article):
    media_files = []
    for line in article:
        m = MEDIA_PATTERN.match(line)
        if m:
            media_file = m.group('media_file').strip()
            media_files.append(media_file)

    return media_files


def main():
    wiki = read('./jawiki-country.json', 'イギリス')
    article = wiki['text'].split('\n')
    media_files = find_media_files(article)
    for f in media_files:
        print(f)


if __name__ == "__main__":
    main()
    # Flag of the United Kingdom.svg
    # Royal Coat of Arms of the United Kingdom.svg
    # Location_UK_EU_Europe_001.svg
    # Battle of Waterloo 1815.PNG
    # The British Empire.png
    # Uk topo en.jpg
    # BenNevis2005.jpg
    # Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
    # Palace of Westminster, London - Feb 2007.jpg
    # David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
    # Soldiers Trooping the Colour, 16th June 2007.jpg
    # Scotland Parliament Holyrood.jpg
    # London.bankofengland.arp.jpg
    # City of London skyline from London City Hall - Oct 2008.jpg
    # Oil platform in the North SeaPros.jpg
    # Eurostar at St Pancras Jan 2008.jpg
    # Heathrow T5.jpg
    # Anglospeak.svg
    # CHANDOS3.jpg
    # The Fabs.JPG
    # PalaceOfWestminsterAtNight.jpg
    # Westminster Abbey - West Door.jpg
    # Edinburgh Cockburn St dsc06789.jpg
    # Canterbury Cathedral - Portal Nave Cross-spire.jpeg
    # Kew Gardens Palm House, London - July 2009.jpg
    # 2005-06-27 - United Kingdom - England - London - Greenwich.jpg
    # Stonehenge2007 07 30.jpg
    # Yard2.jpg
    # Durham Kathedrale Nahaufnahme.jpg
    # Roman Baths in Bath Spa, England - July 2006.jpg
    # Fountains Abbey view02 2005-08-27.jpg
    # Blenheim Palace IMG 3673.JPG
    # Liverpool Pier Head by night.jpg
    # Hadrian's Wall view near Greenhead.jpg
    # London Tower (1).JPG
    # Wembley Stadium, illuminated.jpg
