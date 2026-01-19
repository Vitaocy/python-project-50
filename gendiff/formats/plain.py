def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff):
    def inner(diff, parent_path=''):
        lines = []

        for key, node in diff.items():
            t = node['type']
            full_path = f"{parent_path}.{key}" if parent_path else key

            if t == 'added':
                lines.append(
                    f"Property '{full_path}' was added with value: "
                    f"{format_value(node['value'])}"
                )

            elif t == 'removed':
                lines.append(
                    f"Property '{full_path}' was removed"
                )

            elif t == 'changed':
                old = format_value(node['old'])
                new = format_value(node['new'])
                lines.append(
                    f"Property '{full_path}' was updated. "
                    f"From {old} to {new}"
                )

            elif t == 'nested':
                lines.extend(
                    inner(node['children'], full_path)
                )

        return lines

    return '\n'.join(inner(diff))