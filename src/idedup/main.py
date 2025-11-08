#!/usr/bin/env python3
import sys


def print_help():
    help_message = """
Usage : cat textfile.txt | idedup

Arguments:
    None

Options:
    -h, --help:     Show this help message and exit.
    -f, --forward:  dedup forward (print the first occurrence)
    -r, --reverse:  dedup reverse (print the last occurrence)

By default, idedup will behave as 'idedup -f'
"""

    print(help_message)


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("-h", "--help"):
            print_help()
        elif arg in ("-r", "--reverse"):
            idedup_alt(False)
        elif arg in ("-f", "--forward"):
            idedup_alt(True)
        else:
            print_help()
    else:
        idedup_alt(True)


def idedup_alt(first):
    indexed_dedup = dict()
    last_line = 0
    for index, line in enumerate(sys.stdin, start=1):
        line_strip = line.strip()
        last_line = index
        if first:
            if line_strip in indexed_dedup:
                continue

        indexed_dedup[line_strip] = index

    number_of_digit = (last_line // 10) + 5
    for key, value in indexed_dedup.items():
        print(f"{value:>{number_of_digit}}\t{key}")


if __name__ == "__main__":
    main()
