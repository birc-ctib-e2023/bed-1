"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line
)


def process_lines(infile: TextIO, outfile: TextIO) -> None:
    """Write all lines from `infile` to `outfile` (but tab-separated)."""
    pass  # FIXME: your job is to implement this. Hint: it involves a loop
    for line in infile:
        print_line(parse_line(line), outfile)


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Cleans up a BED file")
    # 'infile' is either provided as an input file name or stdin
    argparser.add_argument('infile',
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('r'),  # file for reading
                           default=sys.stdin)
    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('outfile',
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    process_lines(args.infile, args.outfile)


if __name__ == '__main__':
    main()
