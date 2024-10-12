#!/usr/bin/env python3
import argparse
from gendiff.brains import generate_diff

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')


def main():
    args = parser.parse_args()
    if args.format == 'stylish':
        diff = generate_diff(args.first_file, args.second_file, 'stylish')
    elif args.format == 'plain':
        diff = generate_diff(args.first_file, args.second_file, 'plain')
    elif args.format == 'json':
        diff = generate_diff(args.first_file, args.second_file, 'json')
    else:
        diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
