#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.cli import create_parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
