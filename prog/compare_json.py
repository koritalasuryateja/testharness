#!/usr/bin/env python

import json
import difflib
import argparse
import sys

def compare_json(file1_text, file2_text):
    try:
        json_obj1 = json.loads(file1_text)
        json_obj2 = json.loads(file2_text)
    except json.JSONDecodeError as e:
        return f"Error parsing JSON: {e}"

    diff = list(difflib.unified_diff(
        json.dumps(json_obj1, indent=2).splitlines(),
        json.dumps(json_obj2, indent=2).splitlines(),
        lineterm='',
    ))

    return '\n'.join(diff)

def main():
    parser = argparse.ArgumentParser(description='Compare two JSON files and print the differences.')
    parser.add_argument('file1', help='The first JSON file.')
    parser.add_argument('file2', help='The second JSON file.')

    args = parser.parse_args()

    try:
        with open(args.file1, 'r') as file1, open(args.file2, 'r') as file2:
            json_text1 = file1.read()
            json_text2 = file2.read()
            differences = compare_json(json_text1, json_text2)
            print(differences)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(2)  # Exit with a non-zero status to indicate an error

if __name__ == '__main__':
    main()
