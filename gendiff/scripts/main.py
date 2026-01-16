import argparse
import json

from gendiff.scripts.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )
    
    args = parser.parse_args()
    
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    # output_format = args.format
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == "__main__":
    main()