def get_plain(tree, array):
    result = []
    for key, value in tree.items():
        array.append(key)
        if value['type'] == 'nested':
            result.append(get_plain(value['value'], array))
        elif value['type'] == 'changed':
            result.append(f"Property \'{'.'.join(array)}\' was updated."
                          f" From {to_complex(value['old'])}"
                          f" to {to_complex(value['new'])}")
        elif value['type'] == 'removed':
            result.append(f"Property \'{'.'.join(array)}\' was removed")
        elif value['type'] == 'added':
            result.append(f"Property \'{'.'.join(array)}\' was added with "
                          f"value: {to_complex(value['value'])}")
        array.pop()
    return '\n'.join(result)


def to_complex(item):
    match item:
        case dict():
            return '[complex value]'
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case int():
            return item
        case _:
            return f"'{item}'"
