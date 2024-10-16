import gendiff.formatter.stylish as stylish
import gendiff.formatter.plain as plain
import gendiff.formatter.json as json


def apply_format(tree, format_name):
    match format_name:
        case 'stylish':
            return stylish.get_stylish(tree)
        case 'plain':
            return plain.get_plain(tree, [])
        case 'json':
            return json.get_json(tree)
        case _:
            raise FileNotFoundError
