#!/usr/bin/env python

import sys
import argparse
import os

def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def wc(text):
    num_lines = count_lines(text)
    num_words = count_words(text)
    num_characters = count_characters(text)
    
    return num_lines, num_words, num_characters

def process_file(file, args):
    text = file.read()
    counts = wc(text)

    output = []
    if args.lines:
        output.append(str(counts[0]))
    if args.words:
        output.append(str(counts[1]))
    if args.characters:
        output.append(str(counts[2]))

    if not output:
        output = [str(count) for count in counts]

    return output

def main():
    parser = argparse.ArgumentParser(description='A Python implementation of the wc utility.')
    parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help='Filenames to read from. If omitted, will read from STDIN.')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the number of lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count the number of words')
    parser.add_argument('-c', '--characters', action='store_true', help='Count the number of characters')

    args = parser.parse_args()

    total_counts = [0, 0, 0]

    for file in args.files:
        output = process_file(file, args)
        total_counts = [total + int(count) for total, count in zip(total_counts, output)]
        print(f"{' '.join(output)} {file.name}")

    if len(args.files) > 1:
        print(f"{' '.join(map(str, total_counts))} total")

if __name__ == '__main__':
    main()
