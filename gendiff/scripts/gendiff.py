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
    

def plain(diff):
    lines = ['{']

    for key, node in diff.items():
        t = node['type']

        if t == 'added':
            lines.append(f"  + {key}: {str(node['value'])}")
        elif t == 'removed':
            lines.append(f"  - {key}: {str(node['value'])}")
        elif t == 'unchanged':
            lines.append(f"    {key}: {str(node['value'])}")
        elif t == 'changed':
            lines.append(f"  - {key}: {str(node['old'])}")
            lines.append(f"  + {key}: {str(node['new'])}")

    lines.append('}')
    return '\n'.join(lines)


def stringify(value, depth):
    if not isinstance(value, dict):
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        if value is None:
            return 'null'
        return str(value)

    indent = ' ' * (depth * 4)
    lines = ['{']

    for key, val in value.items():
        lines.append(f"{indent}    {key}: {stringify(val, depth + 1)}")

    lines.append(f"{indent}}}")
    return '\n'.join(lines)


def stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    lines = ['{']

    for key, node in diff.items():
        node_type = node['type']

        if node_type == 'added':
            lines.append(
                f"{indent}  + {key}: {stringify(node['value'], depth + 1)}"
            )

        elif node_type == 'removed':
            lines.append(
                f"{indent}  - {key}: {stringify(node['value'], depth + 1)}"
            )

        elif node_type == 'unchanged':
            lines.append(
                f"{indent}    {key}: {stringify(node['value'], depth + 1)}"
            )

        elif node_type == 'changed':
            lines.append(
                f"{indent}  - {key}: {stringify(node['old'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: {stringify(node['new'], depth + 1)}"
            )

        elif node_type == 'nested':
            lines.append(
                f"{indent}    {key}: {stylish(node['children'], depth + 1)}"
            )

    lines.append(f"{indent}}}")
    return '\n'.join(lines)