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

DESTINATION_MD_FILE = '../vocab.md'
DESTINATION_CSV_FILE = '../vocab.csv'

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

|Uhhuonanjh|Pronunciation|Part of Speech|English|Miscellaneous Notes|
|----------|-------------|--------------|-------|-------------------|
'''

def tablify ():
    data = []

    for filename in CSV_FILES:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data.append(list(reader))

    with open(DESTINATION_MD_FILE, 'w', newline='', encoding='utf-8') as f:
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
                    f.write('.​'.join('<br/>'.join(x.split(';')).split('.')))
                f.write('|\n')

    with open(DESTINATION_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        for i in range(len(data)):
            cat = data[i]
            for line in cat:
                # separate distinct lines (marked w/ semicolon)
                # first 3 separate into distinct entries; final into multiple columns
                lst = []
                for i in range(len(line)):
                    print(line[i])
                    if i == 0:
                        sublines = line[i].split(';')
                        for j in range(len(sublines)):
                            lst.append([sublines[j]])
                    elif i <= 2:
                        sublines = line[i].split(';')
                        for j in range(len(sublines)):
                            lst[j].append(sublines[j])
                    else:
                        for j in range(len(sublines)):
                            lst[j].append(line[i])
                for l in lst:
                    f.write(','.join(l))
                    f.write('\n')
tablify()
