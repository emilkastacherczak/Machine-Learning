#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}

    vocabulary_dict = {}
    with open("data/vocab.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            vocabulary_dict[int(row[0])] = row[1]

    return vocabulary_dict

#print(get_vocabulary_dict())