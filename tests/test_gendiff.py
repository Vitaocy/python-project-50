from pathlib import Path

from gendiff.scripts.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_test_data(filename):
    return get_test_data_path(filename).read_text()


# def test_generate_diff_old_json():
#     first_file = open_file('examples/file1.json')
#     second_file = open_file('examples/file2.json')
#     diff = generate_diff(first_file, second_file, format_name='plain')
#     expected = read_test_data('result_gendiff.txt')
#     assert diff == expected


# def test_generate_diff_old_yaml():
#     first_file = open_file('examples/file1.yaml')
#     second_file = open_file('examples/file2.yaml')
#     diff = generate_diff(first_file, second_file, format_name='plain')
#     expected = read_test_data('result_gendiff.txt')
#     assert diff == expected


def test_generate_diff_recursive_json_stylish():
    first_file = 'examples/file_recursive1.json'
    second_file = 'examples/file_recursive2.json'
    diff = generate_diff(first_file, second_file)
    assert diff == read_test_data('result_recursive.txt')


def test_generate_diff_recursive_yaml_stylish():
    first_file = 'examples/file_recursive1.yaml'
    second_file = 'examples/file_recursive2.yaml'
    diff = generate_diff(first_file, second_file)
    assert diff == read_test_data('result_recursive.txt')


def test_generate_diff_recursive_json_plain():
    first_file = 'examples/file_recursive1.json'
    second_file = 'examples/file_recursive2.json'
    diff = generate_diff(first_file, second_file, format_name='plain')
    assert diff == read_test_data('result_rec_plain.txt')


def test_generate_diff_recursive_yaml_plain():
    first_file = 'examples/file_recursive1.yaml'
    second_file = 'examples/file_recursive2.yaml'
    diff = generate_diff(first_file, second_file, format_name='plain')
    assert diff == read_test_data('result_rec_plain.txt')


def test_generate_diff_recursive_json_to_json():
    first_file = 'examples/file_recursive1.json'
    second_file = 'examples/file_recursive2.json'
    diff = generate_diff(first_file, second_file, format_name='json')
    assert diff == read_test_data('result_rec_json.txt')


def test_generate_diff_recursive_yaml_to_json():
    first_file = 'examples/file_recursive1.yaml'
    second_file = 'examples/file_recursive2.yaml'
    diff = generate_diff(first_file, second_file, format_name='json')
    assert diff == read_test_data('result_rec_json.txt')