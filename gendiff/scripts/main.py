from gendiff.scripts.cli import parse_args
from gendiff.scripts.gendiff import generate_diff


def main():
    args = parse_args()

    first_file = args.first_file
    second_file = args.second_file
    output_format = args.format

    diff = generate_diff(first_file, second_file, output_format)
    print(diff)


if __name__ == "__main__":
    main()