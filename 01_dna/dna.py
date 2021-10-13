#!/usr/bin/env python3
"""Tetranucleotide frequency"""

import argparse
import os
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    args = parser.parse_args()

        # Call open() to open a filehandle,
        # then chain the fh.read() method to return a string,
        # then chain the str.rstrip() method to remove trailing whitespace.
    if os.path.isfile(args.dna):
        args.dna = open(args.dna,'r',encoding='utf8').read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
# The main function has no return statement it returns the default None value.
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    print(str(args.dna.upper().count('A')),
        str(args.dna.upper().count('C')),
        str(args.dna.upper().count('G')),
        str(args.dna.upper().count('T')), sep=' ')


# --------------------------------------------------
if __name__ == '__main__':
    main()
