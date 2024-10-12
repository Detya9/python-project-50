def get_json(value, replacer='   ', space_count=1):
    def walk(curr_value, depth):
        array = ['{']
        if not isinstance(curr_value, dict):
            return f'{cancel_json_translations(curr_value)}'
        curr_space_count = space_count + depth
        curr_indent = replacer * depth
        total_indent = replacer * curr_space_count
        for key, val in curr_value.items():
            array.append(f'{total_indent}{key}: {walk(val, curr_space_count)}')
        array.append(curr_indent + '}')
        return '\n'.join(array)

    return walk(value, 0)


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
