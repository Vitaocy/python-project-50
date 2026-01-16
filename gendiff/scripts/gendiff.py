def generate_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    lines = ['{']

    for key in keys:
        if key not in data1:
            lines.append(f"  + {key}: {data2[key]}")
            continue

        if key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
            continue

        if data1[key] == data2[key]:
            lines.append(f"    {key}: {data1[key]}")
        else:
            lines.append(f"  - {key}: {data1[key]}")
            lines.append(f"  + {key}: {data2[key]}")

    lines.append('}')
    return '\n'.join(lines)