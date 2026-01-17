import json
import yaml
from pathlib import Path

from gendiff.scripts.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_json():
    first_file = json.load(open('examples/file1.json'))
    second_file = json.load(open('examples/file2.json'))
    diff = generate_diff(first_file, second_file)
    result = read_file('result_gendiff.txt')
    assert diff == result

def test_generate_diff_yaml():
    first_file = yaml.safe_load(open('examples/file1.yaml'))
    second_file = yaml.safe_load(open('examples/file2.yaml'))
    diff = generate_diff(first_file, second_file)
    result = read_file('result_gendiff.txt')
    assert diff == result