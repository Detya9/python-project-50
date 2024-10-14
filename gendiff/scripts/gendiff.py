#!/usr/bin/env python3
from gendiff.brains import generate_diff
from gendiff.cli import create_parser


def main():
    parser = create_parser()
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
