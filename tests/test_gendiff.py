from pathlib import Path

from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsers import open_file


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_test_data(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_plain_json():
    first_file = open_file('examples/file1.json')
    second_file = open_file('examples/file2.json')
    diff = generate_diff(first_file, second_file, format_name='plain')
    expected = read_test_data('result_gendiff.txt')
    assert diff == expected


def test_generate_diff_plain_yaml():
    first_file = open_file('examples/file1.yaml')
    second_file = open_file('examples/file2.yaml')
    diff = generate_diff(first_file, second_file, format_name='plain')
    expected = read_test_data('result_gendiff.txt')
    assert diff == expected


def test_generate_diff_recursive_json():
    first_file = open_file('examples/file_recursive1.json')
    second_file = open_file('examples/file_recursive2.json')
    diff = generate_diff(first_file, second_file)
    expected = read_test_data('result_recursive.txt')
    assert diff == expected


def test_generate_diff_recursive_yaml():
    first_file = open_file('examples/file_recursive1.yaml')
    second_file = open_file('examples/file_recursive2.yaml')
    diff = generate_diff(first_file, second_file)
    expected = read_test_data('result_recursive.txt')
    assert diff == expected