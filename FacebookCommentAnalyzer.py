#!/usr/bin/env python

"""A simple python script template.
"""

from __future__ import print_function
import os
import sys
import argparse
from unicodedata import numeric


def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-h', '--help', help='show help')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))