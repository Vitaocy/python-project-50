import json
from pathlib import Path

import yaml


def open_file(filepath):
    path = Path(filepath)
    suffix = path.suffix.lower()

    if suffix == '.json':
        return json.load(open(filepath))
    if suffix in ('.yaml', '.yml'):
        return yaml.safe_load(open(filepath))

    raise ValueError(f'Unsupported file format: {suffix}')
