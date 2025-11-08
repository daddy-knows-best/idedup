#!/usr/bin/env python3
import sys


def main():
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
