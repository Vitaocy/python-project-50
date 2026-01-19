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