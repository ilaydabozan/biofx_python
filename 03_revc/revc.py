#!/usr/bin/env python3
"""
Author : ilaydabozan <ilaydabozan@localhost>
Date   : 2021-10-13
Purpose: Print the reverse complement of DNA
"""

import argparse
import os
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='Input sequence or file')

    args = parser.parse_args()

    # To catch if the input is file
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    trans = {
        'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
        'a': 't', 'c': 'g', 'g': 'c', 't': 'a'
    }
    complement=''
    for base in args.dna:
        complement += trans.get(base, base)

    # List Comprehension
    # print(''.join(reversed([trans.get(base, base) for base in args.dna])))

    print(''.join(reversed(complement)))

# --------------------------------------------------
if __name__ == '__main__':
    main()

