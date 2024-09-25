import json
import yaml


def parser(file_path):
    *_, extension = file_path.split('.')
    with open(file_path, encoding='utf-8') as file:
        if extension == 'json':
            return json.load(file)
        elif extension in ('yml', 'yaml'):
            return yaml.safe_load(file)
