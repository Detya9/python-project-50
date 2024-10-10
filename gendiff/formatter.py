def get_stylish(tree, replacer='    ', space_count=1, shift='  '):
    def walk(curr_value, depth):
        array = ['{']
        if not isinstance(curr_value, dict):
            return f'{cancel_json_translations(curr_value)}'
        curr_space_count = space_count + depth
        curr_indent = replacer * depth
        total_indent = replacer * curr_space_count
        indent_with_shift = curr_indent + shift
        for key, val in curr_value.items():
            if isinstance(val, dict) and 'type' in val:
                for symbol, value in to_typify(val):
                    array.append(f'{indent_with_shift}{symbol} {key}: {walk(value, curr_space_count)}')  # noqa: E501
            else:
                array.append(f'{total_indent}{key}: {walk(val, curr_space_count)}')  # noqa: E501
        array.append(curr_indent + '}')
        return '\n'.join(array)

    return walk(tree, 0)


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
