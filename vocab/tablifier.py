# -*- coding: utf-8 -*-
"""
author: Andi Zhou

Basic tablifier to turn csvs into md tables
"""

import csv

CSV_FILES = [
    '1 - Basic.csv',
    '2 - Nature.csv',
    '3 - Mythology.csv',
    '4 - Agriculture.csv',
    '5 - Society.csv',
    '6 - Industry.csv',
]

DESTINATION_FILE = '../vocab.md'

SECTION_HEADINGS = [
    'Basic Vocabulary',
    'Nature and Environment',
    'Mythology',
    'Food and Agriculture',
    'People and Society',
    'Industry',
]

HEADER = '''
# Uhhuonanjh Vocabulary

'''

SECTION_HEADER = '''

|Uhhuonanjh|Pronunciation|Part of Speech|English|Explanation|Notes|
|----------|-------------|--------------|-------|-----------|-----|
'''

def tablify ():
    data = []

    for filename in CSV_FILES:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data.append(list(reader))

    with open(DESTINATION_FILE, 'w', newline='', encoding='utf-8') as f:
        f.write(HEADER)
        for i in range(len(data)):
            cat = data[i]
            f.write('## ' + SECTION_HEADINGS[i] + SECTION_HEADER)
            for line in cat:
                if line == []:
                    continue
                # separate distinct lines (marked w/ semicolon)
                for x in line:
                    f.write('|')
                    f.write('<br/>'.join(x.split(';')))
                f.write('|\n')
tablify()
