import json
import yaml
from pathlib import Path


def open_file(filepath):
    path = Path(filepath)
    suffix = path.suffix.lower()

    if suffix == '.json':
        return json.load(open(filepath))
    if suffix in ('.yaml', '.yml'):
        return yaml.safe_load(open(filepath))

    raise ValueError(f'Unsupported file format: {suffix}')
