import json

from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    first_file = json.load(open('examples/file1.json'))
    second_file = json.load(open('examples/file2.json'))
    diff = generate_diff(first_file, second_file)
    result = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
    assert diff.strip() == result.strip()