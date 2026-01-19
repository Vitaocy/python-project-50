from gendiff.formats.plain import plain
from gendiff.formats.stylish import stylish


def get_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key not in data1:
            diff[key] = {
                'type': 'added',
                'value': data2[key],
            }

        elif key not in data2:
            diff[key] = {
                'type': 'removed',
                'value': data1[key],
            }

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': 'nested',
                'children': get_diff(data1[key], data2[key]),
            }

        elif data1[key] == data2[key]:
            diff[key] = {
                'type': 'unchanged',
                'value': data1[key],
            }

        else:
            diff[key] = {
                'type': 'changed',
                'old': data1[key],
                'new': data2[key],
            }

    return diff


def generate_diff(data1, data2, format_name='stylish'):
    diff = get_diff(data1, data2)
    
    if format_name == 'stylish' or format_name is None:
        return stylish(diff)

    if format_name == 'plain':
        return plain(diff)

    raise ValueError(f'Unknown format: {format_name}')
