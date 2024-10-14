REPLACER = '    '
SPACE_COUNT = 1
SHIFT = '  '


def get_stylish(tree):
    return customize_output(tree, 0)


def customize_output(tree, depth):
    array = ['{']
    if not isinstance(tree, dict):
        return f'{cancel_json_translations(tree)}'
    curr_space_count = SPACE_COUNT + depth
    curr_indent = REPLACER * depth
    total_indent = REPLACER * curr_space_count
    indent_with_shift = curr_indent + SHIFT
    for key, val in tree.items():
        if isinstance(val, dict) and 'type' in val:
            for symbol, value in to_typify(val):
                array.append(f'{indent_with_shift}{symbol} {key}: '
                             f'{customize_output(value, curr_space_count)}')
        else:
            array.append(f'{total_indent}{key}: '
                         f'{customize_output(val, curr_space_count)}')
    array.append(curr_indent + '}')
    return '\n'.join(array)


def to_typify(dictionary):
    match dictionary['type']:
        case 'unchanged':
            return ((' ', dictionary['value']),)
        case 'added':
            return (('+', dictionary['value']),)
        case 'removed':
            return (('-', dictionary['value']),)
        case 'nested':
            return ((' ', dictionary['value']),)
        case 'changed':
            return ('-', dictionary['old']), ('+', dictionary['new'])


def cancel_json_translations(item):
    match item:
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case _:
            return item
