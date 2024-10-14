import json
import yaml


def get_python_dict(file_path):
    *_, file_format = file_path.split('.')
    with open(file_path, encoding='utf-8') as file:
        return parse(file, file_format)


def parse(content, file_format):
    match file_format:
        case 'json':
            return json.load(content)
        case 'yml' | 'yaml':
            return yaml.safe_load(content)
